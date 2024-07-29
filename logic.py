from dataclasses import dataclass, replace
from pulser import Pulser
from timer import Timer
import logging

@dataclass
class RSYState:
	"""The state of the RSY PPS - all input/output bits from the PLC"""
	#External Inputs (gates, doors, buttons, etc.)
	##Global
	ACR_HW_EN_RT: bool
	EPICS_ILCK_SET_BTN: bool
	##RS1
	RS1_PR1_KSW_RT: bool
	RS1_PR1_TESTBTN_RT: bool
	RS1_PR2_KSW_RT: bool
	RS1_PR2_TESTBTN_RT: bool
	RS1A_GT_CLS_RT: bool
	RS1_SRCH_SET_KSW_RT: bool
	RS1_SRCH_SET_TESTBTN_RT: bool
	EPICS_RS1_SRCH_SET_BTN: bool

	##RT1
	RT1_PR1_KSW_RT: bool
	RT1_PR1_TESTBTN_RT: bool
	RT1_PR2_KSW_RT: bool
	RT1_PR2_TESTBTN_RT: bool
	RT1_SRCH_SET_KSW_RT: bool
	EPICS_RT1_SRCH_SET_BTN: bool 

	#Outputs
	##RS1
	RS1_PR1_LED: bool
	RS1_PR2_LED: bool
	RS1_SRCH_SET_LED: bool

	##RT1
	RT1_PR1_LED: bool
	RT1_PR2_LED: bool
	RT1_SRCH_SET_LED: bool

	#Internal Bits
	##Global
	PERMITTED_ACCESS: bool

	##RS1
	RS1_SRCH_SET_LAT: bool
	RS1_SRCH_TMR_ACTV: bool
	RS1A_GT_CLS_ILCK: bool
	RS1_PR1_LAT: bool
	RS1_PR2_LAT: bool
	RS1_DIB_ACTIVE: bool
	RS1A_GT_CLS_LAT: bool

	##RS3 911
	RS3_911_PR1_KSW_RT: bool
	RS3_911_PR1_TESTBTN_RT: bool
	RS3_911_PR1_LAT: bool
	RS3_911_PR1_LED: bool
	RS3_911_EDR_CLS_ILCK: bool
	RS3_911_PRSVD_SRCH_LAT: bool
	RS3_911_PR2_LAT: bool
	RS3_911_PR2_KSW_RT: bool
	RS3_911_PR2_TESTBTN_RT: bool
	RS3_911_PR2_LED: bool
	RS3_911_DIB_ACTIVE: bool
	RS3_911_EDR_CLS_RT: bool
	RS3_911_EDR_CLS_LAT: bool
	RS3_911_PRSVD_SRCH_LED: bool
	RS3_SRCH_TMR_ACTV: bool
	RS3_PR1_LAT: bool
	RS3_PR1_LED: bool
	RS3_PR1_KSW_RT: bool
	RS3_PR1_TESTBTN_RT: bool
	RS3_SRCH_SET_LAT: bool
	RS3A_GT_CLS_ILCK: bool
	RS3B_GT_CLS_RT: bool
	RS3C_GT_CLS_RT: bool
	RS3_PR2_LAT: bool
	RS3_PR2_KSW_RT: bool
	RS3_PR2_TESTBTN_RT: bool
	RS3_PR2_LED: bool
	RS3_DIB_ACTIVE: bool
	RS3A_GT_CLS_RT: bool
	RS3A_GT_CLS_LAT: bool
	RS3B_GT_CLS_LAT: bool
	RS3C_GT_CLS_LAT: bool
	RS3_ALL_GTS_CLS_LAT: bool
	RS3_SRCH_SET_KSW_RT: bool
	RS3_SRCH_SET_TESTBTN_RT: bool
	EPICS_RS3_SRCH_SET_BTN: bool
	RS3_ALL_GTS_DRS_CLS_LAT: bool
	RS3_SRCH_SET_LED: bool

	##RS4_912
	RS4_912_PR1_KSW_RT: bool
	RS4_912_PR1_TESTBTN_RT: bool
	RS4_SRCH_TMR_ACTV: bool
	RS4_912_WDR_CLS_ILCK: bool
	RS4_912_PR1_LED: bool
	RS4_912_PR1_LAT: bool
	RS4_912_PR2_KSW_RT: bool
	RS4_912_PR2_TESTBTN_RT: bool
	RS4_912_PRSVD_SRCH_LAT: bool
	RS4_912_PR2_LAT: bool	
	RS4_PR1_LAT: bool
	RS4_PR1_KSW_RT: bool
	RS4_PR1_TESTBTN_RT: bool
	RS4_912_DIB_ACTIVE: bool
	RS4_912_PR2_LED: bool
	RS4_912_WDR_CLS_RT: bool
	RS4_912_WDR_CLS_LAT: bool
	RS4_912_PRSVD_SRCH_LED: bool
	RS4_SRCH_SET_LAT: bool
	RS4_SRCH_TMR_ACTV: bool
	RS4A_GT_CLS_ILCK: bool
	RS4B_GT_CLS_RT: bool
	RS4C_GT_CLS_RT: bool
	RS4_DIB_ACTIVE: bool
	RS4_PR2_LAT: bool
	RS4_PR2_LED: bool
	RS4_PR2_KSW_RT: bool
	RS4_PR2_TESTBTN_RT: bool
	RS4A_GT_CLS_RT: bool
	RS4A_GT_CLS_LAT: bool
	RS4B_GT_CLS_LAT: bool
	RS4C_GT_CLS_LAT: bool
	RS4_ALL_GTS_CLS_LAT: bool
	RS4_SRCH_SET_KSW_RT: bool
	RS4_SRCH_SET_TESTBTN_RT: bool
	EPICS_RS4_SRCH_SET_BTN: bool
	RS4_ALL_GTS_DRS_CLS_LAT: bool
	RS4_SRCH_SET_LED: bool

	##RS5_913
	RS5_913_PR1_KSW_RT: bool
	RS5_913_PR1_TESTBTN_RT: bool
	RS5_913_PRSVD_SRCH_LAT: bool
	RS5_SRCH_TMR_ACTV: bool
	RS5_913_SDR_CLS_RT: bool
	RS5_913_WDR_CLS_ILCK: bool
	RS5_913_PR1_LED: bool
	RS5_913_PR1_LAT: bool
	RS5_913_PR2_KSW_RT: bool
	RS5_913_PR2_TESTBTN_RT: bool
	RS5_913_SDR_CLS_LAT: bool
	RS5_913_PR2_LAT: bool
	RS5_913_DIB_ACTIVE: bool
	RS5_913_PR2_LED: bool
	RS5_PR1_LAT: bool
	RS5_PR1_KSW_RT: bool
	RS5_SRCH_SET_LAT: bool
	RS5_913_WDR_CLS_RT: bool
	RS5_913_WDR_CLS_LAT: bool
	RS5_913_PRSVD_SRCH_LED: bool
	EPICS_RS5_SRCH_SET_BTN: bool
	RS5_PR1_TESTBTN_RT: bool
	RS5A_GT_CLS_ILCK: bool
	RS5B_GT_CLS_RT: bool
	RS5C_GT_CLS_RT: bool
	RS5DE_GT_CLS_RT: bool
	RS5_DIB_ACTIVE: bool
	RS5_PR2_LAT: bool
	RS5_PR2_LED: bool
	RS5_PR2_KSW_RT: bool
	RS5_PR2_TESTBTN_RT: bool
	RS5A_GT_CLS_RT: bool
	RS5A_GT_CLS_LAT: bool
	RS5B_GT_CLS_LAT: bool
	RS5C_GT_CLS_LAT: bool
	RS5DE_GT_CLS_LAT: bool
	RS5_ALL_GTS_CLS_LAT: bool
	RS5_SRCH_SET_KSW_RT: bool
	RS5_SRCH_SET_TESTBTN_RT: bool
	RS5_ALL_GTS_DRS_CLS_LAT: bool
	RS5_SRCH_SET_LED: bool
	RS5_913_ALL_DRS_CLS_LAT: bool

	##RT1
	RT1_PR1_LAT: bool
	RT1_SRCH_SET_LAT: bool
	RT1_SRCH_TMR_ACTV: bool
	RT1A_GT_CLS_ILCK: bool
	RT1B_GT_CLS_RT: bool
	RT1_PR2_LAT: bool
	RT1_DIB_ACTIVE: bool
	RT1A_GT_CLS_RT: bool
	RT1A_GT_CLS_LAT: bool
	RT1B_GT_CLS_LAT: bool
	RT1_ALL_GTS_CLS_LAT: bool
	
	##RS2 406, 407
	RS2_406_PR1_KSW_RT: bool
	RS2_406_PR1_TESTBTN_RT: bool
	RS2_406_PR1_LAT: bool
	RS2_406_PR1_LED: bool
	RS2_406_PRSVD_SRCH: bool
	RS2_SRCH_TMR_ACTV: bool
	RS2_406_SDR_CLS_ILCK: bool
	RS2_406_WDR_CLS_RT: bool
	RS2_406_RUDR_CLS_RT: bool
	RS2_406_PR2_LAT: bool
	RS2_406_PR2_KSW_RT: bool
	RS2_406_PR2_TESTBTN_RT: bool
	RS2_406_DIB_ACTIVE: bool
	RS2_406_PR2_LED: bool
	RS2_406_SDR_CLS_RT: bool
	RS2_406_WDR_CLS_LAT: bool
	RS2_406_WDR_CLS_RT: bool
	RS2_406_RUDR_CLS_LAT: bool
	RS2_406_ALL_DRS_CLS_LAT: bool
	RS2_406_PRSVD_SRCH_LED: bool

	RS2_407_PR1_LAT: bool
	RS2_407_PR1_KSW_RT: bool
	RS2_407_PR1_TESTBTN_RT: bool
	RS2_407_PRSVD_SRCH: bool
	RS2_406_SDR_CLS_LAT: bool
	RS2_407_SDR_CLS_ILCK: bool
	RS2_407_NDR_CLS_RT: bool
	RS2_407_EDR_CLS_RT: bool
	RS2_407_PR1_LED: bool
	RS2_407_PR2_LAT: bool
	RS2_407_PR2_KSW_RT: bool
	RS2_407_PR2_TESTBTN_RT: bool
	RS2_407_DIB_ACTIVE: bool
	RS2_407_PR2_LED: bool
	RS2_407_SDR_CLS_RT: bool
	RS2_407_NDR_CLS_LAT: bool
	RS2_407_SDR_CLS_LAT: bool
	RS2_407_EDR_CLS_LAT: bool
	RS2_407_ALL_DRS_CLS_LAT: bool
	RS2_407_PRSVD_SRCH_LED: bool

	RS2_PR1_LAT: bool
	RS2_PR1_KSW_RT: bool
	RS2_PR1_TESTBTN_RT: bool
	RS2_SRCH_SET_LAT: bool
	RS2A_GT_CLS_ILCK: bool
	RS2_PR1_LED: bool
	RS2_PR2_LAT: bool
	RS2_PR2_KSW_RT: bool
	RS2_PR2_TESTBTN_RT: bool
	RS2_DIB_ACTIVE: bool
	RS2_PR2_LED: bool
	RS2A_GT_CLS_RT: bool
	RS2A_GT_CLS_LAT: bool
	RS2_ALL_GTS_DRS_CLS_LAT: bool
	RS2_SRCH_SET_KSW_RT: bool
	RS2_SRCH_SET_TESTBTN_RT: bool
	EPICS_RS2_SRCH_SET_BTN: bool
	RS2_SRCH_SET_LED: bool

	def copy(self):
		return replace(self)

