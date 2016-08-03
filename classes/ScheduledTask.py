import threading
import subprocess
import functools

'''
Class for task scheduling
'''

class ScheduledTask():

	initialized = False
	runOnFirstSchedule = False

	def __init__(self, funcToSchedule, interval, runOnFirstSchedule = False):
		self.runOnFirstSchedule = runOnFirstSchedule
		scheduleFunction = self.getTaskLambda(funcToSchedule, interval)
		scheduleFunction()

	def getTaskLambda(self, funcToSchedule, interval):
		def doTask():
			threading.Timer(interval, self.getTaskLambda(funcToSchedule, interval)).start()

			# If we are the initial thread, we don't want to block whoever is creating this task thread
			if self.initialized:
				funcToSchedule()
			else:
				self.initialized = True
				if(self.runOnFirstSchedule):
					threading.Thread(target = funcToSchedule).start()

		return doTask