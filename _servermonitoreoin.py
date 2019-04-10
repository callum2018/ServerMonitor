
#!/usr/bin/env python3

"""
This program monitors the server and outputs to screen, to HTML.
"""

from time import sleep
from eoin import *
# add your import

interval = 5 * 60  # 5 minutes in seconds

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\n The Date is" + system_date()
    message += "\n The Time is" + system_time()
    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><br>Date</b> is" + system_date()
    html += "<p><br>Time</b> is" + system_time()
    # add your HTML contribution here
    html += "</body></html>"

    print(message)
    report = open("servermonitor.html", "w")
    print(html, file=report)
    report.close()

    # add any testing function here

    sleep(interval)