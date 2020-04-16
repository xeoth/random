# Reddit Stylesheet Updater

Allows for fetching a sub's stylesheet, editing it locally, and sending it back to reddit.

This project took me longer than expected, but I'm happy with the result.

## Usage

Fill out [config.yaml](./config.yaml) with correct values (you might want to check out the [developed applications](https://www.reddit.com/prefs/apps) page)

Run [init.py](init.py) and edit [stylesheet.css](./fetched/stylesheet.css). Changes will be uploaded to Reddit every time you save the file.

## Dependencies

- praw (`pip3 install praw`)
- yaml (`pip3 install pyyaml`)
- watchdog (`pip3 install watchdog`)
