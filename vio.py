#!/usr/bin/env python3
"""
Can be combined within codes that need an alarm
"""
import sys
import time
import easygui

def bell():
    sys.stdout.write('\a')
    sys.stdout.flush()

def alarm_bell():
    """alarms for 2 sec"""
    for times in range(10):
        bell()
        time.sleep(.02)

def dialog(text,title):
    """Will Output a message."""
    easygui.msgbox(text, title=title)


#dialog("hello", "Information")
