import unittest
import time
from engine import Engine
from timer import Timer
from pulser import Pulser
from generic_test import gate_door_test, gate_dib_test
import logic
import logging

class RS5_913_TestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.logic = [logic.rs5_search_timer, logic.rs5_913_preset_1, logic.rs5_913_preset_2, logic.rs5_913_preset_2_led,
					logic.rs5_913_wdoor_closed_interlock, logic.rs5_913_wdr_closed_latch, logic.rs5_913_sdr_closed_latch,
					logic.rs5_913_all_doors_closed, logic.rs5_913_preserved_search, logic.rs5_913_preserved_search_led,
					logic.rs5_preset_1, logic.rs5_preset_2, logic.rs5_preset_2_led, logic.rs5a_gate_closed_interlock, 
					logic.rs5a_gate_closed_latch, logic.rs5b_gate_closed_latch, logic.rs5c_gate_closed_latch, logic.rs5de_gate_closed_latch,
					logic.rs5_all_gates_closed, logic.rs5_search_set, logic.rs5_all_gates_and_doors_closed,
					logic.rs5_search_led
					]
	
	def setUp(self):
		rs5_913_initial_state = logic.RSYState(
			RS1_SRCH_SET_LAT = False,
			RS1_SRCH_TMR_ACTV = False,
			RS1A_GT_CLS_ILCK = False,
			RS1_PR1_KSW_RT = False,
			RS1_PR1_TESTBTN_RT = False,
			PERMITTED_ACCESS = True,
			RS1_PR1_LED = False,
			RS1_PR1_LAT = False,
			RS1_PR2_KSW_RT = False,
			RS1_PR2_TESTBTN_RT = False,
			RS1_PR2_LAT = False,
			RS1_DIB_ACTIVE = False,
			RS1A_GT_CLS_RT = False,
			RS1_PR2_LED = False,
			ACR_HW_EN_RT = False,
			EPICS_ILCK_SET_BTN = False,
			RS1A_GT_CLS_LAT = False,
			RS1_SRCH_SET_KSW_RT = False,
			RS1_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS1_SRCH_SET_BTN = False,
			RS1_SRCH_SET_LED = False,

			RS2_406_PR1_KSW_RT = False,
			RS2_406_PR1_TESTBTN_RT = False,
			RS2_406_PR1_LAT = False,
			RS2_406_PR1_LED = False,
			RS2_406_PRSVD_SRCH = False,
			RS2_SRCH_TMR_ACTV = False,
			RS2_406_SDR_CLS_ILCK = False,
			RS2_406_WDR_CLS_RT = False,
			RS2_406_RUDR_CLS_RT = False,
			RS2_406_PR2_LAT = False,
			RS2_406_PR2_KSW_RT = False,
			RS2_406_PR2_TESTBTN_RT = False,
			RS2_406_DIB_ACTIVE = False,
			RS2_406_PR2_LED = False,
			RS2_406_SDR_CLS_RT = False,
			RS2_406_WDR_CLS_LAT = False,
			RS2_406_RUDR_CLS_LAT = False,
			RS2_406_ALL_DRS_CLS_LAT = False,
			RS2_406_PRSVD_SRCH_LED = False,

			RS2_407_PR1_LAT = False,
			RS2_407_PR1_KSW_RT = False,
			RS2_407_PR1_TESTBTN_RT = False,
			RS2_407_PRSVD_SRCH = False,
			RS2_406_SDR_CLS_LAT = False,
			RS2_407_SDR_CLS_ILCK = False,
			RS2_407_NDR_CLS_RT = False,
			RS2_407_EDR_CLS_RT = False,
			RS2_407_PR1_LED = False,
			RS2_407_PR2_LAT = False,
			RS2_407_PR2_KSW_RT = False,
			RS2_407_PR2_TESTBTN_RT = False,
			RS2_407_DIB_ACTIVE = False,
			RS2_407_PR2_LED = False,
			RS2_407_SDR_CLS_RT = False,
			RS2_407_NDR_CLS_LAT = False,
			RS2_407_SDR_CLS_LAT = False,
			RS2_407_EDR_CLS_LAT = False,
			RS2_407_ALL_DRS_CLS_LAT = False,
			RS2_407_PRSVD_SRCH_LED = False,

			RS2_PR1_LAT = False,
			RS2_PR1_KSW_RT = False,
			RS2_PR1_TESTBTN_RT = False,
			RS2_SRCH_SET_LAT = False,
			RS2A_GT_CLS_ILCK = False,
			RS2_PR1_LED = False,
			RS2_PR2_LAT = False,
			RS2_PR2_KSW_RT = False,
			RS2_PR2_TESTBTN_RT = False,
			RS2_DIB_ACTIVE = False,
			RS2_PR2_LED = False,
			RS2A_GT_CLS_RT = False,
			RS2A_GT_CLS_LAT = False,
			RS2_ALL_GTS_DRS_CLS_LAT = False,
			RS2_SRCH_SET_KSW_RT = False,
			RS2_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS2_SRCH_SET_BTN = False,
			RS2_SRCH_SET_LED = False,

			RS3_911_PR1_KSW_RT = False,
			RS3_911_PR1_TESTBTN_RT = False,
			RS3_911_PR1_LAT = False,
			RS3_911_PR1_LED = False,
			RS3_911_EDR_CLS_ILCK = False,
			RS3_911_PRSVD_SRCH_LAT = False,
			RS3_911_PR2_LAT = False,
			RS3_911_PR2_KSW_RT = False,
			RS3_911_PR2_TESTBTN_RT = False,
			RS3_911_PR2_LED = False,
			RS3_911_DIB_ACTIVE = False,
			RS3_911_EDR_CLS_RT = False,
			RS3_911_EDR_CLS_LAT = False,
			RS3_911_PRSVD_SRCH_LED = False,
			RS3_SRCH_TMR_ACTV = False,
			RS3_PR1_LAT = False,
			RS3_PR1_LED = False,
			RS3_PR1_KSW_RT = False,
			RS3_PR1_TESTBTN_RT = False,
			RS3_SRCH_SET_LAT = False,
			RS3A_GT_CLS_ILCK = False,
			RS3B_GT_CLS_RT = False,
			RS3C_GT_CLS_RT = False,
			RS3_PR2_LAT = False,
			RS3_PR2_LED = False,
			RS3_DIB_ACTIVE = False,
			RS3_PR2_KSW_RT = False,
			RS3_PR2_TESTBTN_RT = False,
			RS3A_GT_CLS_RT = False,
			RS3A_GT_CLS_LAT = False,
			RS3B_GT_CLS_LAT = False,
			RS3C_GT_CLS_LAT = False,
			RS3_ALL_GTS_CLS_LAT = False,
			RS3_SRCH_SET_KSW_RT = False,
			RS3_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS3_SRCH_SET_BTN = False,
			RS3_ALL_GTS_DRS_CLS_LAT = False,
			RS3_SRCH_SET_LED = False,

			RS4_912_PR1_KSW_RT = False,
			RS4_912_PR1_TESTBTN_RT = False,
			RS4_SRCH_TMR_ACTV = False,
			RS4_912_WDR_CLS_ILCK = False,
			RS4_912_PR1_LED = False,
			RS4_912_PR1_LAT = False,
			RS4_912_PR2_KSW_RT = False,
			RS4_912_PR2_TESTBTN_RT = False,
			RS4_912_PRSVD_SRCH_LAT = False,
			RS4_912_PR2_LAT = False,	
			RS4_PR1_LAT = False,
			RS4_PR1_KSW_RT = False,
			RS4_PR1_TESTBTN_RT = False,
			RS4_SRCH_SET_LAT = False,
			RS4_912_DIB_ACTIVE = False,
			RS4_912_PR2_LED = False,
			RS4_912_WDR_CLS_RT = False,
			RS4_912_WDR_CLS_LAT = False,
			RS4_912_PRSVD_SRCH_LED = False,			
			RS4A_GT_CLS_ILCK = False,
			RS4B_GT_CLS_RT = False,
			RS4C_GT_CLS_RT = False,
			RS4_DIB_ACTIVE = False,
			RS4_PR2_LAT = False,
			RS4_PR2_LED = False,
			RS4_PR2_KSW_RT = False,
			RS4_PR2_TESTBTN_RT = False,
			RS4A_GT_CLS_RT = False,
			RS4A_GT_CLS_LAT = False,
			RS4B_GT_CLS_LAT = False,
			RS4C_GT_CLS_LAT = False,
			RS4_ALL_GTS_CLS_LAT = False,
			RS4_SRCH_SET_KSW_RT = False,
			RS4_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS4_SRCH_SET_BTN = False,
			RS4_ALL_GTS_DRS_CLS_LAT = False,
			RS4_SRCH_SET_LED = False,

			RS5_913_PR1_KSW_RT = False,
			RS5_913_PR1_TESTBTN_RT = False,
			RS5_913_PRSVD_SRCH_LAT = False,
			RS5_SRCH_TMR_ACTV = False,
			RS5_913_SDR_CLS_RT = False,
			RS5_913_SDR_CLS_LAT = False,
			RS5_913_WDR_CLS_ILCK = False,
			RS5_913_PR1_LED = False,
			RS5_913_PR1_LAT = False,
			RS5_913_PR2_KSW_RT = False,
			RS5_913_PR2_TESTBTN_RT = False,
			RS5_913_PR2_LAT = False,
			RS5_913_DIB_ACTIVE = False,
			RS5_913_PR2_LED = False,
			RS5_PR1_LAT = False,
			RS5_PR1_KSW_RT = False,
			RS5_SRCH_SET_LAT = False,
			RS5_913_WDR_CLS_RT = False,
			RS5_913_WDR_CLS_LAT = False,
			RS5_913_PRSVD_SRCH_LED = False,
			EPICS_RS5_SRCH_SET_BTN = False,
			RS5_PR1_TESTBTN_RT = False,
			RS5A_GT_CLS_ILCK = False,
			RS5B_GT_CLS_RT = False,
			RS5C_GT_CLS_RT = False,
			RS5DE_GT_CLS_RT = False,
			RS5_DIB_ACTIVE = False,
			RS5_PR2_LAT = False,
			RS5_PR2_LED = False,
			RS5_PR2_KSW_RT = False,
			RS5_PR2_TESTBTN_RT = False,
			RS5A_GT_CLS_RT = False,
			RS5A_GT_CLS_LAT = False,
			RS5B_GT_CLS_LAT = False,
			RS5C_GT_CLS_LAT = False,
			RS5DE_GT_CLS_LAT = False,
			RS5_ALL_GTS_CLS_LAT = False,
			RS5_SRCH_SET_KSW_RT = False,
			RS5_SRCH_SET_TESTBTN_RT = False,
			RS5_ALL_GTS_DRS_CLS_LAT = False,
			RS5_SRCH_SET_LED = False,
			RS5_913_ALL_DRS_CLS_LAT = False,

			RT1_PR1_KSW_RT = False,
			RT1_PR1_TESTBTN_RT = False,
			RT1_PR2_KSW_RT = False,
			RT1_PR2_TESTBTN_RT = False,
			RT1_SRCH_SET_KSW_RT = False,
			EPICS_RT1_SRCH_SET_BTN = False, 
			RT1_PR1_LED = False,
			RT1_PR2_LED = False,
			RT1_SRCH_SET_LED = False,
			RT1_PR1_LAT = False,
			RT1_SRCH_SET_LAT = False,
			RT1_SRCH_TMR_ACTV = False,
			RT1A_GT_CLS_ILCK = False,
			RT1B_GT_CLS_RT = False,
			RT1_PR2_LAT = False,
			RT1_DIB_ACTIVE = False,
			RT1A_GT_CLS_RT = False,
			RT1A_GT_CLS_LAT = False,
			RT1B_GT_CLS_LAT = False,
			RT1_ALL_GTS_CLS_LAT = False,

			KYBNK_N_REL_EPICS_BTN = False,
			KYBNK_N_REL = False,
			KYBNK_S_REL_EPICS_BTN = False,
			KYBNK_S_REL = False,
			KYBNK_N_COMPLETE_RT = False,
			KYBNK_N_CMPLT_LAT = False,
			KYBNK_S_COMPLETE_RT = False,
			KYBNK_S_CMPLT_LAT = False,
			ALL_KYBNK_CMPLT_LAT = False,
			RSY_ZN_CLS_LAT = False,
			ILCKS_CMPLT = False,
			RSY_SRCHD = False,
			RSY_SECURITY_VIOLATION = False,
			EPICS_NO_ACCESS_BTN = False,
			EPICS_PERMITTED_ACCESS_BTN = False,
			NO_ACCESS = False,
			AV_WARN_CMPLT = False,
			AV_WARN = False,
			RSY_SECURE = False,
		)
		timer_fast_forward_factor = 10
		rs5_913_timers = logic.RSYTimers(
			RS1_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS1_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS1_DIB_PULSER =  Pulser(1),
			RS1_SEARCH_LED_PULSER = Pulser(1),

			RS2_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS2_406_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS2_406_DIB_PULSER =  Pulser(1),
			RS2_406_SEARCH_LED_PULSER = Pulser(1),

			RS2_407_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS2_407_DIB_PULSER =  Pulser(1),
			RS2_407_SEARCH_LED_PULSER = Pulser(1),

			RS2_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS2_DIB_PULSER =  Pulser(1),
			RS2_SEARCH_LED_PULSER = Pulser(1),

			RS3_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS3_911_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS3_911_DIB_PULSER =  Pulser(1),
			RS3_911_SEARCH_LED_PULSER = Pulser(1),

			RS3_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS3_DIB_PULSER =  Pulser(1),
			RS3_SEARCH_LED_PULSER = Pulser(1),

			RS4_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS4_912_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS4_912_DIB_PULSER =  Pulser(1),
			RS4_912_SEARCH_LED_PULSER = Pulser(1),

			RS4_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS4_DIB_PULSER =  Pulser(1),
			RS4_SEARCH_LED_PULSER = Pulser(1),

			RS5_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS5_913_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS5_913_DIB_PULSER =  Pulser(1),
			RS5_913_SEARCH_LED_PULSER = Pulser(1),

			RS5_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS5_DIB_PULSER =  Pulser(1),
			RS5_SEARCH_LED_PULSER = Pulser(1),

			RT1_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RT1_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RT1_DIB_PULSER =  Pulser(1),
			RT1_SEARCH_LED_PULSER = Pulser(1),

			AV_WARN_TMR = Timer(10/timer_fast_forward_factor),
		)
		self.engine = Engine(rs5_913_initial_state, self.logic, timers=rs5_913_timers)
		self.engine.process() #Do one round of initial processing.
	
	def test_01_gate_rs5_913(self):
		gate_door_test(self, 'RS5_913_WDR_CLS_RT', 'RS5_913_WDR_CLS_LAT', 'RS5 913 WDR')
		gate_door_test(self, 'RS5_913_SDR_CLS_RT', 'RS5_913_SDR_CLS_LAT', 'RS5 913 SDR')

	def test_02_gate_rs5_913_dib(self):
		gate_dib_test(self, gate_rt_name='RS5_913_WDR_CLS_RT', gate_interlock_name='RS5_913_WDR_CLS_ILCK', dib_timer_name='RS5_913_DIB_TMR', 
					dib_active_name='RS5_913_DIB_ACTIVE', preset_1_name='RS5_913_PR1_LAT', preset_2_led_name='RS5_913_PR2_LED', preset_2_ksw_name='RS5_913_PR2_KSW_RT', 
					gate_list=['RS5_913_SDR_CLS_RT'], zone_name='RS5 913')

	def test_03_search_logic_rs5_913(self):
		logging.debug("\n-Starting RS5 913 Test Search Logic")
		self.engine.state.RS5_913_SDR_CLS_RT = True
		self.assertTrue(self.engine.state.RS5_913_SDR_CLS_RT, "RS5 913 SWD is not closed.")
		logging.debug("  -Verified that the RS5 913 South Door is closed.")

		# Searcher enters zone.
		logging.debug("  -Searcher entered the RS5 913 and closed the RS5 913 West Door.")
		self.engine.state.RS5_913_WDR_CLS_RT = True
		self.engine.process()
		self.assertFalse(self.engine.state.RS5_SRCH_TMR_ACTV, "RS5 Search Timer active before turning PR1 key.")

		# Searcher turns preset 1 key.
		logging.debug("  -Searcher turns preset 1 key.")
		with self.engine.momentary_press("RS5_913_PR1_KSW_RT"):
			self.assertTrue(self.engine.state.RS5_SRCH_TMR_ACTV, "RS5 Search Timer didn't start after PR1 key turned.")
			self.assertTrue(self.engine.state.RS5_913_PR1_LAT, "RS5 PR1 did not latch after turning key.")
		self.assertTrue(self.engine.state.RS5_913_PR1_LAT, "RS5 PR1 didn't stay latched after releasing PR1 key.")
		logging.debug("  -RS5 913 Preset 1 is Latched.")

		# RS5 913 is a subzone, which does not have a search reset button or keypot.
		# RS5 913 Preserved Set if both RS5_913_PR1 and RS5_913 _PR2 are True.
		self.assertFalse(self.engine.state.RS5_913_PRSVD_SRCH_LAT, "RS5 913 Preserved Set without PR2")

		# Searcher turns preset 2 key.
		logging.debug("  -Searcher turns preset 2 key.")
		with self.engine.momentary_press("RS5_913_PR2_KSW_RT"):
			self.assertTrue(self.engine.state.RS5_913_PR2_LAT, "RS5 PR2 did not latch after turning key.")
		self.assertTrue(self.engine.state.RS5_913_PR2_LAT, "RS5 PR2 did not stay latched after releasing PR2 key.")
		logging.debug("  -RS5 913 Preset 2 is Latched.")

		logging.debug("  -Searcher opens RS5 913 West Door to exit.")
		# Searcher opens gate to exit.
		self.engine.state.RS5_913_WDR_CLS_RT = False
		self.engine.process()
		time.sleep(self.engine.timers.RS5_913_DIB_TMR.duration()/5) #Take some non-zero amount of time to exit
		self.engine.state.RS5_913_WDR_CLS_RT = True #Close gate on the way out
		self.engine.process()
		logging.debug("  -Searcher closed RS5 913 West Door and guard for 15 secs.")

		# Get interlock reset to latch gate
		logging.debug("  -Searcher (controlled) pressing Interlock Reset and Hardware Enable.")
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_ILCK_SET_BTN"]):
			pass
		
		# Get RS5 913 Preserved Search set
		# RS5 913 Preserved Set if both RS5_913_PR1 and RS5_913_PR2 are True.
		self.assertTrue(self.engine.state.RS5_913_PR1_LAT, "RS5 PR1 did not latch.")
		self.assertTrue(self.engine.state.RS5_913_PR2_LAT, "RS5 PR2 did not latch.")
		self.assertTrue(self.engine.state.RS5_913_PRSVD_SRCH_LAT, "RS5 913 Preserved Search not set with all conditions met.")
		logging.debug("  -RS5 913 Preserved Search is Latched.")

	def test_04_gateA_rs5(self):
		gate_door_test(self, 'RS5A_GT_CLS_RT', 'RS5A_GT_CLS_LAT', 'RS5A Gate')
		gate_door_test(self, 'RS5B_GT_CLS_RT', 'RS5B_GT_CLS_LAT', 'RS5B Gate')
		gate_door_test(self, 'RS5C_GT_CLS_RT', 'RS5C_GT_CLS_LAT', 'RS5C Gate')
		gate_door_test(self, 'RS5DE_GT_CLS_RT', 'RS5DE_GT_CLS_LAT', 'RS5D&E Gate')

	def test_05_gate_rs5a_dib(self):
		gate_dib_test(self, gate_rt_name='RS5A_GT_CLS_RT', gate_interlock_name='RS5A_GT_CLS_ILCK', dib_timer_name='RS5_DIB_TMR', 
					dib_active_name='RS5_DIB_ACTIVE', preset_1_name='RS5_PR1_LAT', preset_2_led_name='RS5_PR2_LED', preset_2_ksw_name='RS5_PR2_KSW_RT', 
					gate_list=['RS5B_GT_CLS_RT','RS5C_GT_CLS_RT','RS5DE_GT_CLS_RT'], zone_name='RS5A', prerequisite_search=[self.test_03_search_logic_rs5_913])

	def test_06_search_logic_rs5(self):
		logging.debug("\n-Starting RS5 Test Search Logic")
		logging.debug("  -Ensuring All RS5 Gates are Closed. If not, then let's get close them all!")		
		self.engine.state.RS5B_GT_CLS_RT = True
		self.engine.state.RS5C_GT_CLS_RT = True
		self.engine.state.RS5DE_GT_CLS_RT = True

		logging.debug("  -Ensuring RS5 913 Preserved Search is Latched. If not, then let's get a search!")
		self.test_03_search_logic_rs5_913()

		# Searcher enters zone.
		logging.debug("\n  -Searcher entered the RS5 Gate A and closed the RS5 Gate A.")
		self.engine.state.RS5A_GT_CLS_RT = True
		self.engine.process()
		self.assertFalse(self.engine.state.RS5_SRCH_TMR_ACTV, "RS5 Search Timer active before turning PR1 key.")

		# Searcher turns preset 1 key.
		logging.debug("  -Searcher turns preset 1 key.")
		with self.engine.momentary_press("RS5_PR1_KSW_RT"):
			self.assertTrue(self.engine.state.RS5_SRCH_TMR_ACTV, "RS5 Search Timer didn't start after PR1 key turned.")
			self.assertTrue(self.engine.state.RS5_PR1_LAT, "RS5 PR1 did not latch after turning key.")
		self.assertTrue(self.engine.state.RS5_PR1_LAT, "RS5 PR1 didn't stay latched after releasing PR1 key.")
		logging.debug("  -RS5 Preset 1 is Latched.")

		# Attempt to get search reset now.
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_RS5_SRCH_SET_BTN"]):
			self.assertFalse(self.engine.state.RS5_SRCH_SET_LAT, "RS5 Search Set without both preset 2.")

		# Searcher turns preset 2 key.
		logging.debug("  -Searcher turns preset 2 key.")
		with self.engine.momentary_press("RS5_PR2_KSW_RT"):
			self.assertTrue(self.engine.state.RS5_PR2_LAT, "RS5 PR2 did not latch after turning key.")
		self.assertTrue(self.engine.state.RS5_PR2_LAT, "RS5 PR2 did not stay latched after releasing PR2 key.")
		logging.debug("  -RS5 Preset 2 is Latched.")

		logging.debug("  -Searcher opens RS5 Gate A to exit within 15 secs.")
		# Searcher opens gate to exit.
		self.engine.state.RS5A_GT_CLS_RT = False
		self.engine.process()
		time.sleep(self.engine.timers.RS5_DIB_TMR.duration()/5) #Take some non-zero amount of time to exit
		self.engine.state.RS5A_GT_CLS_RT = True #Close gate on the way out
		self.engine.process()
		logging.debug("  -Searcher closed RS5 Gate A and guard for the remainder DIB timer.")
		# Get interlock reset to latch gate
		logging.debug("  -Searcher (controlled) pressing Interlock Reset and Hardware Enable.")
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_ILCK_SET_BTN"]):
			pass
		self.assertTrue(self.engine.state.RS5A_GT_CLS_ILCK, "RS5 Gate A Closed Interlock is not True after Interlock Reset with Hardware Enable.")

		
		# Get RS5 Search set
		self.assertTrue(self.engine.state.RS5_ALL_GTS_CLS_LAT, "All RS5 gates and door are not closed and latched.")
		self.assertTrue(self.engine.state.RS5_913_PRSVD_SRCH_LAT, "RS5 913 Preserved Search is not latched.")
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_RS5_SRCH_SET_BTN"]):
			with self.engine.momentary_press("RS5_SRCH_SET_KSW_RT"):
				pass
		self.assertTrue(self.engine.state.RS5_SRCH_SET_LAT, "RS5 Search not set with all conditions met.")
		logging.debug("  -RS5 Search is Latched.")
