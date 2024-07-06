from dataclasses import dataclass, replace
from pulser import Pulser
from timer import Timer

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
	RS1_GT_CLS_RT: bool
	RS1_SRCH_SET_KSW_RT: bool
	RS1_SRCH_SET_TESTBTN_RT: bool
	EPICS_RS1_SRCH_SET_BTN: bool
	#Outputs
	##RS1
	RS1_PR1_LED: bool
	RS1_PR2_LED: bool
	RS1_SRCH_SET_LED: bool
	#Internal Bits
	##Global
	PERMITTED_ACCESS: bool
	##RS1
	RS1_SRCH_SET_LAT: bool
	RS1_SRCH_TMR_ACTV: bool
	RS1_GT_CLS_ILCK: bool
	RS1_PR1_LAT: bool
	RS1_PR2_LAT: bool
	RS1_DIB_ACTIVE: bool
	RS1_GT_CLS_LAT: bool
	
	def copy(self):
		return replace(self)

@dataclass
class RSYTimers:
	RS1_SRCH_TMR: Timer
	RS1_DIB_TMR: Timer
	RS1_DIB_PULSER: Pulser
	RS1_SEARCH_LED_PULSER: Pulser

def rising(state, prev_state, key):
	return getattr(prev_state,key) == False and getattr(state,key) == True

def falling(state, prev_state, key):
	return getattr(prev_state,key) == True and getattr(state,key) == False

def rs1_preset_1(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	key_or_button_rising = rising(state, prev_state, 'RS1_PR1_KSW_RT') or rising(state, prev_state, 'RS1_PR1_TESTBTN_RT')
	new_state.RS1_PR1_LAT = ((key_or_button_rising and state.PERMITTED_ACCESS) or state.RS1_PR1_LAT) and state.RS1_GT_CLS_ILCK and (state.RS1_SRCH_SET_LAT or state.RS1_SRCH_TMR_ACTV)
	new_state.RS1_PR1_LED = new_state.RS1_PR1_LAT
	return new_state

def rs1_search_timer(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start = (state.RS1_PR1_TESTBTN_RT or state.RS1_PR1_KSW_RT or state.RS1_PR1_LAT) and (not state.RS1_SRCH_SET_LAT)
	if timer_start:
		print("Starting RS1_SRCH_TMR")
		timers.RS1_SRCH_TMR.start()
	new_state.RS1_SRCH_TMR_ACTV = timer_start and (not timers.RS1_SRCH_TMR.done())
	return new_state
	
def rs1_search_timer_PATCHED(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	timer_start = (state.RS1_PR1_TESTBTN_RT or state.RS1_PR1_KSW_RT or state.RS1_PR1_LAT) and (not state.RS1_SRCH_SET_LAT)
	if not timer_start:
		timers.RS1_SRCH_TMR.stop()
	if timer_start and not timers.RS1_SRCH_TMR.running():
		print("Starting RS1_SRCH_TMR")
		timers.RS1_SRCH_TMR.start()
	new_state.RS1_SRCH_TMR_ACTV = timer_start and (not timers.RS1_SRCH_TMR.done())
	return new_state

def rs1_preset_2(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS1_PR2_LAT = (((rising(state, prev_state, 'RS1_PR2_KSW_RT') or rising(state, prev_state, 'RS1_PR2_TESTBTN_RT')) and state.PERMITTED_ACCESS) or state.RS1_PR2_LAT) and state.RS1_GT_CLS_ILCK and state.RS1_PR1_LAT and (state.RS1_SRCH_SET_LAT or state.RS1_SRCH_TMR_ACTV)
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
	initiate_dib = state.RS1_PR1_LAT and rising(state, prev_state, 'RS1_PR2_KSW_RT') and state.PERMITTED_ACCESS and state.RS1_GT_CLS_RT
	if initiate_dib:
		print("Starting RS1_DIB_TMR")
		timers.RS1_DIB_TMR.start()
	new_state.RS1_DIB_ACTIVE = bool(timers.RS1_DIB_TMR)
	new_state.RS1_GT_CLS_ILCK = bool(timers.RS1_DIB_TMR) or state.RS1_GT_CLS_RT
	return new_state
	
def rs1a_gate_closed_latch(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS1_GT_CLS_LAT = ((state.ACR_HW_EN_RT and state.EPICS_ILCK_SET_BTN and state.PERMITTED_ACCESS) or state.RS1_GT_CLS_LAT) and state.RS1_GT_CLS_RT
	return new_state

def rs1_search_set(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	search_request = (state.RS1_SRCH_SET_KSW_RT or state.RS1_SRCH_SET_TESTBTN_RT) and state.ACR_HW_EN_RT and state.EPICS_RS1_SRCH_SET_BTN and state.RS1_SRCH_TMR_ACTV
	new_state.RS1_SRCH_SET_LAT = (search_request or state.RS1_SRCH_SET_LAT) and state.RS1_GT_CLS_LAT and state.RS1_PR1_LAT and state.RS1_PR2_LAT
	return new_state
	
def rs1_search_led(state: RSYState, prev_state: RSYState, timers: RSYTimers):
	new_state = state.copy()
	new_state.RS1_SRCH_SET_LED = state.RS1_DIB_ACTIVE and bool(timers.RS1_SEARCH_LED_PULSER) and state.RS1_SRCH_SET_LAT
	return new_state