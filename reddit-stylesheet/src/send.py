# Remember to fill out config.yaml

import praw
import os
from src.colors import bcolors


def send_stylesheet(reddit_instance, config):
    subreddit = reddit_instance.subreddit(config['options']['subreddit'])

    css_file = open('./fetched/stylesheet.css', 'r')
    try:
        subreddit.stylesheet.update(css_file.read())
    except:
        print(bcolors.FAIL +
              'Couldn\'t update the stylesheet. Does stylesheet.css exist?')
