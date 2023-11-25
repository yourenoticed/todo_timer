import time

class Timer():
	def __init__(self, start_time, id=0, paused=False):
		self.id = id
		self.start_time = start_time
		self.paused = paused

	def stop_timer(self):
		self.paused = True

	def counter_timer(self):
		pass