@dataclass
class RSYTimers:
	RS1_SRCH_TMR: Timer
	RS1_DIB_TMR: Timer
	RS1_DIB_PULSER: Pulser
	RS1_SEARCH_LED_PULSER: Pulser

	RS2_SRCH_TMR: Timer
	RS2_406_DIB_TMR: Timer
	RS2_406_DIB_PULSER: Pulser
	RS2_406_SEARCH_LED_PULSER: Pulser

	RS2_407_DIB_TMR: Timer
	RS2_407_DIB_PULSER: Pulser
	RS2_407_SEARCH_LED_PULSER: Pulser

	RS2_DIB_TMR: Timer
	RS2_DIB_PULSER: Pulser
	RS2_SEARCH_LED_PULSER: Pulser

	RS3_SRCH_TMR: Timer
	RS3_911_DIB_TMR: Timer
	RS3_911_DIB_PULSER: Pulser
	RS3_911_SEARCH_LED_PULSER: Pulser

	RS3_DIB_TMR: Timer
	RS3_DIB_PULSER: Pulser
	RS3_SEARCH_LED_PULSER: Pulser

	RS4_SRCH_TMR: Timer
	RS4_912_DIB_TMR: Timer
	RS4_912_DIB_PULSER: Pulser
	RS4_912_SEARCH_LED_PULSER: Pulser

	RS4_DIB_TMR: Timer
	RS4_DIB_PULSER: Pulser
	RS4_SEARCH_LED_PULSER: Pulser

	RS5_SRCH_TMR: Timer
	RS5_913_DIB_TMR: Timer
	RS5_913_DIB_PULSER: Pulser
	RS5_913_SEARCH_LED_PULSER: Pulser

	RS5_DIB_TMR: Timer
	RS5_DIB_PULSER: Pulser
	RS5_SEARCH_LED_PULSER: Pulser

	RT1_SRCH_TMR: Timer
	RT1_DIB_TMR: Timer
	RT1_DIB_PULSER: Pulser
	RT1_SEARCH_LED_PULSER: Pulser

def rising(state, prev_state, key):
	return getattr(prev_state,key) == False and getattr(state,key) == True

