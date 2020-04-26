# Remember to fill out config.yaml

import praw
import os
from colors import bcolors

# actual updating starts here
subreddit = reddit.subreddit(config['options']['subreddit'])

css_file = open('./fetched/stylesheet.css', 'r')
try:
    subreddit.stylesheet.update(css_file.read())
except:
    print(bcolors.FAIL + 'Couldn\'t update the stylesheet. Does stylesheet.css exist?')
