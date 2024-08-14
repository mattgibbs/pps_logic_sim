import time
import logging
#logging.basicConfig(level=logging.DEBUG)

items = [
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

def gate_door_test(test_class, gate_rt_name, gate_latch_name, gate_name):
    # Close gate
    logging.debug(f"\n-Starting {gate_name} Test")
    logging.debug(f" -Tester closed the {gate_name}.")
    setattr(test_class.engine.state, gate_rt_name, True)
    test_class.engine.process()
    test_class.assertTrue(getattr(test_class.engine.state, gate_rt_name), f"{gate_name} didn't stay closed.")
    test_class.assertFalse(getattr(test_class.engine.state, gate_latch_name), f"{gate_name} latched without pressing interlock reset.")
    
    # Latch
    logging.debug(" -Tester (controlled) pressing Interlock Reset and Hardware Enable.")
    with test_class.engine.momentary_press(['EPICS_ILCK_SET_BTN']):
        test_class.assertFalse(getattr(test_class.engine.state, gate_latch_name), f"{gate_name} latched without hardware enable.")
        with test_class.engine.momentary_press(['ACR_HW_EN_RT']):
            test_class.assertTrue(getattr(test_class.engine.state, gate_latch_name), f"{gate_name} not latched with harware enable and interlock reset held.")
        test_class.assertTrue(getattr(test_class.engine.state, gate_latch_name), f"{gate_name} didn't stay latched after releasing hardware enable.")
    test_class.assertTrue(getattr(test_class.engine.state, gate_latch_name), f"{gate_name} didn't stay latched after releasing interlock reset.")			
    logging.debug(f" -Tester got {gate_name} Latched.")

    # Open again
    logging.debug(f" -Tester opened the {gate_name}.")
    setattr(test_class.engine.state, gate_rt_name, False)
    test_class.engine.process()
    test_class.assertFalse(getattr(test_class.engine.state, gate_rt_name), f"{gate_name} didn't stay open.")
    test_class.assertFalse(getattr(test_class.engine.state, gate_latch_name), f"{gate_name} remained latched after opening.")
    logging.debug(f" -Lost the {gate_name} Latch because it was opened.")

def gate_dib_test(test_class, gate_rt_name, gate_interlock_name, dib_timer_name, dib_active_name, preset_1_name, preset_2_led_name, preset_2_ksw_name, gate_list, zone_name, prerequisite_search = None):
    logging.debug(f"\n-Starting {zone_name} Test Gate DIB")
    setattr(test_class.engine.state, gate_rt_name, True)
    test_class.assertTrue(getattr(test_class.engine.state, gate_rt_name), f"{gate_rt_name} is not closed.")
    test_class.assertFalse(getattr(test_class.engine.state, gate_interlock_name), f"{gate_interlock_name} true without gate closed.")
    
    if prerequisite_search is not None:
        for search in prerequisite_search:
            search()

    logging.debug(f"  -Tester closed all {zone_name} gates and doors.")
    for gate in gate_list:
        setattr(test_class.engine.state, gate, True)
        test_class.assertTrue(getattr(test_class.engine.state, gate), f"{zone_name} {gate} is not closed.")

    test_class.engine.process()
    test_class.assertTrue(getattr(test_class.engine.state, gate_interlock_name), f"{gate_interlock_name} not active in P/A with gate closed.")

    logging.debug("  -Tester magically already got preset 1 latched.")
    setattr(test_class.engine.state, preset_1_name, True)
    test_class.engine.process()
    test_class.assertFalse(getattr(test_class.engine.timers, dib_timer_name), f"{dib_timer_name} running before turning {zone_name} PR2 Keyswitch.")

    logging.debug("  -Tester turns preset 2 key to initate the DIB.")
    with test_class.engine.momentary_press(str(preset_2_ksw_name)):
        test_class.assertTrue(getattr(test_class.engine.timers, dib_timer_name), f"{dib_timer_name} not running after turning {zone_name} PR2 Keyswitch.")

    test_class.assertTrue(getattr(test_class.engine.timers, dib_timer_name), f"{dib_timer_name} not running after releasing {zone_name} PR2 Keyswitch.")
    test_class.assertTrue(getattr(test_class.engine.state, dib_active_name), f"{dib_active_name} not active while timer running.")
    test_class.assertTrue(getattr(test_class.engine.state, gate_interlock_name), f"{gate_interlock_name} is not True while {zone_name} DIB Active.")

    logging.debug(f"  -Tester opened the {gate_rt_name} to exit.")
    setattr(test_class.engine.state, gate_rt_name, False)
    test_class.engine.process()
    test_class.assertTrue(getattr(test_class.engine.state, gate_interlock_name), f"{gate_interlock_name} is not True with gate open and {zone_name} DIB Active.")
    with test_class.subTest(msg=f"{zone_name} Preset 2 LED Tests"):
        preset_2_led_values = []
        while (time.time() - getattr(test_class.engine.timers, dib_timer_name).time_started()) < getattr(test_class.engine.timers, dib_timer_name).duration():
            test_class.engine.process()
            preset_2_led_values.append(getattr(test_class.engine.state, preset_2_led_name))
            time.sleep(getattr(test_class.engine.timers, dib_timer_name).duration() / 10)
        test_class.assertFalse(all(preset_2_led_values), f"{zone_name} Preset 2 LED is not flashing (always on).")
        test_class.assertFalse(not any(preset_2_led_values), f"{zone_name} Preset 2 LED is not flashing (always off).")
    # Leave the gate open and let the DIB expire.
    logging.debug(f"  -Tester purposefully leave the {gate_rt_name} open and let the DIB expire.")
    test_class.engine.process()
    test_class.assertFalse(getattr(test_class.engine.state, gate_interlock_name), f"{gate_interlock_name} still True even after DIB timer expired.")

def keybank_test(test_class, kb_rt_name, kb_latch_name, kb_name):
    # Close gate
    logging.debug(f"\n-Starting {kb_name} Test")
    logging.debug(f" -Tester make sure the keybank is completed the {kb_name}.")
    setattr(test_class.engine.state, kb_rt_name, True)
    test_class.engine.process()
    test_class.assertTrue(getattr(test_class.engine.state, kb_rt_name), f"{kb_name} didn't stay latched.")
    test_class.assertFalse(getattr(test_class.engine.state, kb_latch_name), f"{kb_name} latched without pressing interlock reset.")
    
    # Latch
    logging.debug(" -Tester (controlled) pressing Interlock Reset and Hardware Enable.")
    with test_class.engine.momentary_press(['EPICS_ILCK_SET_BTN']):
        test_class.assertFalse(getattr(test_class.engine.state, kb_latch_name), f"{kb_name} latched without hardware enable.")
        with test_class.engine.momentary_press(['ACR_HW_EN_RT']):
            test_class.assertTrue(getattr(test_class.engine.state, kb_latch_name), f"{kb_name} not latched with harware enable and interlock reset held.")
        test_class.assertTrue(getattr(test_class.engine.state, kb_latch_name), f"{kb_name} didn't stay latched after releasing hardware enable.")
    test_class.assertTrue(getattr(test_class.engine.state, kb_latch_name), f"{kb_name} didn't stay latched after releasing interlock reset.")			
    logging.debug(f" -Tester got {kb_name} Latched.")

    # Open again
    logging.debug(f" -Tester magically make the {kb_name} not complete.")
    setattr(test_class.engine.state, kb_rt_name, False)
    test_class.engine.process()
    test_class.assertFalse(getattr(test_class.engine.state, kb_rt_name), f"{kb_name} didn't stay latche.")
    test_class.assertFalse(getattr(test_class.engine.state, kb_latch_name), f"{kb_name} remained latched after keybank not complete.")
    logging.debug(f" -Lost the {kb_name} Latch because it keybank not complete.")

def keybank_release_test(test_class, kb_rel_btn_name, kb_rel_name, kb_name):
    logging.debug(f"\n-Starting {kb_name} replease test.")
    # Test Case #1: PERM ACCESS
    logging.debug(f"  -Testing {kb_name} release under PERM ACCESS")
    test_class.assertTrue(getattr(test_class.engine.state, 'PERMITTED_ACCESS'), f"{kb_name} is not in PERM ACCESS")
    with test_class.engine.momentary_press([kb_rel_btn_name]):
        test_class.assertFalse(getattr(test_class.engine.state, kb_rel_name), f"{kb_name} released without hardware enable.")
        with test_class.engine.momentary_press(['ACR_HW_EN_RT']):
            test_class.assertTrue(getattr(test_class.engine.state, kb_rel_name), f"{kb_name} not released with harware enable and interlock reset held.")
    logging.debug(f"  -{kb_name} successfully released under PERM ACCESS")
    # Test Case #2: NO ACCESS
    logging.debug(f"  -Testing {kb_name} release under NO ACCESS")
    lock_down_mode(test_class, items)
    with test_class.engine.momentary_press([kb_rel_btn_name]):
        test_class.assertFalse(getattr(test_class.engine.state, kb_rel_name), f"{kb_name} released without hardware enable.")
        with test_class.engine.momentary_press(['ACR_HW_EN_RT']):
            test_class.assertFalse(getattr(test_class.engine.state, kb_rel_name), f"{kb_name} released with harware enable and interlock reset held.")   
    logging.debug(f"  -{kb_name} failed to released under NO ACCESS as expected.") 

def lock_down_mode(test_class, items):
    real_time = [item for item in items if "_CLS_RT" in item or "_COMPLETE_RT" in item or "_CLS_ILCK" in item]
    latch = [item for item in items if "_LAT" in item]
    for item in real_time:
        setattr(test_class.engine.state, item, True)
        test_class.assertTrue(getattr(test_class.engine.state, item), f"{item} is not closed.")
    for item in latch:
        setattr(test_class.engine.state, item, True)
        test_class.assertTrue(getattr(test_class.engine.state, item), f"{item} is not latched.")
    test_class.engine.process()
    setattr(test_class.engine.state, 'PERMITTED_ACCESS', False)
    setattr(test_class.engine.state, 'NO_ACCESS', True)
    test_class.assertTrue(getattr(test_class.engine.state, 'NO_ACCESS'), f"NO_ACCESS is not set.")
    test_class.assertFalse(getattr(test_class.engine.state, 'PERMITTED_ACCESS'), f"PERMITTED_ACCESS is set.")
    logging.debug("  -RSY is in NO_ACCESS.")
