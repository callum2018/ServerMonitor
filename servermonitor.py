#!/usr/bin/env python3

"""This program monitors the server and outputs to screen, to HTML.  ...

TO DO:

    Daniel: consolidate into single module called daniel.py
    Sean: upload files
    Matthew, Daniel, Adam, Sean: add code to servermonitor.py

    Eoin, Vio: review integration.
    Rebecca: correct time() code error.

    Generate all pydoc documenation and add to GitHub."""

from time import sleep
from rebecca import *
from vio import *
from eoin import *
# add your import

__author__ = 'Computer Systems & Networks 2019: Rebecca, Vio, Eoin'
__credits__ = 'Copyright 2019, Computer Systems & Networks Class 2019, Mallow College, eoinospealain@mallowcollege.ie, released on GPL.'
__version__ = 'Prototype 0.1'

interval = 5 * 60 # 5 minutes in seconds

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\n The Date is: " + system_date() # eoin
    message += "\n The Time is: " + system_time() # eoin
    message += "\nUptime is: " + up_time()  # rebecca
    message += "\nLoad is: " + load()  # rebecca
    message += "\nUser is: " + user()  # rebecca
    message += "\nTime is " + current_time()  # rebecca
    message += "\nThe Host Hame is: " + get_hostname()  # rebecca
    message += "\n\n ----------------\n\n"

    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><br>Date</b> is: " + system_date() # eoin
    html += "<p><br>Time</b> is: " + system_time() # eoin
    html += "<p><b>Uptime</b> is: " + up_time()  # rebecca
    html += "<p><b>Load</b> is: " + load()  # rebecca
    html += "<p><b>User</b> is: " + user()  # rebecca
    html += "<p><b>Time</b> is: " + current_time()  # rebecca
    html += "<p><b>The Host Hame is: </b> is " + get_hostname()  # rebecca

    # add your HTML contribution here

    html += "</body></html>"

    print(message)
    dialog(message, "Server Monitor 0.1")  # vio
    alarm_bell() # vio - could be used by an error statement

    report = open("servermonitor-report.html", "w")
    print(html, file=report)
    report.close()
    email("roomnineteenclass@gmail.com", "*************", "rebeccamacdonald2018@mallowcollege.email", "server monitor",
          "This is a update from your computer about " + message)  # rebecca

    # add any testing function here

    break  # break in loop for testing and PyDoc
    sleep(interval)