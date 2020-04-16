import os
import time
import yaml
from watchdog.observers import Observer
from datetime import datetime, timedelta
from watchdog.events import FileSystemEventHandler

config = yaml.safe_load(open('config.yaml'))


def clear(): return os.system('clear')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


clear()
print(bcolors.BOLD + f'Reddit Stylesheet Updater')
print(
    f'{bcolors.ENDC}Currently working on /r/{config["options"]["subreddit"]}')
print('Use Ctrl+C to exit')
print('---')

# fetch stylesheet
os.system('python3 ./src/fetch.py')
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

        print(bcolors.OKGREEN + 'Latest change sent to Reddit successfully.')
        os.system('python3 ./src/send.py')


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
