class MomentaryPress:
	def __init__(self, engine, keys, process=True):
		if isinstance(keys, str):
			keys = [keys]
		self.keys = keys
		self.initial_state = engine.state.copy()
		self.engine = engine
		self.process = process
	
	def __enter__(self):
		for key in self.keys:
			setattr(self.engine.state,key,True)
		if self.process:
			self.engine.process()
	
	def __exit__(self, type, value, traceback):
		for key in self.keys:
			setattr(self.engine.state,key, getattr(self.initial_state,key))
		if self.process:
			self.engine.process()

class Engine:
	def __init__(self, initial_state, logic_blocks, timers=None):
		self.state = initial_state
		self.prev_state = initial_state
		self.blocks = logic_blocks
		self.timers = timers
		
	
	def process(self):
		for block in self.blocks:
			new_state = block(self.state, self.prev_state, self.timers)
			self.state = new_state
		self.prev_state = self.state.copy()
	
	def momentary_press(self, keys, process=True):
		return MomentaryPress(self, keys, process)