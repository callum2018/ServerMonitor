#!/usr/bin/env python3

"""
This program monitors the server and outputs to screen, to HTML.
"""
__author__ = "Rebecca MacDonald"
__version__ = "1.0"
__emailaddress__ = "rebeccamacdonald2018@mallowcollege.email"

from rebecca import *
from time import sleep
# add your import

interval = 5 * 60 # 5 minutes in seconds

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\nUptime is " + up_time() # rebecca
    message += "\nLoad is " + load()  # rebecca
    message += "\nUser is " + user()  # rebecca
    message += "\nTime is " + time()  # rebecca
    message += "\nThe Host Hame is " + get_hostname()  # rebecca
    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><b>Uptime</b> is: " + up_time() # rebecca
    html += "<p><b>Load</b> is: " + load()  # rebecca
    html += "<p><b>User</b> is: " + user()  # rebecca
    html += "<p><b>Time</b> is: " + time()  # rebecca
    html += "<p><b>The Host Hame is: </b> is " + get_hostname()  # rebecca

    # add your HTML contribution here
    html += "</body></html>"
    email("roomnineteenclass@gmail.com", "*************", "rebeccamacdonald2018@mallowcollege.email", "server monitor", "This is a update from your computer about " + message)
    print(message)
    report = open("servermonitor.html", "w")
    print(html, file=report)
    report.close()

    # add any testing function here

    sleep(interval)