"""
This will overwrite any contents of fetched_css.css!
Remember to fill out config.yaml!
"""

import yaml
import praw
import os
from colors import bcolors


def fetch_stylesheet(reddit_instance, config):
    subreddit_name = config['options']['subreddit']

    css_contents = reddit_instance.subreddit(subreddit_name).stylesheet()

    # checking whether dir exists and creating it if not
    if not os.path.isdir('./fetched'):
        os.mkdir('./fetched')

    # writing to the file
    file = open('./fetched/stylesheet.css', 'w')
    file.write(css_contents.stylesheet)
    file.close()

    print(bcolors.OKBLUE + 'Successfully fetched! Check /fetched/stylesheet.css')
