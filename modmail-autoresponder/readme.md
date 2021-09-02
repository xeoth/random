# Modmail Autoresponder

**THIS IS SUPPOSED TO RUN ON A SCHEDULE IN CRON!!!**

Set up a cron job with `crontab -e` - I recommend running it every 15 minutes, so put 

```
*/15 * * * * python /path/to/main.py
```

in your cronjobs config file.
