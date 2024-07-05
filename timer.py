import time
class Timer:
	def __init__(self, duration):
		self._duration = duration
		self._running = False
		self._time_started = None
		
	def elapsed_time(self):
		if not self._running:
			return 0
		return time.time() - self._time_started
	
	def start(self):
		self._running = True
		self._time_started = time.time()
	
	def stop(self):
		self._running = False
		self._time_started = None
	
	def running(self):
		return self._running
		
	def duration(self):
		return self._duration
	
	def time_started(self):
		return self._time_started
	
	def __bool__(self):
		return self._running and not self.done()
	
	def done(self):
		return self.elapsed_time() >= self._duration