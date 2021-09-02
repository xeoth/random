# Sub Notifications

Send redditcomber.com's notifications to a Discord channel.

## Setup

Create a .env file and fill it out

```env
SM_USERNAME=
SM_PASSWORD=
SM_ID=
SM_SECRET=
SM_WEBHOOK=
```

`SM_USERNAME`, `SM_PASSWORD` are Reddit's username and password, `SM_ID`, `SM_SECRET` can be obtained by logging into the account and going to https://reddit.com/prefs/apps and creating a script-type app.

`SM_WEBHOOK` is the webhook link provided by Discord. More info here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks.