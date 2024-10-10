import unittest
import time
import logging
from engine import Engine
from timer import Timer
from pulser import Pulser
from generic_test import gate_door_test, gate_dib_test, keybank_test, keybank_release_test, lock_down_mode
import logic

#logging.basicConfig(level=logging.DEBUG)
class RSY_Zone_TestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.logic = [
					logic.rs1_search_timer, logic.rs1_preset_1, logic.rs1_preset_2, logic.rs1_preset_2_led, 
					logic.rs1_gate_closed_interlock, logic.rs1a_gate_closed_latch, logic.rs1_search_set, logic.rs1_search_led,

					logic.rs2_search_timer, logic.rs2_406_preset_1, logic.rs2_406_preset_2, logic.rs2_406_preset_2_led,
					logic.rs2_406_sdoor_closed_interlock, logic.rs2_406_wdr_closed_latch, logic.rs2_406_sdr_closed_latch,
					logic.rs2_406_rudr_closed_latch, logic.rs2_406_doors_closed, logic.rs2_406_preserved_search, 
					logic.rs2_406_preserved_search_led,
					logic.rs2_407_preset_1, logic.rs2_407_preset_2, logic.rs2_407_preset_2_led,
					logic.rs2_407_sdoor_closed_interlock, logic.rs2_407_ndr_closed_latch, logic.rs2_407_edr_closed_latch,
					logic.rs2_407_sdr_closed_latch, logic.rs2_407_all_doors_closed, logic.rs2_407_preserved_search,
					logic.rs2_407_preserved_search_led,
					logic.rs2_preset_1, logic.rs2_preset_2, logic.rs2_preset_2_led,
					logic.rs2a_gate_closed_interlock, logic.rs2a_gate_closed_latch, logic.rs2_all_gates_and_doors_closed,
					logic.rs2_search_set, logic.rs2_search_led,

					logic.rs3_search_timer, logic.rs3_911_preset_1, logic.rs3_911_preset_2, logic.rs3_911_preset_2_led,
					logic.rs3_911_edoor_closed_interlock, logic.rs3_911_edr_closed_latch, logic.rs3_911_preserved_search,
					logic.rs3_911_preserved_search_led,
					logic.rs3_preset_1, logic.rs3_preset_2, logic.rs3_preset_2_led, logic.rs3a_gate_closed_interlock,
					logic.rs3a_gate_closed_latch, logic.rs3b_gate_closed_latch, logic.rs3c_gate_closed_latch,
					logic.rs3_all_gates_closed, logic.rs3_search_set, logic.rs3_all_gates_and_doors_closed,
					logic.rs3_search_led,

					logic.rs4_search_timer, logic.rs4_912_preset_1, logic.rs4_912_preset_2, logic.rs4_912_preset_2_led,
					logic.rs4_912_wdoor_closed_interlock, logic.rs4_912_wdr_closed_latch, logic.rs4_912_preserved_search,
					logic.rs4_912_preserved_search_led,
					logic.rs4_preset_1, logic.rs4_preset_2, logic.rs4_preset_2_led, logic.rs4a_gate_closed_interlock,
					logic.rs4a_gate_closed_latch, logic.rs4b_gate_closed_latch, logic.rs4c_gate_closed_latch,
					logic.rs4_all_gates_closed, logic.rs4_search_set, logic.rs4_all_gates_and_doors_closed,
					logic.rs4_search_led,

					logic.rs5_search_timer, logic.rs5_913_preset_1, logic.rs5_913_preset_2, logic.rs5_913_preset_2_led,
					logic.rs5_913_wdoor_closed_interlock, logic.rs5_913_wdr_closed_latch, logic.rs5_913_sdr_closed_latch,
					logic.rs5_913_all_doors_closed, logic.rs5_913_preserved_search, logic.rs5_913_preserved_search_led,
					logic.rs5_preset_1, logic.rs5_preset_2, logic.rs5_preset_2_led, logic.rs5a_gate_closed_interlock, 
					logic.rs5a_gate_closed_latch, logic.rs5b_gate_closed_latch, logic.rs5c_gate_closed_latch, logic.rs5de_gate_closed_latch,
					logic.rs5_all_gates_closed, logic.rs5_search_set, logic.rs5_all_gates_and_doors_closed,
					logic.rs5_search_led,

					logic.rt1_search_timer, logic.rt1_preset_1, logic.rt1_preset_2, logic.rt1_preset_2_led, 
					logic.rt1_gate_closed_interlock, logic.rt1a_gate_closed_latch, logic.rt1b_gate_closed_latch, logic.rt1_all_gates_closed,logic.rt1_search_set, logic.rt1_search_led,
	
					logic.north_keybank_release, logic.south_keybank_release, logic.north_keybank_complete_latch, logic.south_keybank_complete_latch,
					logic.keybanks_complete_latch, logic.rsy_all_gates_and_doors_closed, logic.interlock_complete, logic.rsy_searched,
					logic.no_access_permitted_access, logic.av_warn, logic.rsy_security_violation, logic.rsy_secure,
					]
	
	def setUp(self):
		rsy_zone_initial_state = logic.RSYState(
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
		rsy_zone_timers = logic.RSYTimers(
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
		self.engine = Engine(rsy_zone_initial_state, self.logic, timers=rsy_zone_timers)
		self.engine.process() #Do one round of initial processing.
		self.items = [
			"RS1_SRCH_SET_LAT",
			"RS1_SRCH_TMR_ACTV",
			"RS1A_GT_CLS_ILCK",
			"RS1_PR1_KSW_RT",
			"RS1_PR1_TESTBTN_RT",
			"PERMITTED_ACCESS",
			"RS1_PR1_LED",
			"RS1_PR1_LAT",
			"RS1_PR2_KSW_RT",
			"RS1_PR2_TESTBTN_RT",
			"RS1_PR2_LAT",
			"RS1_DIB_ACTIVE",
			"RS1A_GT_CLS_RT",
			"RS1_PR2_LED",
			"ACR_HW_EN_RT",
			"EPICS_ILCK_SET_BTN",
			"RS1A_GT_CLS_LAT",
			"RS1_SRCH_SET_KSW_RT",
			"RS1_SRCH_SET_TESTBTN_RT",
			"EPICS_RS1_SRCH_SET_BTN",
			"RS1_SRCH_SET_LED",
			"RS2_406_PR1_KSW_RT",
			"RS2_406_PR1_TESTBTN_RT",
			"RS2_406_PR1_LAT",
			"RS2_406_PR1_LED",
			"RS2_406_PRSVD_SRCH",
			"RS2_SRCH_TMR_ACTV",
			"RS2_406_SDR_CLS_ILCK",
			"RS2_406_WDR_CLS_RT",
			"RS2_406_RUDR_CLS_RT",
			"RS2_406_PR2_LAT",
			"RS2_406_PR2_KSW_RT",
			"RS2_406_PR2_TESTBTN_RT",
			"RS2_406_DIB_ACTIVE",
			"RS2_406_PR2_LED",
			"RS2_406_SDR_CLS_RT",
			"RS2_406_WDR_CLS_LAT",
			"RS2_406_RUDR_CLS_LAT",
			"RS2_406_ALL_DRS_CLS_LAT",
			"RS2_406_PRSVD_SRCH_LED",
			"RS2_407_PR1_LAT",
			"RS2_407_PR1_KSW_RT",
			"RS2_407_PR1_TESTBTN_RT",
			"RS2_407_PRSVD_SRCH",
			"RS2_406_SDR_CLS_LAT",
			"RS2_407_SDR_CLS_ILCK",
			"RS2_407_NDR_CLS_RT",
			"RS2_407_EDR_CLS_RT",
			"RS2_407_PR1_LED",
			"RS2_407_PR2_LAT",
			"RS2_407_PR2_KSW_RT",
			"RS2_407_PR2_TESTBTN_RT",
			"RS2_407_DIB_ACTIVE",
			"RS2_407_PR2_LED",
			"RS2_407_SDR_CLS_RT",
			"RS2_407_NDR_CLS_LAT",
			"RS2_407_SDR_CLS_LAT",
			"RS2_407_EDR_CLS_LAT",
			"RS2_407_ALL_DRS_CLS_LAT",
			"RS2_407_PRSVD_SRCH_LED",
			"RS2_PR1_LAT",
			"RS2_PR1_KSW_RT",
			"RS2_PR1_TESTBTN_RT",
			"RS2_SRCH_SET_LAT",
			"RS2A_GT_CLS_ILCK",
			"RS2_PR1_LED",
			"RS2_PR2_LAT",
			"RS2_PR2_KSW_RT",
			"RS2_PR2_TESTBTN_RT",
			"RS2_DIB_ACTIVE",
			"RS2_PR2_LED",
			"RS2A_GT_CLS_RT",
			"RS2A_GT_CLS_LAT",
			"RS2_ALL_GTS_DRS_CLS_LAT",
			"RS2_SRCH_SET_KSW_RT",
			"RS2_SRCH_SET_TESTBTN_RT",
			"EPICS_RS2_SRCH_SET_BTN",
			"RS2_SRCH_SET_LED",
			"RS3_911_PR1_KSW_RT",
			"RS3_911_PR1_TESTBTN_RT",
			"RS3_911_PR1_LAT",
			"RS3_911_PR1_LED",
			"RS3_911_EDR_CLS_ILCK",
			"RS3_911_PRSVD_SRCH_LAT",
			"RS3_911_PR2_LAT",
			"RS3_911_PR2_KSW_RT",
			"RS3_911_PR2_TESTBTN_RT",
			"RS3_911_PR2_LED",
			"RS3_911_DIB_ACTIVE",
			"RS3_911_EDR_CLS_RT",
			"RS3_911_EDR_CLS_LAT",
			"RS3_911_PRSVD_SRCH_LED",
			"RS3_SRCH_TMR_ACTV",
			"RS3_PR1_LAT",
			"RS3_PR1_LED",
			"RS3_PR1_KSW_RT",
			"RS3_PR1_TESTBTN_RT",
			"RS3_SRCH_SET_LAT",
			"RS3A_GT_CLS_ILCK",
			"RS3B_GT_CLS_RT",
			"RS3C_GT_CLS_RT",
			"RS3_PR2_LAT",
			"RS3_PR2_LED",
			"RS3_DIB_ACTIVE",
			"RS3_PR2_KSW_RT",
			"RS3_PR2_TESTBTN_RT",
			"RS3A_GT_CLS_RT",
			"RS3A_GT_CLS_LAT",
			"RS3B_GT_CLS_LAT",
			"RS3C_GT_CLS_LAT",
			"RS3_ALL_GTS_CLS_LAT",
			"RS3_SRCH_SET_KSW_RT",
			"RS3_SRCH_SET_TESTBTN_RT",
			"EPICS_RS3_SRCH_SET_BTN",
			"RS3_ALL_GTS_DRS_CLS_LAT",
			"RS3_SRCH_SET_LED",
			"RS4_912_PR1_KSW_RT",
			"RS4_912_PR1_TESTBTN_RT",
			"RS4_SRCH_TMR_ACTV",
			"RS4_912_WDR_CLS_ILCK",
			"RS4_912_PR1_LED",
			"RS4_912_PR1_LAT",
			"RS4_912_PR2_KSW_RT",
			"RS4_912_PR2_TESTBTN_RT",
			"RS4_912_PRSVD_SRCH_LAT",
			"RS4_912_PR2_LAT",
			"RS4_PR1_LAT",
			"RS4_PR1_KSW_RT",
			"RS4_PR1_TESTBTN_RT",
			"RS4_SRCH_SET_LAT",
			"RS4_912_DIB_ACTIVE",
			"RS4_912_PR2_LED",
			"RS4_912_WDR_CLS_RT",
			"RS4_912_WDR_CLS_LAT",
			"RS4_912_PRSVD_SRCH_LED",
			"RS4A_GT_CLS_ILCK",
			"RS4B_GT_CLS_RT",
			"RS4C_GT_CLS_RT",
			"RS4_DIB_ACTIVE",
			"RS4_PR2_LAT",
			"RS4_PR2_LED",
			"RS4_PR2_KSW_RT",
			"RS4_PR2_TESTBTN_RT",
			"RS4A_GT_CLS_RT",
			"RS4A_GT_CLS_LAT",
			"RS4B_GT_CLS_LAT",
			"RS4C_GT_CLS_LAT",
			"RS4_ALL_GTS_CLS_LAT",
			"RS4_SRCH_SET_KSW_RT",
			"RS4_SRCH_SET_TESTBTN_RT",
			"EPICS_RS4_SRCH_SET_BTN",
			"RS4_ALL_GTS_DRS_CLS_LAT",
			"RS4_SRCH_SET_LED",
			"RS5_913_PR1_KSW_RT",
			"RS5_913_PR1_TESTBTN_RT",
			"RS5_913_PRSVD_SRCH_LAT",
			"RS5_SRCH_TMR_ACTV",
			"RS5_913_SDR_CLS_RT",
			"RS5_913_SDR_CLS_LAT",
			"RS5_913_WDR_CLS_ILCK",
			"RS5_913_PR1_LED",
			"RS5_913_PR1_LAT",
			"RS5_913_PR2_KSW_RT",
			"RS5_913_PR2_TESTBTN_RT",
			"RS5_913_PR2_LAT",
			"RS5_913_DIB_ACTIVE",
			"RS5_913_PR2_LED",
			"RS5_PR1_LAT",
			"RS5_PR1_KSW_RT",
			"RS5_SRCH_SET_LAT",
			"RS5_913_WDR_CLS_RT",
			"RS5_913_WDR_CLS_LAT",
			"RS5_913_PRSVD_SRCH_LED",
			"EPICS_RS5_SRCH_SET_BTN",
			"RS5_PR1_TESTBTN_RT",
			"RS5A_GT_CLS_ILCK",
			"RS5B_GT_CLS_RT",
			"RS5C_GT_CLS_RT",
			"RS5DE_GT_CLS_RT",
			"RS5_DIB_ACTIVE",
			"RS5_PR2_LAT",
			"RS5_PR2_LED",
			"RS5_PR2_KSW_RT",
			"RS5_PR2_TESTBTN_RT",
			"RS5A_GT_CLS_RT",
			"RS5A_GT_CLS_LAT",
			"RS5B_GT_CLS_LAT",
			"RS5C_GT_CLS_LAT",
			"RS5DE_GT_CLS_LAT",
			"RS5_ALL_GTS_CLS_LAT",
			"RS5_SRCH_SET_KSW_RT",
			"RS5_SRCH_SET_TESTBTN_RT",
			"RS5_ALL_GTS_DRS_CLS_LAT",
			"RS5_SRCH_SET_LED",
			"RS5_913_ALL_DRS_CLS_LAT",
			"RT1_PR1_KSW_RT",
			"RT1_PR1_TESTBTN_RT",
			"RT1_PR2_KSW_RT",
			"RT1_PR2_TESTBTN_RT",
			"RT1_SRCH_SET_KSW_RT",
			"EPICS_RT1_SRCH_SET_BTN", 
			"RT1_PR1_LED",
			"RT1_PR2_LED",
			"RT1_SRCH_SET_LED",
			"RT1_PR1_LAT",
			"RT1_SRCH_SET_LAT",
			"RT1_SRCH_TMR_ACTV",
			"RT1A_GT_CLS_ILCK",
			"RT1B_GT_CLS_RT",
			"RT1_PR2_LAT",
			"RT1_DIB_ACTIVE",
			"RT1A_GT_CLS_RT",
			"RT1A_GT_CLS_LAT",
			"RT1B_GT_CLS_LAT",
			"RT1_ALL_GTS_CLS_LAT",
			"KYBNK_N_CMPLT_LAT",
			"KYBNK_S_CMPLT_LAT",
			"ALL_KYBNK_CMPLT_LAT",
			"RSY_ZN_CLS_LAT",
			"KYBNK_N_COMPLETE_RT",
			"KYBNK_S_COMPLETE_RT",]

	def test_01_keybanks_rsy_zone(self):
		keybank_test(self, 'KYBNK_N_COMPLETE_RT', 'KYBNK_N_CMPLT_LAT', 'North Keybank')
		keybank_test(self, 'KYBNK_S_COMPLETE_RT', 'KYBNK_S_CMPLT_LAT', 'South Keybank')

	def test_02a_n_keybanks_release_rsy_zone(self):
		keybank_release_test(self, 'KYBNK_N_REL_EPICS_BTN', 'KYBNK_N_REL', 'North Keybank')

	def test_02b_s_keybanks_release_rsy_zone(self):
		keybank_release_test(self, 'KYBNK_S_REL_EPICS_BTN', 'KYBNK_S_REL', 'South Keybank')

	def test_03_no_access_and_perm_access(self, perm=True):
		logging.debug("\n-Starting RSY NO_ACCESS Test.")
		real_time = [item for item in self.items if "_CLS_RT" in item or "_COMPLETE_RT" in item or "_CLS_ILCK" in item]
		latch = [item for item in self.items if "_LAT" in item and "RSY_ZN_CLS_LAT" not in item]
		for item in real_time:
			setattr(self.engine.state, item, True)
			self.assertTrue(getattr(self.engine.state, item), f"{item} is not closed.")
		for item in latch:
			setattr(self.engine.state, item, True)
			self.assertTrue(getattr(self.engine.state, item), f"{item} is not latched.")
		self.engine.process()

		for item in latch:
			self.assertTrue(getattr(self.engine.state, item), f"{item} is not latched.")

		self.assertFalse(getattr(self.engine.state, 'NO_ACCESS'), f"NO_ACCESS is set.")
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_NO_ACCESS_BTN"]):
			pass
		self.assertTrue(getattr(self.engine.state, 'NO_ACCESS'), f"NO_ACCESS is not set.")
		self.assertFalse(getattr(self.engine.state, 'PERMITTED_ACCESS'), f"PERMITTED_ACCESS is set.")
		self.engine.process()
		logging.debug("  -RSY is in NO_ACCESS.")
		self.assertTrue(getattr(self.engine.state, 'AV_WARN'), f"AV_WARN is on.")
		while (time.time() - getattr(self.engine.timers, 'AV_WARN_TMR').time_started()) < getattr(self.engine.timers, 'AV_WARN_TMR').duration():
			self.engine.process()
			#print((time.time() - getattr(self.engine.timers, 'AV_WARN_TMR').time_started()),"<", getattr(self.engine.timers, 'AV_WARN_TMR').duration())
			time.sleep(getattr(self.engine.timers, 'AV_WARN_TMR').duration() / 10)

		self.engine.process()
		self.assertFalse(getattr(self.engine.state, 'AV_WARN'), f"AV_WARN is not done playing.")
		self.assertTrue(getattr(self.engine.state, 'AV_WARN_CMPLT'), f"AV_WARN is not done playing.")
		self.assertTrue(getattr(self.engine.state, 'ILCKS_CMPLT'), f"ILCKS_CMPLT is not set.")
		self.assertTrue(getattr(self.engine.state, 'RSY_SRCHD'), f"RSY_SRCHD is not set.")
		self.assertTrue(getattr(self.engine.state, 'NO_ACCESS'), f"NO_ACCESS is not set.")

		self.assertTrue(getattr(self.engine.state, 'RSY_SECURE'), f"RSY_SECURE is not secure.")
		self.assertFalse(getattr(self.engine.state, 'RSY_SECURITY_VIOLATION'), f"RSY_SECURITY_VIOLATION is set.")

		if perm:
			logging.debug("\n-Starting RSY PERMITTED_ACCESS Test.")
			with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_PERMITTED_ACCESS_BTN"]):
				pass
			self.assertFalse(getattr(self.engine.state, 'NO_ACCESS'), f"NO_ACCESS is set.")
			self.assertTrue(getattr(self.engine.state, 'PERMITTED_ACCESS'), f"PERMITTED_ACCESS is not set.")
			self.engine.process()	
			self.assertFalse(getattr(self.engine.state, 'RSY_SECURE'), f"RSY_SECURE is set.")
			self.assertFalse(getattr(self.engine.state, 'RSY_SECURITY_VIOLATION'), f"RSY_SECURITY_VIOLATION is set.")
			logging.debug("  -RSY is in PERMITTED_ACCESS.")

	def test_04_rsy_sec_violation(self, perm=True):
		self.test_03_no_access_and_perm_access(perm=False)
		logging.debug("\n-Starting RSY Security Violation Test.")
		self.engine.state.RS3_911_EDR_CLS_RT = False
		logging.debug(" -Tester opened the RS3_911_EDR_CLS_RT.")
		self.engine.process()
		self.assertTrue(self.engine.state.NO_ACCESS, "NO_ACCESS is False.")
		self.assertFalse(self.engine.state.RS3_911_EDR_CLS_LAT, "RS3A_GT_CRS3_911_EDR_CLS_LATLS_LAT is still Latched.")
		logging.debug(" -Lost the RS3_911_EDR_CLS_LAT.")
		self.assertFalse(self.engine.state.RS3_ALL_GTS_DRS_CLS_LAT, "RS3_ALL_GTS_DRS_CLS_LAT is still Latched.")
		self.engine.process()
		self.assertFalse(self.engine.state.RS3_911_PRSVD_SRCH_LAT, "RS3_911_PRSVD_SRCH_LAT is still Latched.")
		logging.debug(" -Lost the RS3_911_PRSVD_SRCH_LAT.")
		self.assertFalse(self.engine.state.RSY_SRCHD, "RSY_SRCHD is still intact.")
		logging.debug(" -Lost the RSY_SRCHD.")
		self.assertTrue(self.engine.state.ALL_KYBNK_CMPLT_LAT, "ALL_KYBNK_CMPLT_LAT is not Latched.")
		self.assertFalse(self.engine.state.RSY_ZN_CLS_LAT, "RSY_ZN_CLS_LAT is still completed.")
		self.assertFalse(self.engine.state.ILCKS_CMPLT, "ILCKS_CMPLT is still completed.")
		self.assertTrue(self.engine.state.RSY_SECURITY_VIOLATION, "RSY_SECURITY_VIOLATION is not violated.")
		logging.debug(" -RSY_SECURITY_VIOLATION is violated.")
		self.assertFalse(self.engine.state.RSY_SECURE, "RSY_SECURE is still completed.")
		self.assertTrue(self.engine.state.NO_ACCESS, "NO_ACCESS is False.")
		logging.debug(" -Lost RSY_SECURE and still in NO_ACCESS.")		