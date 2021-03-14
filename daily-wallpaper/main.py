import ctypes
import requests
import shutil
from getpass import getuser
from random import choice

# basic config values
SUBREDDITS = ("wallpapers", "imaginarybattlefields", "imaginarycityscapes",
              "imaginaryarchitecture", "imaginaryinteriors", "imaginarycybernetics", "imaginarycyberpunk")
MODE = "random"  # set to random to select one random subreddit from the list above on each run. keep at multireddit to choose from all of the subreddits at once
MIN_HEIGHT = 1080
MIN_WIDTH = 1920

# advanced config values - don't touch unless you know what you're doing
TMP_FOLDER = f"C:\\Users\\{getuser()}\\AppData\\Local\\Temp"

# construct the URI
if MODE == "multireddit":
    url = f"https://reddit.com/r/{''.join([sub + '+' for sub in SUBREDDITS])}.json"
elif MODE == "random":
    url = f"https://reddit.com/r/{choice(SUBREDDITS)}.json"
else:
    raise ValueError(
        "Invalid value of MODE - select either 'multireddit' or 'random'.")

# fetching the new wallpaper
r = requests.get(url, headers={"User-Agent": "Daily Wallpaper"})

if r.status_code != 200:
    print(r.status_code)
    raise Exception("A Reddit API error has occured.")

response = r.json()

for entry in response["data"]["children"]:
    data = entry["data"]
    if data["post_hint"] != "image":
        continue

    elif data["preview"]["images"][0]["source"]["width"] < MIN_WIDTH or \
            data["preview"]["images"][0]["source"]["height"] < MIN_HEIGHT:
        continue

    req = requests.get(data["url"], headers={
                       "User-Agent": "Daily Wallpaper"}, stream=True)
    req.raw.decode_content = True

    with open(path := TMP_FOLDER+"\\wallpaper.jpg", "wb") as f:
        shutil.copyfileobj(req.raw, f)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
