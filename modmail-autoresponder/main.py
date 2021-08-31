from os import getenv

import praw
from dotenv import load_dotenv

load_dotenv()

AUTORESPONDER_MESSAGE = """
Hello! r/{} is currently private as Reddit has taken a laissez-faire approach to handling misinformation on their platfom.

Last week, hundreds of subreddits stood together and requested Reddit take action against COVID-19 misinformation.

Reddit's response was insufficient and took an approach that both sides carry equal weight.

We have gone private to spread awareness and to urge more concrete and tangible action from reddit that helps protect users from dangerous misinformation.

Please help this initiative by reporting covid misinformation on reddit: https://www.reddit.com/report?reason=this-is-misinformation

Read more about this protest in this post: https://reddit.com/pbe8nj.

**This is temporary and we hope that we'll be able to unprivate the subreddit in a few days.** Hopefully this message clears up any confusion. In case you have questions that haven't been answered here, reply to this message and a human will come along soon to assist you.
"""

sub = getenv('MAR_SUBREDDIT')

reddit = praw.Reddit(
    username=getenv('MAR_USERNAME'),
    password=getenv('MAR_PASSWORD'),
    client_id=getenv('MAR_ID'),
    client_secret=getenv('MAR_SECRET'),
    user_agent=f"{sub}'s Modmail Autoresponder"
)


for conversation in reddit.subreddit(sub).modmail.conversations(state='new'):
    conversation.reply(AUTORESPONDER_MESSAGE.format(sub), author_hidden=True)
    conversation.archive()
