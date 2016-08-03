import subprocess

'''
Library for displaying notifications and dialogs in OSX
'''

def notify(text, title="", subtitle=""):
	script = '''on run argv
	set notificationTitle to (item 1 of argv)
	set notificationSubtitle to (item 2 of argv)
	set notificationText to (item 3 of argv)
	
	display notification notificationText with title notificationTitle subtitle notificationSubtitle
	end run'''

	if(title == '' and subtitle == ''):
		script.replace(" with title notificationTitle subtitle notificationSubtitle", "")
	elif(subtitle == ''):
		script.replace(" subtitle notificationSubtitle", "")
	elif(title == ''):
		script.replace(" title notificationTitle", "")

	subprocess.call(["osascript", "-e", script, title, subtitle, text])

def displayDialog(text, title="", application = "Finder"):
	script = '''on run argv
	set notificationTitle to (item 1 of argv)
	set notificationText to (item 2 of argv)	

	tell app "{}" to display dialog notificationText with title notificationTitle
	end run'''.format(application)

	print(script)
	if(title == ''):
		script.replace(" with title notificationTitle", "")

	subprocess.call(["osascript", "-e", script, title, text])