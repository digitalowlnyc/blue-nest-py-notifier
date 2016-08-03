'''
Usage: python3 py-timer.py

Python Version: 3+

About: This is a Mac OSX utility to schedule alerts on a set interval.
The alerts can be either notifications or dialogs. Dialogs will 
show in the "Finder" application by default

'''

import time, functools, sys

from libs import MacNotifications as MacNotificationsLib
from classes import ScheduledTask

def getCurrentTime():
	return time.strftime("%H:%M:%S")

def printHeartbeat():
	print("Heartbeat at " + getCurrentTime())

def runApplication(appName, schedule, heartbeatInterval):
	#log("Running ", appName, " with schedule ", schedule)

	MacNotificationsLib.notify("Mac timer has started", appName)

	# Callbacks for different alert types
	def doNotify(msg):
		MacNotificationsLib.notify("{}: {}".format(getCurrentTime(), msg), appName)

	def doDialog(msg):
		MacNotificationsLib.displayDialog("{}: {}".format(getCurrentTime(), msg), appName)

	# Heartbeat so we know we are still running and are not blocked
	ScheduledTask.ScheduledTask(printHeartbeat, heartbeatInterval)

	for entry in schedule:

		if entry["type"] not in ["notification", "dialog"]:
			raise Exception("Bad timer type: " + entry["type"])

		message = "{}".format(entry["message"]);

		if entry["type"] == "notification":
			boundCallback = functools.partial(doNotify, message);
		else:
			boundCallback = functools.partial(doDialog, message);

		ScheduledTask.ScheduledTask(boundCallback, entry["interval"])
		print("Task was scheduled {}".format(entry))

heartbeatInterval = 5

schedule = [
	{
		"message": "30 seconds have passed, so I am showing a dialog!",  # A message to display
		"interval": 30, 				# How long in seconds to wait for
		"type": "dialog", 					# dialog or notification
	},
	{
		"message": "A minute has passed, so I am showing a notification!",
		"interval": 60,
		"type": "notification",
	}
]

runApplication(sys.argv[0], schedule, heartbeatInterval)