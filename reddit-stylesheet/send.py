# Remember to fill out config.yaml

import praw
import yaml
import os

# initializing values from config.yaml
config = yaml.safe_load(open('config.yaml'))


# adding the 2FA to the password
password = config['credentials']['password']
if config['options']['two_factor_auth']:
    password += ':' + input('Please enter the 2 factor authentication code: ')


# trying to log in
reddit = praw.Reddit(
    client_id=config['credentials']['client_id'],
    client_secret=config['credentials']['client_secret'],
    password=password,
    username=config['credentials']['username'],
    user_agent='StylesheetUpdater'
)


# actual updating starts here
subreddit = reddit.subreddit(config['options']['subreddit'])

css_file = open('stylesheet.css', 'r')
try:
    subreddit.stylesheet.update(css_file.read())
except:
    print('Couldn\'t update the stylesheet. Does stylesheet.css exist?')
