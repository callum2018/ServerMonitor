#!/usr/bin/env python3

"""
This program monitors the server and outputs to screen, to HTML.

Add more documentation ...

"""

__author__ = 'Computer Systems & Networks 2019: Rebecca, Vio, Eoin'
__copyright__ = 'Copyright 2019, Computer Systems & Networks.'
__credits__ = ['Road Runner', 'Road Runners best friend Harrold']
__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = ''
__email__ = 'eoinospealain@mallowcollege.ie'
__status__ = 'Prototype'

from time import sleep
from rebecca import *
from vio import *
from eoin import *
# add your import

interval = 5 * 60 # 5 minutes in seconds

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\n The Date is" + system_date()
    message += "\n The Time is" + system_time()
    message += "\nUptime is " + up_time()  # rebecca
    message += "\nLoad is " + load()  # rebecca
    message += "\nUser is " + user()  # rebecca
    message += "\nTime is " + time()  # rebecca
    message += "\nThe Host Hame is " + get_hostname()  # rebecca
    message += "\n\n ----------------\n\n"
    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><br>Date</b> is" + system_date()
    html += "<p><br>Time</b> is" + system_time()
    html += "<p><b>Uptime</b> is: " + up_time()  # rebecca
    html += "<p><b>Load</b> is: " + load()  # rebecca
    html += "<p><b>User</b> is: " + user()  # rebecca
    html += "<p><b>Time</b> is: " + time()  # rebecca
    html += "<p><b>The Host Hame is: </b> is " + get_hostname()  # rebecca
    # add your HTML contribution here

    html += "</body></html>"

    print(message)
    dialog(message)  # vio
    report = open("servermonitor.html", "w")
    print(html, file=report)
    report.close()
    email("roomnineteenclass@gmail.com", "*************", "rebeccamacdonald2018@mallowcollege.email", "server monitor",
          "This is a update from your computer about " + message)  # rebecca

    # add any testing function here

    sleep(interval)