import unittest
import time
from engine import Engine
from timer import Timer
from pulser import Pulser
import logic

class RS1TestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.logic = [logic.rs1_search_timer_PATCHED, logic.rs1_preset_1, logic.rs1_preset_2, logic.rs1_preset_2_led, logic.rs1_gate_closed_interlock, logic.rs1a_gate_closed_latch, logic.rs1_search_set, logic.rs1_search_led]
	
	def setUp(self):
		rs1_initial_state = logic.RSYState(
			RS1_SRCH_SET_LAT = False,
			RS1_SRCH_TMR_ACTV = False,
			RS1_GT_CLS_ILCK = False,
			RS1_PR1_KSW_RT = False,
			RS1_PR1_TESTBTN_RT = False,
			PERMITTED_ACCESS = True,
			RS1_PR1_LED = False,
			RS1_PR1_LAT = False,
			RS1_PR2_KSW_RT = False,
			RS1_PR2_TESTBTN_RT = False,
			RS1_PR2_LAT = False,
			RS1_DIB_ACTIVE = False,
			RS1_GT_CLS_RT = False,
			RS1_PR2_LED = False,
			ACR_HW_EN_RT = False,
			EPICS_ILCK_SET_BTN = False,
			RS1_GT_CLS_LAT = False,
			RS1_SRCH_SET_KSW_RT = False,
			RS1_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS1_SRCH_SET_BTN = False,
			RS1_SRCH_SET_LED = False
		)
		timer_fast_forward_factor = 20
		rs1_timers = logic.RSYTimers(
			RS1_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS1_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS1_DIB_PULSER =  Pulser(1),
			RS1_SEARCH_LED_PULSER = Pulser(1)
		)
		self.engine = Engine(rs1_initial_state, self.logic, timers=rs1_timers)
		self.engine.process() #Do one round of initial processing.
	
	def test_gate(self):
		# Close gate
		self.engine.state.RS1_GT_CLS_RT = True
		self.engine.process()
		self.assertTrue(self.engine.state.RS1_GT_CLS_RT, "RS1 Gate didn't stay closed.")
		self.assertFalse(self.engine.state.RS1_GT_CLS_LAT, "RS1 Gate latched without pressing interlock reset.")
		
		# Latch
		with self.engine.momentary_press(['EPICS_ILCK_SET_BTN']):
			self.assertFalse(self.engine.state.RS1_GT_CLS_LAT, "Gate latched without hardware enable.")
			with self.engine.momentary_press(['ACR_HW_EN_RT']):
				self.assertTrue(self.engine.state.RS1_GT_CLS_LAT, "RS1 Gate not latched with harware enable and interlock reset held.")
			self.assertTrue(self.engine.state.RS1_GT_CLS_LAT, "RS1 Gate didn't stay latched after releasing hardware enable.")
		self.assertTrue(self.engine.state.RS1_GT_CLS_LAT, "RS1 Gate didn't stay latched after releasing interlock reset.")			
		
		# Open again
		self.engine.state.RS1_GT_CLS_RT = False
		self.engine.process()
		self.assertFalse(self.engine.state.RS1_GT_CLS_RT, "RS1 Gate didn't stay open.")
		self.assertFalse(self.engine.state.RS1_GT_CLS_LAT, "RS1 Gate remained latched after opening.")
	
	def test_gate_dib(self):
		self.assertFalse(self.engine.state.RS1_GT_CLS_ILCK, "RS1 Gate interlock true without gate closed.")
		self.engine.state.RS1_GT_CLS_RT = True
		self.engine.process()
		self.assertTrue(self.engine.state.RS1_GT_CLS_ILCK, "RS1 gate interlock not active in P/A with gate closed.")
		self.engine.state.RS1_PR1_LAT = True
		self.engine.process()
		self.assertFalse(self.engine.timers.RS1_DIB_TMR.running(), "RS1 DIB timer running before turning RS1 PR2 Keyswitch.")
		with self.engine.momentary_press("RS1_PR2_KSW_RT"):
			self.assertTrue(self.engine.timers.RS1_DIB_TMR.running(), "RS1 DIB timer not running after turning RS1 PR2 Keyswitch.")
		self.assertTrue(self.engine.timers.RS1_DIB_TMR.running(), "RS1 DIB timer not running after releasing RS1 PR2 Keyswitch.")
		self.assertTrue(self.engine.state.RS1_DIB_ACTIVE, "RS1 DIB is not active while timer running.")
		self.assertTrue(self.engine.state.RS1_GT_CLS_ILCK, "RS1 Gate Closed Interlock is not True while RS1 DIB Active.")
		self.engine.state.RS1_GT_CLS_RT = False
		self.engine.process()
		self.assertTrue(self.engine.state.RS1_GT_CLS_ILCK, "RS1 Gate Closed Interlock is not True with gate open and RS1 DIB Active.")
		
		while (time.time() - self.engine.timers.RS1_DIB_TMR.time_started()) < self.engine.timers.RS1_DIB_TMR.duration():
			time.sleep(self.engine.timers.RS1_DIB_TMR.duration() / 10)
		
		time.sleep(self.engine.timers.RS1_DIB_TMR.duration())
		self.engine.process()
		self.assertFalse(self.engine.state.RS1_GT_CLS_ILCK, "RS1 Gate Closed Interlock still True even after DIB timer expired.")
	
	def test_search_logic(self):
		# Searcher enters zone.
		self.engine.state.RS1_GT_CLS_RT = True
		self.engine.process()
		self.assertFalse(self.engine.state.RS1_SRCH_TMR_ACTV, "RS1 Search Timer active before turning PR1 key.")

		# Searcher turns preset 1 key.
		with self.engine.momentary_press("RS1_PR1_KSW_RT"):
			self.assertTrue(self.engine.state.RS1_SRCH_TMR_ACTV, "RS1 Search Timer didn't start after PR1 key turned.")
			self.assertTrue(self.engine.state.RS1_PR1_LAT, "RS1 PR1 did not latch after turning key.")
		self.assertTrue(self.engine.state.RS1_PR1_LAT, "RS1 PR1 didn't stay latched after releasing PR1 key.")
		
		# Attempt to get search reset now.
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_RS1_SRCH_SET_BTN"]):
			self.assertFalse(self.engine.state.RS1_SRCH_SET_LAT, "RS1 Search Set without both preset 2.")
		
		# Searcher turns preset 2 key.
		with self.engine.momentary_press("RS1_PR2_KSW_RT"):
			self.assertTrue(self.engine.state.RS1_PR2_LAT, "RS1 PR2 did not latch after turning key.")
		self.assertTrue(self.engine.state.RS1_PR2_LAT, "RS1 PR2 did not stay latched after releasing PR2 key.")
		
		# Searcher opens gate to exit.
		self.engine.state.RS1_GT_CLS_RT = False
		self.engine.process()
		time.sleep(self.engine.timers.RS1_DIB_TMR.duration()/5) #Take some non-zero amount of time to exit
		self.engine.state.RS1_GT_CLS_RT = True #Close gate on the way out
		self.engine.process()
		
		# Get interlock reset to latch gate
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_ILCK_SET_BTN"]):
			pass
		
		# Get RS1 search set
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_RS1_SRCH_SET_BTN"]):
			with self.engine.momentary_press("RS1_SRCH_SET_KSW_RT"):
				pass
		self.assertTrue(self.engine.state.RS1_SRCH_SET_LAT, "RS1 search not set with all conditions met.")