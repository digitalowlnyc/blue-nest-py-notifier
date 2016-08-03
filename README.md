# Blue-nest-py-notifier
A python utility for creating recurring notifications using OSX dialogs or notifications

# Requirements
Python 3+

# Configuration
Edit the settings variable to add new recurring notifications:

```
schedule = [
        {
                "message": "30 seconds have passed, so I am showing a dialog!",  # A message to display
                "interval": 30,                                 # How long in seconds to wait for
                "type": "dialog",                                       # dialog or notification
        },
        {
                "message": "A minute has passed, so I am showing a notification!",
                "interval": 60,
                "type": "notification",
        }
]
```

a new entry will have three keys:
`message` - specifies the message to display in the alert
`interval` - how many seconds between alerts
`type` - "notification" or "dialog". Dialogs will show in the Finder application.

# Usage
python3 BlueNestPyTimer.py

# Notes
- For "dialog" type alerts, the thread for that specific alert will block until you dismiss the dialog. You need to make sure you close out dialogs so that they don't pile up on top of each other.
