import os
import time
import yaml
import praw
from prawcore import exceptions
from watchdog.events import FileSystemEventHandler
from datetime import datetime, timedelta
from watchdog.observers import Observer
from src.fetch import fetch_stylesheet
from src.send import send_stylesheet
from src.colors import bcolors
from sys import exit

config = yaml.safe_load(open('config.yaml'))


def clear(): return os.system('clear')


# clear screen and display the header
clear()
print(bcolors.HEADER + 'Reddit Stylesheet Updater')

# adding the 2FA to the password
password = config['credentials']['password']
if config['options']['two_factor_auth']:
    password += ':' + input(bcolors.ENDC +
                            'Please enter the 2 factor authentication code: ')

# trying to log in

reddit = praw.Reddit(
    client_id=config['credentials']['client_id'],
    client_secret=config['credentials']['client_secret'],
    password=password,
    username=config['credentials']['username'],
    user_agent='StylesheetUpdater'
)


# display info
print(
    f'{bcolors.ENDC}Currently working on /r/{config["options"]["subreddit"]}')
print('Use Ctrl+C to exit')
print('---')

# fetch stylesheet
try:
    fetch_stylesheet(reddit, config)
except exceptions.OAuthException:
    print(bcolors.FAIL + 'Wrong credentials! Check config.yaml for any mistakes and make sure you\'re inputting the correct 2FA code (if applicable).')
    exit(1)


# watch for file changes
# for each save, send this to reddit


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()

        print(bcolors.OKGREEN + datetime.now().isoformat(timespec='seconds').split('T')[1],
              'Latest change sent to Reddit successfully.')
        send_stylesheet(reddit, config)


handler = FileChangeHandler()
observer = Observer()
observer.schedule(handler, path='./fetched/', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
