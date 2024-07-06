import time
class Pulser:
	def __init__(self, period, initial_value=False):
		self._period = period
		self._value = initial_value
		self._time_started = None
		self._running = False
	
	def start(self):
		self._running = True
		self._time_started = time.time()
	
	def running(self):
		return self._running
	
	def stop(self):
		self._running = False
	
	def __bool__(self):
		if not self._running:
			return False
		return not int((time.time() - self._time_started)/self._period) % 2