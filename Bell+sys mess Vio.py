#!/usr/bin/env python3
"""
Can be combined within codes that need an alarm
"""
import sys
import time

def bell():
    sys.stdout.write('\a')
    sys.stdout.flush()


def alarm_bell():
    """alarms for 2 sec"""
    for times in range(100):
        bell()
        time.sleep(.02)

alarm_bell()



#!/usr/bin/env python3

"""Will Output a message."""
import easygui
easygui.msgbox("Warning Temp Is High!!! Get Out!!! It will explode!!!", title="Warning!!!!")
