import epics
from logic import RSYState
class Engine:
	def __init__(self, input_map, output_map):
		self.bit_to_pv_map = {}
		self.input_map = input_map
		self.output_map = output_map
		self.bit_to_pv_map.update(self.input_map)
		self.bit_to_pv_map.update(self.output_map)
		self.pv_to_bit_map = {pv: bit for pv, bit in bit_to_pv_map.items()}
		
	def read_state(self):
		state_values = {pv: val for pv, val in zip(self.pv_to_bit_map.keys(), epics.caget_many(self.pv_to_bit_map.keys())}
		return RSYState(**state_values)
	
	def write_state(self, state):
		output_values = [getattr(state, bit) for bit in self.output_map.keys()]
		results = epics.caput_many(self.output_map.values(), output_values, timeout=10.0)
		if not all([result == 1 for result in results]):
			failed_pvs = [pv for (pv, result) in zip(self.output_map.values(), results)]
			raise Exception(f"Could not write state to PVs.  Failed PVs: {failed_pvs.join("\n")}")