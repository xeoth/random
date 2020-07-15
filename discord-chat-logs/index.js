const Discord = require("discord.js");
const fs = require("fs");
const config = require("./config.json");

const client = new Discord.Client();

client.on("ready", () => {
  console.log("ready");
});

client.on("message", (message) => {
  if (!message.content.startsWith(config.prefix)) return;

  if (message.author.id !== config.ownerID) return;

  const args = message.content.slice(config.prefix.length).trim().split(/ +/g);
  if (args[0] === "dumpmsg") {
    // show initiation of logging process
    message.channel.startTyping();

    let amountToFetch = args[1];

    const fileName = `${+new Date()}_${message.channel.name}_logs.txt`;
    const stream = fs.createWriteStream(`./${fileName}`, { flags: "a" });

    console.log(
      `Dumping ${amountToFetch} messages into ${fileName}. Requested by ${message.author.tag}`
    );

    stream.write(new Date().toString());

    // the message starting from which messages will be fetched
    let lastMessageID = message.channel.lastMessageID;

    while (amountToFetch > 0) {
      // discord only allows for fetching 100 msg. at the time
      const currentLimit = amountToFetch >= 100 ? 100 : amountToFetch;

      message.channel.messages
        .fetch({ limit: currentLimit, before: lastMessageID })
        .then((messages) => {
          const msgArr = messages.array();
          msgArr.forEach((el) => {
            if (!message.content) return;
            stream.write(`<${el.author.tag}> ${el.content}\n`);
          });

          lastMessageID = msgArr[msgArr.length - 1].id;
        });

      amountToFetch -= currentLimit;
    }

    stream.write(new Date().toString());

    message.reply(`Dumped the last ${args[1]} messages into \`${fileName}\`.`);
    message.channel.stopTyping();
  }
});

client.login(config.token);
