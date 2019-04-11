#!/usr/bin/env python3

"""This program monitors the server and outputs to screen, to HTML.  ...

TO DO:

    Daniel: consolidate into single module called daniel.py
    Matthew, Daniel, Adam, Sean: add code to servermonitor.py

    Eoin, Vio: review integration.

    Generate all pydoc documentation and add to GitHub."""

from time import sleep
from rebecca import *
from vio import *
from eoin import *
from sean import *
from matthew import *
from adam import *

# add your import

__author__ = 'Computer Systems & Networks 2019: Rebecca, Vio, Eoin, Sean, Adam, Matthew'
__credits__ = 'Copyright 2019, Computer Systems & Networks Class 2019, Mallow College, eoinospealain@mallowcollege.ie, released on GPL.'
__version__ = 'Prototype 0.1'

interval = 5 * 60 # 5 minutes in seconds
speech = True  # matthew

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\n The Date is: " + system_date() # eoin
    message += "\n The Time is: " + system_time() # eoin
    message += "\nUptime is: " + up_time()  # rebecca
    message += "\nLoad is: " + load()  # rebecca
    message += "\nUser is: " + user()  # rebecca
    message += "\nThere are " + str(users()) + " users and " + identity() + " is current user"  # sean
    message += "\nTime is " + current_time()  # rebecca
    message += "\nThe Hostname is: " + get_hostname()  # rebecca
    spokenmessage = message
    message += "\n\n ----------------\n\n"

    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><br>Date</b> is: " + system_date() # eoin
    html += "<p><br>Time</b> is: " + system_time() # eoin
    html += "<p><b>Uptime</b> is: " + up_time()  # rebecca
    html += "<p><b>Load</b> is: " + load()  # rebecca
    html += "<p><b>User</b> is: " + user()  # rebecca
    html += "<p>There are " + str(users()) + " users and " + identity() + " is current user"  # sean
    html += "<p><b>Time</b> is: " + current_time()  # rebecca
    html += "<p><b>The Hostname is: </b> is " + get_hostname()  # rebecca

    # add your HTML contribution here

    html += "</body></html>"

    print(message)
    dialog(message, "Server Monitor 0.1")  # vio
    alarm_bell() # vio - could be used by an error statement

    report = open("servermonitor-report.html", "w")
    print(html, file=report)
    report.close()
    # email("roomnineteenclass@gmail.com", "*************", "rebeccamacdonald2018@mallowcollege.email", "server monitor",
    #     "This is a update from your computer about " + message)  # rebecca
    if speech:
        speak(spokenmessage + "\nThis message will self destruct in 5 seconds, 4, 3, 2, 1, boom")
    # add any testing function here

    break  # break in loop for testing and PyDoc
    sleep(interval)