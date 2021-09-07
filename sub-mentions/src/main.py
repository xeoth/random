import praw
import requests
from dotenv import load_dotenv
from os import getenv
from socket import gethostname
import logging
import re

load_dotenv()

reddit = praw.Reddit(
    username=getenv('SM_USERNAME'),
    password=getenv('SM_PASSWORD'),
    client_id=getenv('SM_ID'),
    client_secret=getenv('SM_SECRET'),
    user_agent=f"SubMentions on {gethostname()}"
)

logging.basicConfig(
    datefmt="%X %d.%m.%Y",
    format="[%(module)s] %(asctime)s | %(levelname)s: %(message)s",
    level=logging.INFO,
)

link_regex = re.compile(r'\[(?P<title>.+)]\((?P<url>[\w/?=;&]+)\)')

# tuple with usernames of the feedcomber bots, to prevent abuse.
FEEDCOMBER_USERNAMES = ("feedcomber-c1",
                        "feedcomber-c2",
                        "feedcomber-c3",
                        "feedcomber-c4",
                        "feedcomber-c5",
                        "feedcomber-c6",
                        "feedcomber-p1",
                        "feedcomber-p2",
                        "feedcomber-p3",
                        "feedcomber-p4",
                        "Xeoth")

def send_mention(title, comment_url: str):
    comment = reddit.comment(url=comment_url)
    requests.post(
        url=getenv("SM_WEBHOOK"),
        json={
            "embeds": [
                {
                    "title": title,
                    "description":  "> ".join(("> "+comment.body.lstrip()).splitlines(True)),
                    "url": comment_url
                }
            ]
        }
    )


if __name__ == '__main__' and not reddit.read_only:
    logging.info('Connected and running.')
    for message in reddit.inbox.stream():
        if message.author.name not in FEEDCOMBER_USERNAMES:
            continue
        # we now know that it's a message from feedcomber with a sub mention, let's process it
        if match := link_regex.search(message.body):
            # grabbing the URL
            url = match.groupdict()['url']
            
            # we have everything we need. send it off to discord!
            send_mention(message.subject, f"https://reddit.com{url}")
            logging.info(f"Message about https://reddit.com{url} sent")
            
            # we don't need the message anymore and it'd trigger re-sends when the bot restarts, so just delete it
            message.delete()
