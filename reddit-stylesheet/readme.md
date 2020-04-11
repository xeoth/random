# Reddit Stylesheet Updater

Allows for fetching a sub's stylesheet, editing it locally, and sending it back to the server.

This project took me longer than expected, but I'm happy with the result.

## Usage

Fill out [config.yaml](./config.yaml) with correct values (you might want to check out the [developed applications](https://www.reddit.com/prefs/apps) page)

Run [fetch.py](./fetch.py) to fetch the stylesheet from the specified subreddit.

Use [Prettier](https://prettier.io/) to lint and format it

Make necessary changes in the newly created stylesheet.css (it's important that you keep the name)

Run [send.py](./send.py) to update the subreddit's stylesheet

## Dependencies

- praw (`pip3 install praw`)
- requests (`pip3 install requests`)
- yaml (`pip3 install pyyaml`)