def falling(state, prev_state, key):
	return getattr(prev_state,key) == True and getattr(state,key) == False

#____

def rs1_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS1_PR1_KSW_RT') or rising(state, prev_state, 'RS1_PR1_TESTBTN_RT')
	new_state.RS1_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS1_PR1_LAT) and state.RS1A_GT_CLS_ILCK and (state.RS1_SRCH_SET_LAT or state.RS1_SRCH_TMR_ACTV)
	new_state.RS1_PR1_LED = new_state.RS1_PR1_LAT
	return new_state

def rs1_search_timer(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start = (state.RS1_PR1_TESTBTN_RT or state.RS1_PR1_KSW_RT or state.RS1_PR1_LAT) and (not state.RS1_SRCH_SET_LAT)
	if timer_start:
		logging.debug("   -Starting RS1_SRCH_TMR")
		timers.RS1_SRCH_TMR.start()
	new_state.RS1_SRCH_TMR_ACTV = timer_start and (not timers.RS1_SRCH_TMR.done())
	return new_state
	
def rs1_search_timer_PATCHED(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start = (state.RS1_PR1_TESTBTN_RT or state.RS1_PR1_KSW_RT or state.RS1_PR1_LAT) and (not state.RS1_SRCH_SET_LAT)
	if not timer_start:
		timers.RS1_SRCH_TMR.stop()
	if timer_start and not timers.RS1_SRCH_TMR.running():
		logging.debug("Starting RS1_SRCH_TMR")
		timers.RS1_SRCH_TMR.start()
	new_state.RS1_SRCH_TMR_ACTV = timer_start and (not timers.RS1_SRCH_TMR.done())
	return new_state

def rs1_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS1_PR2_LAT = (((rising(state, prev_state, 'RS1_PR2_KSW_RT') or rising(state, prev_state, 'RS1_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS1_PR2_LAT) and state.RS1A_GT_CLS_ILCK and state.RS1_PR1_LAT and (state.RS1_SRCH_SET_LAT or state.RS1_SRCH_TMR_ACTV)
	return new_state

def rs1_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS1_DIB_ACTIVE and not timers.RS1_DIB_PULSER.running():
		timers.RS1_DIB_PULSER.start()
	elif not state.RS1_DIB_ACTIVE:
		timers.RS1_DIB_PULSER.stop()
	new_state.RS1_PR2_LED = state.RS1_DIB_ACTIVE and (not bool(timers.RS1_DIB_PULSER)) and state.RS1_PR2_LAT
	return new_state

def rs1_gate_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS1_PR1_LAT and rising(state, prev_state, 'RS1_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS1A_GT_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS1_DIB_TMR")
		timers.RS1_DIB_TMR.start()
	new_state.RS1_DIB_ACTIVE = bool(timers.RS1_DIB_TMR)
	new_state.RS1A_GT_CLS_ILCK = bool(timers.RS1_DIB_TMR) or state.RS1A_GT_CLS_RT
	return new_state
	
def rs1a_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS1A_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS1A_GT_CLS_LAT) and state.RS1A_GT_CLS_RT
	return new_state

def rs1_search_set(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	search_request = (state.RS1_SRCH_SET_KSW_RT or state.RS1_SRCH_SET_TESTBTN_RT) and state.ACR_HW_EN_RT and state.EPICS_RS1_SRCH_SET_BTN and state.RS1_SRCH_TMR_ACTV
	new_state.RS1_SRCH_SET_LAT = (search_request or state.RS1_SRCH_SET_LAT) and state.RS1A_GT_CLS_LAT and state.RS1_PR1_LAT and state.RS1_PR2_LAT
	return new_state
	
def rs1_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS1_SRCH_SET_LED = state.RS1_DIB_ACTIVE and bool(timers.RS1_SEARCH_LED_PULSER) and state.RS1_SRCH_SET_LAT
	return new_state

#____

def rs2_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS2_PR1_KSW_RT') or rising(state, prev_state, 'RS2_PR1_TESTBTN_RT')
	new_state.RS2_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS2_PR1_LAT) and state.RS2A_GT_CLS_ILCK and state.RS2_407_PRSVD_SRCH and state.RS2_406_PRSVD_SRCH and (state.RS2_SRCH_SET_LAT or state.RS2_SRCH_TMR_ACTV)
	new_state.RS2_PR1_LED = new_state.RS2_PR1_LAT
	return new_state

def rs2_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_PR2_LAT = (((rising(state, prev_state, 'RS2_PR2_KSW_RT') or rising(state, prev_state, 'RS2_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS2_PR2_LAT) and (state.RS2_SRCH_SET_LAT or state.RS2_SRCH_TMR_ACTV) and state.RS2A_GT_CLS_ILCK and state.RS2_PR1_LAT
	return new_state

def rs2_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS2_DIB_ACTIVE and not timers.RS2_DIB_PULSER.running():
		timers.RS2_DIB_PULSER.start()
	elif not state.RS2_DIB_ACTIVE:
		timers.RS2_DIB_PULSER.stop()
	new_state.RS2_PR2_LED = state.RS2_DIB_ACTIVE and (not bool(timers.RS2_DIB_PULSER)) and state.RS2_PR2_LAT
	return new_state

def rs2a_gate_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS2_PR1_LAT and rising(state, prev_state, 'RS2_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS2A_GT_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS2_DIB_TMR")
		timers.RS2_DIB_TMR.start()
	new_state.RS2_DIB_ACTIVE = bool(timers.RS2_DIB_TMR)
	new_state.RS2A_GT_CLS_ILCK = bool(timers.RS2_DIB_TMR) or state.RS2A_GT_CLS_RT
	return new_state

def rs2a_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2A_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS2A_GT_CLS_LAT) and state.RS2A_GT_CLS_RT
	return new_state

def rs2_all_gates_and_doors_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_ALL_GTS_DRS_CLS_LAT = state.RS2_406_ALL_DRS_CLS_LAT and state.RS2_407_ALL_DRS_CLS_LAT and state.RS2A_GT_CLS_LAT
	return new_state

def rs2_search_set(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	search_request = (state.RS2_SRCH_SET_KSW_RT or state.RS2_SRCH_SET_TESTBTN_RT) and state.ACR_HW_EN_RT and state.EPICS_RS2_SRCH_SET_BTN and state.RS2_SRCH_TMR_ACTV
	new_state.RS2_SRCH_SET_LAT = (search_request or state.RS2_SRCH_SET_LAT) and state.RS2A_GT_CLS_LAT and state.RS2_PR1_LAT and state.RS2_PR2_LAT
	return new_state

def rs2_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_SRCH_SET_LED = state.RS2_DIB_ACTIVE and bool(timers.RS2_SEARCH_LED_PULSER) and state.RS2_SRCH_SET_LAT
	return new_state

#____

def rs2_406_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS2_406_PR1_KSW_RT') or rising(state, prev_state, 'RS2_406_PR1_TESTBTN_RT')
	new_state.RS2_406_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS2_406_PR1_LAT) and state.RS2_406_SDR_CLS_ILCK and state.RS2_406_WDR_CLS_RT and state.RS2_406_RUDR_CLS_RT and (state.RS2_406_PRSVD_SRCH or state.RS2_SRCH_TMR_ACTV)
	new_state.RS2_406_PR1_LED = new_state.RS2_406_PR1_LAT
	return new_state

def rs2_search_timer(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start_rs2_406 = (state.RS2_406_PR1_LAT or state.RS2_406_PR1_KSW_RT or state.RS2_406_PR1_TESTBTN_RT) and (not state.RS2_406_PRSVD_SRCH)
	timer_start_rs2_407 = (state.RS2_407_PR1_LAT or state.RS2_407_PR1_KSW_RT or state.RS2_407_PR1_TESTBTN_RT) and (not state.RS2_407_PRSVD_SRCH)
	timer_start_rs2 = (state.RS2_PR1_LAT or state.RS2_PR1_KSW_RT or state.RS2_PR1_TESTBTN_RT) and state.RS2_406_PRSVD_SRCH and state.RS2_407_PRSVD_SRCH and (not state.RS2_SRCH_SET_LAT)
	result = None
	if timer_start_rs2_406:
		timers.RS2_SRCH_TMR.start()
		logging.debug("   -Starting RS2_SRCH_TMR for RS2_406")
		result = timer_start_rs2_406 and (not timers.RS2_SRCH_TMR.done())
	elif timer_start_rs2_407:
		timers.RS2_SRCH_TMR.start()
		logging.debug("   -Starting RS2_SRCH_TMR for RS2_407")
		result = timer_start_rs2_407 and (not timers.RS2_SRCH_TMR.done())
	elif timer_start_rs2:
		timers.RS2_SRCH_TMR.start()
		logging.debug("   -Starting RS2_SRCH_TMR for RS2")
		result = timer_start_rs2 and (not timers.RS2_SRCH_TMR.done())	  
	new_state.RS2_SRCH_TMR_ACTV = result
	return new_state

def rs2_406_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_406_PR2_LAT = (((rising(state, prev_state, 'RS2_406_PR2_KSW_RT') or rising(state, prev_state, 'RS2_406_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS2_406_PR2_LAT) and state.RS2_406_PR1_LAT and state.RS2_406_SDR_CLS_ILCK and state.RS2_406_WDR_CLS_RT and state.RS2_406_RUDR_CLS_RT and (state.RS2_406_PRSVD_SRCH or state.RS2_SRCH_TMR_ACTV)
	return new_state

def rs2_406_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS2_406_DIB_ACTIVE and not timers.RS2_406_DIB_PULSER.running():
		timers.RS2_406_DIB_PULSER.start()
	elif not state.RS2_406_DIB_ACTIVE:
		timers.RS2_406_DIB_PULSER.stop()
	new_state.RS2_406_PR2_LED = state.RS2_406_DIB_ACTIVE and (not bool(timers.RS2_406_DIB_PULSER)) and state.RS2_406_PR2_LAT
	return new_state

def rs2_406_sdoor_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS2_406_PR1_LAT and rising(state, prev_state, 'RS2_406_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS2_406_SDR_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS2_406_DIB_TMR")
		timers.RS2_406_DIB_TMR.start()
	new_state.RS2_406_DIB_ACTIVE = bool(timers.RS2_406_DIB_TMR)
	new_state.RS2_406_SDR_CLS_ILCK = bool(timers.RS2_406_DIB_TMR) or state.RS2_406_SDR_CLS_RT
	return new_state

def rs2_406_wdr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_406_WDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS2_406_WDR_CLS_LAT) and state.RS2_406_WDR_CLS_RT
	return new_state

def rs2_406_sdr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_406_SDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS2_406_SDR_CLS_LAT) and state.RS2_406_SDR_CLS_RT
	return new_state

def rs2_406_rudr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_406_RUDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS2_406_RUDR_CLS_LAT) and state.RS2_406_RUDR_CLS_RT
	return new_state

def rs2_406_doors_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_406_ALL_DRS_CLS_LAT = state.RS2_406_WDR_CLS_LAT and state.RS2_406_SDR_CLS_LAT and state.RS2_406_RUDR_CLS_LAT
	return new_state

def rs2_406_preserved_search(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_406_PRSVD_SRCH = state.RS2_406_PR1_LAT and state.RS2_406_PR2_LAT
	return new_state

def rs2_406_preserved_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_406_PRSVD_SRCH_LED = state.RS2_406_DIB_ACTIVE and bool(timers.RS2_406_SEARCH_LED_PULSER) and state.RS2_406_PRSVD_SRCH
	return new_state	

#____

def rs2_407_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS2_407_PR1_KSW_RT') or rising(state, prev_state, 'RS2_407_PR1_TESTBTN_RT')
	new_state.RS2_407_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS2_407_PR1_LAT) and state.RS2_407_SDR_CLS_ILCK and state.RS2_407_NDR_CLS_RT and state.RS2_407_EDR_CLS_RT and (state.RS2_407_PRSVD_SRCH or state.RS2_SRCH_TMR_ACTV)
	new_state.RS2_407_PR1_LED = new_state.RS2_407_PR1_LAT
	return new_state

def rs2_407_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_407_PR2_LAT = (((rising(state, prev_state, 'RS2_407_PR2_KSW_RT') or rising(state, prev_state, 'RS2_407_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS2_407_PR2_LAT) and state.RS2_407_PR1_LAT and state.RS2_407_SDR_CLS_ILCK and state.RS2_407_NDR_CLS_RT and state.RS2_407_EDR_CLS_RT and (state.RS2_407_PRSVD_SRCH or state.RS2_SRCH_TMR_ACTV)
	return new_state

def rs2_407_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS2_407_DIB_ACTIVE and not timers.RS2_407_DIB_PULSER.running():
		timers.RS2_407_DIB_PULSER.start()
	elif not state.RS2_407_DIB_ACTIVE:
		timers.RS2_407_DIB_PULSER.stop()
	new_state.RS2_407_PR2_LED = state.RS2_407_DIB_ACTIVE and (not bool(timers.RS2_407_DIB_PULSER)) and state.RS2_407_PR2_LAT
	return new_state

def rs2_407_sdoor_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS2_407_PR1_LAT and rising(state, prev_state, 'RS2_407_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS2_407_SDR_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS2_407_DIB_TMR")
		timers.RS2_407_DIB_TMR.start()
	new_state.RS2_407_DIB_ACTIVE = bool(timers.RS2_407_DIB_TMR)
	new_state.RS2_407_SDR_CLS_ILCK = bool(timers.RS2_407_DIB_TMR) or state.RS2_407_SDR_CLS_RT
	return new_state

def rs2_407_ndr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_407_NDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS2_407_NDR_CLS_LAT) and state.RS2_407_NDR_CLS_RT
	return new_state

def rs2_407_edr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_407_EDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS2_407_EDR_CLS_LAT) and state.RS2_407_EDR_CLS_RT
	return new_state

def rs2_407_sdr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_407_SDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS2_407_SDR_CLS_LAT) and state.RS2_407_SDR_CLS_RT
	return new_state

def rs2_407_all_doors_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_407_ALL_DRS_CLS_LAT = state.RS2_407_NDR_CLS_LAT and state.RS2_407_EDR_CLS_LAT and state.RS2_407_SDR_CLS_LAT
	return new_state

def rs2_407_preserved_search(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_407_PRSVD_SRCH = state.RS2_407_PR1_LAT and state.RS2_407_PR2_LAT
	return new_state

def rs2_407_preserved_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS2_407_PRSVD_SRCH_LED = state.RS2_407_DIB_ACTIVE and bool(timers.RS2_407_SEARCH_LED_PULSER) and state.RS2_407_PRSVD_SRCH
	return new_state

#____

def rs3_911_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS3_911_PR1_KSW_RT') or rising(state, prev_state, 'RS3_911_PR1_TESTBTN_RT')
	new_state.RS3_911_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS3_911_PR1_LAT) and state.RS3_911_EDR_CLS_ILCK and (state.RS3_911_PRSVD_SRCH_LAT or state.RS3_SRCH_TMR_ACTV)
	new_state.RS3_911_PR1_LED = new_state.RS3_911_PR1_LAT
	return new_state

def rs3_search_timer(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start_rs3_911 = (state.RS3_911_PR1_LAT or state.RS3_911_PR1_KSW_RT or state.RS3_911_PR1_TESTBTN_RT) and (not state.RS3_911_PRSVD_SRCH_LAT)
	timer_start_rs3 = (state.RS3_PR1_LAT or state.RS3_PR1_KSW_RT or state.RS3_PR1_TESTBTN_RT) and state.RS3_911_PRSVD_SRCH_LAT and (not state.RS3_SRCH_SET_LAT)
	result = None
	if timer_start_rs3_911:
		timers.RS3_SRCH_TMR.start()
		logging.debug("   -Starting RS3_SRCH_TMR for RS3_911")
		result = timer_start_rs3_911 and (not timers.RS3_SRCH_TMR.done())
	elif timer_start_rs3:
		timers.RS3_SRCH_TMR.start()
		logging.debug("   -Starting RS3_SRCH_TMR for RS3")
		result = timer_start_rs3 and (not timers.RS3_SRCH_TMR.done())	  
	new_state.RS3_SRCH_TMR_ACTV = result
	return new_state

def rs3_911_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_911_PR2_LAT = (((rising(state, prev_state, 'RS3_911_PR2_KSW_RT') or rising(state, prev_state, 'RS3_911_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS3_911_PR2_LAT) and state.RS3_911_EDR_CLS_ILCK and state.RS3_911_PR1_LAT and (state.RS3_911_PRSVD_SRCH_LAT or state.RS3_SRCH_TMR_ACTV)
	return new_state

def rs3_911_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS3_911_DIB_ACTIVE and not timers.RS3_911_DIB_PULSER.running():
		timers.RS3_911_DIB_PULSER.start()
	elif not state.RS3_911_DIB_ACTIVE:
		timers.RS3_911_DIB_PULSER.stop()
	new_state.RS3_911_PR2_LED = state.RS3_911_DIB_ACTIVE and (not bool(timers.RS3_911_DIB_PULSER)) and state.RS3_911_PR2_LAT
	return new_state

def rs3_911_edoor_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS3_911_PR1_LAT and rising(state, prev_state, 'RS3_911_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS3_911_EDR_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS3_911_DIB_TMR")
		timers.RS3_911_DIB_TMR.start()
	new_state.RS3_911_DIB_ACTIVE = bool(timers.RS3_911_DIB_TMR)
	new_state.RS3_911_EDR_CLS_ILCK = bool(timers.RS3_911_DIB_TMR) or state.RS3_911_EDR_CLS_RT
	return new_state
	
def rs3_911_edr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_911_EDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS3_911_EDR_CLS_LAT) and state.RS3_911_EDR_CLS_RT
	return new_state

def rs3_911_preserved_search(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_911_PRSVD_SRCH_LAT = state.RS3_911_PR1_LAT and state.RS3_911_PR2_LAT
	return new_state

def rs3_911_preserved_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_911_PRSVD_SRCH_LED = state.RS3_911_DIB_ACTIVE and bool(timers.RS3_911_SEARCH_LED_PULSER) and state.RS3_911_PRSVD_SRCH_LAT
	return new_state	

def rs3_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS3_PR1_KSW_RT') or rising(state, prev_state, 'RS3_PR1_TESTBTN_RT')
	new_state.RS3_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS3_PR1_LAT) and (state.RS3_SRCH_SET_LAT or state.RS3_SRCH_TMR_ACTV) and state.RS3A_GT_CLS_ILCK and state.RS3B_GT_CLS_RT and state.RS3C_GT_CLS_RT and state.RS3_911_PRSVD_SRCH_LAT
	new_state.RS3_PR1_LED = new_state.RS3_PR1_LAT
	return new_state

def rs3_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_PR2_LAT = (((rising(state, prev_state, 'RS3_PR2_KSW_RT') or rising(state, prev_state, 'RS3_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS3_PR2_LAT) and (state.RS3_SRCH_SET_LAT or state.RS3_SRCH_TMR_ACTV) and state.RS3A_GT_CLS_ILCK and state.RS3B_GT_CLS_RT and state.RS3C_GT_CLS_RT and state.RS3_PR1_LAT
	return new_state

def rs3_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS3_DIB_ACTIVE and not timers.RS3_DIB_PULSER.running():
		timers.RS3_DIB_PULSER.start()
	elif not state.RS3_DIB_ACTIVE:
		timers.RS3_DIB_PULSER.stop()
	new_state.RS3_PR2_LED = state.RS3_DIB_ACTIVE and (not bool(timers.RS3_DIB_PULSER)) and state.RS3_PR2_LAT
	return new_state

def rs3a_gate_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS3_PR1_LAT and rising(state, prev_state, 'RS3_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS3A_GT_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS3_DIB_TMR")
		timers.RS3_DIB_TMR.start()
	new_state.RS3_DIB_ACTIVE = bool(timers.RS3_DIB_TMR)
	new_state.RS3A_GT_CLS_ILCK = bool(timers.RS3_DIB_TMR) or state.RS3A_GT_CLS_RT
	return new_state

def rs3a_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3A_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS3A_GT_CLS_LAT) and state.RS3A_GT_CLS_RT
	return new_state

def rs3b_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3B_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS3B_GT_CLS_LAT) and state.RS3B_GT_CLS_RT
	return new_state

def rs3c_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3C_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS3C_GT_CLS_LAT) and state.RS3C_GT_CLS_RT
	return new_state

def rs3_all_gates_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_ALL_GTS_CLS_LAT = state.RS3A_GT_CLS_LAT and state.RS3B_GT_CLS_LAT and state.RS3C_GT_CLS_LAT
	return new_state

def rs3_search_set(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	search_request = (state.RS3_SRCH_SET_KSW_RT or state.RS3_SRCH_SET_TESTBTN_RT) and state.ACR_HW_EN_RT and state.EPICS_RS3_SRCH_SET_BTN and state.RS3_SRCH_TMR_ACTV
	new_state.RS3_SRCH_SET_LAT = (search_request or state.RS3_SRCH_SET_LAT) and state.RS3_ALL_GTS_CLS_LAT and state.RS3_911_PRSVD_SRCH_LAT and state.RS3_PR1_LAT and state.RS3_PR2_LAT
	return new_state

def rs3_all_gates_and_doors_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_ALL_GTS_DRS_CLS_LAT = state.RS3_911_EDR_CLS_LAT and state.RS3_ALL_GTS_CLS_LAT
	return new_state

def rs3_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS3_SRCH_SET_LED = state.RS3_DIB_ACTIVE and bool(timers.RS3_SEARCH_LED_PULSER) and state.RS3_SRCH_SET_LAT
	return new_state

#____

def rs4_912_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS4_912_PR1_KSW_RT') or rising(state, prev_state, 'RS4_912_PR1_TESTBTN_RT')
	new_state.RS4_912_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS4_912_PR1_LAT) and state.RS4_912_WDR_CLS_ILCK and (state.RS4_912_PRSVD_SRCH_LAT or state.RS4_SRCH_TMR_ACTV)
	new_state.RS4_912_PR1_LED = new_state.RS4_912_PR1_LAT
	return new_state

def rs4_912_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_912_PR2_LAT = (((rising(state, prev_state, 'RS4_912_PR2_KSW_RT') or rising(state, prev_state, 'RS4_912_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS4_912_PR2_LAT) and state.RS4_912_WDR_CLS_ILCK and state.RS4_912_PR1_LAT and (state.RS4_912_PRSVD_SRCH_LAT or state.RS4_SRCH_TMR_ACTV)
	return new_state

def rs4_search_timer(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start_rs4_912 = (state.RS4_912_PR1_LAT or state.RS4_912_PR1_KSW_RT or state.RS4_912_PR1_TESTBTN_RT) and (not state.RS4_912_PRSVD_SRCH_LAT)
	timer_start_rs4 = (state.RS4_PR1_LAT or state.RS4_PR1_KSW_RT or state.RS4_PR1_TESTBTN_RT) and state.RS4_912_PRSVD_SRCH_LAT and (not state.RS4_SRCH_SET_LAT)
	#logging.debug(timer_start_rs4)
	result = None
	if timer_start_rs4_912:
		timers.RS4_SRCH_TMR.start()
		logging.debug("   -Starting RS4_SRCH_TMR for RS4_912")
		result = timer_start_rs4_912 and (not timers.RS4_SRCH_TMR.done())
	elif timer_start_rs4:
		timers.RS4_SRCH_TMR.start()
		logging.debug("   -Starting RS4_SRCH_TMR for RS4")
		result = timer_start_rs4 and (not timers.RS4_SRCH_TMR.done())	  
	new_state.RS4_SRCH_TMR_ACTV = result
	return new_state

def rs4_912_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS4_912_DIB_ACTIVE and not timers.RS4_912_DIB_PULSER.running():
		timers.RS4_912_DIB_PULSER.start()
	elif not state.RS4_912_DIB_ACTIVE:
		timers.RS4_912_DIB_PULSER.stop()
	new_state.RS4_912_PR2_LED = state.RS4_912_DIB_ACTIVE and (not bool(timers.RS4_912_DIB_PULSER)) and state.RS4_912_PR2_LAT
	return new_state
	
def rs4_912_wdoor_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()

	initiate_dib = state.RS4_912_PR1_LAT and rising(state, prev_state, 'RS4_912_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS4_912_WDR_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS4_912_DIB_TMR")
		timers.RS4_912_DIB_TMR.start()
	new_state.RS4_912_DIB_ACTIVE = bool(timers.RS4_912_DIB_TMR)
	new_state.RS4_912_WDR_CLS_ILCK = bool(timers.RS4_912_DIB_TMR) or state.RS4_912_WDR_CLS_RT
	return new_state

def rs4_912_wdr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_912_WDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS4_912_WDR_CLS_LAT) and state.RS4_912_WDR_CLS_RT
	return new_state

def rs4_912_preserved_search(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_912_PRSVD_SRCH_LAT = state.RS4_912_PR1_LAT and state.RS4_912_PR2_LAT
	return new_state

def rs4_912_preserved_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_912_PRSVD_SRCH_LED = state.RS4_912_DIB_ACTIVE and bool(timers.RS4_912_SEARCH_LED_PULSER) and state.RS4_912_PRSVD_SRCH_LAT
	return new_state

def rs4_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS4_PR1_KSW_RT') or rising(state, prev_state, 'RS4_PR1_TESTBTN_RT')
	new_state.RS4_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS4_PR1_LAT) and (state.RS4_SRCH_SET_LAT or state.RS4_SRCH_TMR_ACTV) and state.RS4A_GT_CLS_ILCK and state.RS4B_GT_CLS_RT and state.RS4C_GT_CLS_RT and state.RS4_912_PRSVD_SRCH_LAT
	new_state.RS4_PR1_LED = new_state.RS4_PR1_LAT
	return new_state

def rs4_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_PR2_LAT = (((rising(state, prev_state, 'RS4_PR2_KSW_RT') or rising(state, prev_state, 'RS4_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS4_PR2_LAT) and (state.RS4_SRCH_SET_LAT or state.RS4_SRCH_TMR_ACTV) and state.RS4A_GT_CLS_ILCK and state.RS4B_GT_CLS_RT and state.RS4C_GT_CLS_RT and state.RS4_PR1_LAT
	return new_state

def rs4_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS4_DIB_ACTIVE and not timers.RS4_DIB_PULSER.running():
		timers.RS4_DIB_PULSER.start()
	elif not state.RS4_DIB_ACTIVE:
		timers.RS4_DIB_PULSER.stop()
	new_state.RS4_PR2_LED = state.RS4_DIB_ACTIVE and (not bool(timers.RS4_DIB_PULSER)) and state.RS4_PR2_LAT
	return new_state

def rs4a_gate_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS4_PR1_LAT and rising(state, prev_state, 'RS4_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS4A_GT_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS4_DIB_TMR")
		timers.RS4_DIB_TMR.start()
	new_state.RS4_DIB_ACTIVE = bool(timers.RS4_DIB_TMR)
	new_state.RS4A_GT_CLS_ILCK = bool(timers.RS4_DIB_TMR) or state.RS4A_GT_CLS_RT
	return new_state

def rs4a_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	#logging.debug(f"({state.ACR_HW_EN_RT} & {state.EPICS_ILCK_SET_BTN} & {state.PERMITTED_ACCESS} or {state.RS4A_GT_CLS_LAT}) & {state.RS4A_GT_CLS_RT}")
	new_state.RS4A_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS4A_GT_CLS_LAT) and state.RS4A_GT_CLS_RT
	return new_state

def rs4b_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4B_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS4B_GT_CLS_LAT) and state.RS4B_GT_CLS_RT
	return new_state

def rs4c_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4C_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS4C_GT_CLS_LAT) and state.RS4C_GT_CLS_RT
	return new_state

def rs4_all_gates_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_ALL_GTS_CLS_LAT = state.RS4A_GT_CLS_LAT and state.RS4B_GT_CLS_LAT and state.RS4C_GT_CLS_LAT
	return new_state

def rs4_search_set(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	search_request = (state.RS4_SRCH_SET_KSW_RT or state.RS4_SRCH_SET_TESTBTN_RT) and state.ACR_HW_EN_RT and state.EPICS_RS4_SRCH_SET_BTN and state.RS4_SRCH_TMR_ACTV
	new_state.RS4_SRCH_SET_LAT = (search_request or state.RS4_SRCH_SET_LAT) and state.RS4_ALL_GTS_CLS_LAT and state.RS4_912_PRSVD_SRCH_LAT and state.RS4_PR1_LAT and state.RS4_PR2_LAT
	return new_state

def rs4_all_gates_and_doors_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_ALL_GTS_DRS_CLS_LAT = state.RS4_912_WDR_CLS_LAT and state.RS4_ALL_GTS_CLS_LAT
	return new_state

def rs4_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS4_SRCH_SET_LED = state.RS4_DIB_ACTIVE and bool(timers.RS4_SEARCH_LED_PULSER) and state.RS4_SRCH_SET_LAT
	return new_state	

#____

def rs5_913_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS5_913_PR1_KSW_RT') or rising(state, prev_state, 'RS5_913_PR1_TESTBTN_RT')
	new_state.RS5_913_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS5_913_PR1_LAT) and state.RS5_913_WDR_CLS_ILCK and state.RS5_913_SDR_CLS_RT and (state.RS5_913_PRSVD_SRCH_LAT or state.RS5_SRCH_TMR_ACTV)
	new_state.RS5_913_PR1_LED = new_state.RS5_913_PR1_LAT
	return new_state

def rs5_search_timer(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start_rs5_913 = (state.RS5_913_PR1_LAT or state.RS5_913_PR1_KSW_RT) and (not state.RS5_913_PRSVD_SRCH_LAT)
	timer_start_rs5 = (state.RS5_PR1_LAT or state.RS5_PR1_KSW_RT) and state.RS5_913_PRSVD_SRCH_LAT and (not state.RS5_SRCH_SET_LAT)
	result = None
	if timer_start_rs5_913:
		timers.RS5_SRCH_TMR.start()
		logging.debug("   -Starting RS5_SRCH_TMR for RS5_913")
		result = timer_start_rs5_913 and (not timers.RS5_SRCH_TMR.done())
	elif timer_start_rs5:
		timers.RS5_SRCH_TMR.start()
		logging.debug("   -Starting RS5_SRCH_TMR for RS5")
		result = timer_start_rs5 and (not timers.RS5_SRCH_TMR.done())	  
	new_state.RS5_SRCH_TMR_ACTV = result
	return new_state

def rs5_913_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_913_PR2_LAT = (((rising(state, prev_state, 'RS5_913_PR2_KSW_RT') or rising(state, prev_state, 'RS5_913_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS5_913_PR2_LAT) and state.RS5_913_WDR_CLS_ILCK and state.RS5_913_PR1_LAT and state.RS5_913_SDR_CLS_RT and (state.RS5_913_PRSVD_SRCH_LAT or state.RS5_SRCH_TMR_ACTV)
	return new_state

def rs5_913_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS5_913_DIB_ACTIVE and not timers.RS5_913_DIB_PULSER.running():
		timers.RS5_913_DIB_PULSER.start()
	elif not state.RS5_913_DIB_ACTIVE:
		timers.RS5_913_DIB_PULSER.stop()
	new_state.RS5_913_PR2_LED = state.RS5_913_DIB_ACTIVE and (not bool(timers.RS5_913_DIB_PULSER)) and state.RS5_913_PR2_LAT
	return new_state

def rs5_913_wdoor_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()

	initiate_dib = state.RS5_913_PR1_LAT and rising(state, prev_state, 'RS5_913_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS5_913_WDR_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS5_913_DIB_TMR")
		timers.RS5_913_DIB_TMR.start()
	new_state.RS5_913_DIB_ACTIVE = bool(timers.RS5_913_DIB_TMR)
	new_state.RS5_913_WDR_CLS_ILCK = bool(timers.RS5_913_DIB_TMR) or state.RS5_913_WDR_CLS_RT
	return new_state

def rs5_913_wdr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_913_WDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS5_913_WDR_CLS_LAT) and state.RS5_913_WDR_CLS_RT
	return new_state

def rs5_913_sdr_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_913_SDR_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS5_913_SDR_CLS_LAT) and state.RS5_913_SDR_CLS_RT
	return new_state

def rs5_913_all_doors_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_913_ALL_DRS_CLS_LAT = state.RS5_913_WDR_CLS_LAT and state.RS5_913_SDR_CLS_LAT
	return new_state

def rs5_913_preserved_search(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_913_PRSVD_SRCH_LAT = state.RS5_913_PR1_LAT and state.RS5_913_PR2_LAT
	return new_state

def rs5_913_preserved_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_913_PRSVD_SRCH_LED = state.RS5_913_DIB_ACTIVE and bool(timers.RS5_913_SEARCH_LED_PULSER) and state.RS5_913_PRSVD_SRCH_LAT
	return new_state

def rs5_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS5_PR1_KSW_RT') or rising(state, prev_state, 'RS5_PR1_TESTBTN_RT')
	new_state.RS5_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS5_PR1_LAT) and (state.RS5_SRCH_SET_LAT or state.RS5_SRCH_TMR_ACTV) and state.RS5A_GT_CLS_ILCK and state.RS5B_GT_CLS_RT and state.RS5C_GT_CLS_RT and state.RS5DE_GT_CLS_RT and state.RS5_913_PRSVD_SRCH_LAT
	new_state.RS5_PR1_LED = new_state.RS5_PR1_LAT
	return new_state

def rs5_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_PR2_LAT = (((rising(state, prev_state, 'RS5_PR2_KSW_RT') or rising(state, prev_state, 'RS5_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS5_PR2_LAT) and (state.RS5_SRCH_SET_LAT or state.RS5_SRCH_TMR_ACTV) and state.RS5A_GT_CLS_ILCK and state.RS5B_GT_CLS_RT and state.RS5C_GT_CLS_RT and state.RS5DE_GT_CLS_RT and state.RS5_PR1_LAT
	return new_state

def rs5_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RS5_DIB_ACTIVE and not timers.RS5_DIB_PULSER.running():
		timers.RS5_DIB_PULSER.start()
	elif not state.RS5_DIB_ACTIVE:
		timers.RS5_DIB_PULSER.stop()
	new_state.RS5_PR2_LED = state.RS5_DIB_ACTIVE and (not bool(timers.RS5_DIB_PULSER)) and state.RS5_PR2_LAT
	return new_state

def rs5a_gate_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RS5_PR1_LAT and rising(state, prev_state, 'RS5_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS5A_GT_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RS5_DIB_TMR")
		timers.RS5_DIB_TMR.start()
	new_state.RS5_DIB_ACTIVE = bool(timers.RS5_DIB_TMR)
	new_state.RS5A_GT_CLS_ILCK = bool(timers.RS5_DIB_TMR) or state.RS5A_GT_CLS_RT
	return new_state

def rs5a_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5A_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS5A_GT_CLS_LAT) and state.RS5A_GT_CLS_RT
	return new_state

def rs5b_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5B_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS5B_GT_CLS_LAT) and state.RS5B_GT_CLS_RT
	return new_state

def rs5c_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5C_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS5C_GT_CLS_LAT) and state.RS5C_GT_CLS_RT
	return new_state

def rs5de_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5DE_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS5DE_GT_CLS_LAT) and state.RS5DE_GT_CLS_RT
	return new_state

def rs5_all_gates_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_ALL_GTS_CLS_LAT = state.RS5A_GT_CLS_LAT and state.RS5B_GT_CLS_LAT and state.RS5C_GT_CLS_LAT and state.RS5DE_GT_CLS_LAT
	return new_state

def rs5_search_set(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	search_request = (state.RS5_SRCH_SET_KSW_RT or state.RS5_SRCH_SET_TESTBTN_RT) and state.ACR_HW_EN_RT and state.EPICS_RS5_SRCH_SET_BTN and state.RS5_SRCH_TMR_ACTV
	new_state.RS5_SRCH_SET_LAT = (search_request or state.RS5_SRCH_SET_LAT) and state.RS5_ALL_GTS_CLS_LAT and state.RS5_913_PRSVD_SRCH_LAT and state.RS5_PR1_LAT and state.RS5_PR2_LAT
	return new_state

def rs5_all_gates_and_doors_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_ALL_GTS_DRS_CLS_LAT = state.RS5_913_ALL_DRS_CLS_LAT and state.RS5_ALL_GTS_CLS_LAT
	return new_state

def rs5_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS5_SRCH_SET_LED = state.RS5_DIB_ACTIVE and bool(timers.RS5_SEARCH_LED_PULSER) and state.RS5_SRCH_SET_LAT
	return new_state

#____

def rt1_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RT1_PR1_KSW_RT') or rising(state, prev_state, 'RT1_PR1_TESTBTN_RT')
	new_state.RT1_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RT1_PR1_LAT) and state.RT1A_GT_CLS_ILCK and state.RT1B_GT_CLS_RT and (state.RT1_SRCH_SET_LAT or state.RT1_SRCH_TMR_ACTV)
	new_state.RT1_PR1_LED = new_state.RT1_PR1_LAT
	return new_state

def rt1_search_timer(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start = (state.RT1_PR1_TESTBTN_RT or state.RT1_PR1_KSW_RT or state.RT1_PR1_LAT) and (not state.RT1_SRCH_SET_LAT)
	if timer_start:
		logging.debug("   -Starting RT1_SRCH_TMR")
		timers.RT1_SRCH_TMR.start()
	new_state.RT1_SRCH_TMR_ACTV = timer_start and (not timers.RT1_SRCH_TMR.done())
	return new_state

def rt1_search_timer_PATCHED(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start = (state.RT1_PR1_TESTBTN_RT or state.RT1_PR1_KSW_RT or state.RT1_PR1_LAT) and (not state.RT1_SRCH_SET_LAT)
	if not timer_start:
		timers.RT1_SRCH_TMR.stop()
	if timer_start and not timers.RT1_SRCH_TMR.running():
		logging.debug("Starting RT1_SRCH_TMR")
		timers.RT1_SRCH_TMR.start()
	new_state.RT1_SRCH_TMR_ACTV = timer_start and (not timers.RT1_SRCH_TMR.done())
	return new_state

def rt1_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RT1_PR2_LAT = (((rising(state, prev_state, 'RT1_PR2_KSW_RT') or rising(state, prev_state, 'RT1_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RT1_PR2_LAT) and state.RT1A_GT_CLS_ILCK and state.RT1B_GT_CLS_RT and state.RT1_PR1_LAT and (state.RT1_SRCH_SET_LAT or state.RT1_SRCH_TMR_ACTV)
	return new_state

def rt1_preset_2_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	if state.RT1_DIB_ACTIVE and not timers.RT1_DIB_PULSER.running():
		timers.RT1_DIB_PULSER.start()
	elif not state.RT1_DIB_ACTIVE:
		timers.RT1_DIB_PULSER.stop()
	new_state.RT1_PR2_LED = state.RT1_DIB_ACTIVE and (not bool(timers.RT1_DIB_PULSER)) and state.RT1_PR2_LAT
	return new_state

def rt1_gate_closed_interlock(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	initiate_dib = state.RT1_PR1_LAT and rising(state, prev_state, 'RT1_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RT1A_GT_CLS_RT
	if initiate_dib:
		logging.debug("   -Starting RT1_DIB_TMR")
		timers.RT1_DIB_TMR.start()
	new_state.RT1_DIB_ACTIVE = bool(timers.RT1_DIB_TMR)
	new_state.RT1A_GT_CLS_ILCK = bool(timers.RT1_DIB_TMR) or state.RT1A_GT_CLS_RT
	return new_state

def rt1a_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RT1A_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RT1A_GT_CLS_LAT) and state.RT1A_GT_CLS_RT
	return new_state

def rt1b_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RT1B_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RT1B_GT_CLS_LAT) and state.RT1B_GT_CLS_RT
	return new_state

def rt1_all_gates_closed(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RT1_ALL_GTS_CLS_LAT = state.RT1A_GT_CLS_LAT and state.RT1B_GT_CLS_LAT
	return new_state

def rt1_search_set(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	search_request = (state.RT1_SRCH_SET_KSW_RT or state.RS1_SRCH_SET_TESTBTN_RT) and state.ACR_HW_EN_RT and state.EPICS_RT1_SRCH_SET_BTN and state.RT1_SRCH_TMR_ACTV
	new_state.RT1_SRCH_SET_LAT = (search_request or state.RT1_SRCH_SET_LAT) and state.RT1_ALL_GTS_CLS_LAT and state.RT1_PR1_LAT and state.RT1_PR2_LAT
	return new_state

def rt1_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RT1_SRCH_SET_LED = state.RT1_DIB_ACTIVE and bool(timers.RT1_SEARCH_LED_PULSER) and state.RS1_SRCH_SET_LAT
	return new_state	