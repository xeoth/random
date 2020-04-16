"""
This will overwrite any contents of fetched_css.css!
Remember to fill out config.yaml!
"""

import yaml
import praw


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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

subreddit_name = config['options']['subreddit']

css_contents = reddit.subreddit(subreddit_name).stylesheet()

# writing to the file
file = open('./fetched/stylesheet.css', 'w')
file.write(css_contents.stylesheet)
file.close()

print(bcolors.OKBLUE + 'Successfully fetched! Check /fetched/stylesheet.css')
