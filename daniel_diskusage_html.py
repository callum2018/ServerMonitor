#!/usr/bin/env python3

"""
This program monitors the server and outputs to screen, to HTML.
"""
from diskusage import *
from time import sleep
# add your import

interval = 5 * 60 # 5 minutes in seconds

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\n Disk Percent used " + str(disk_info("percent")) # Daniel
    message += "\n Disk Total (GB) " + str(disk_info("total"))  # Daniel
    message += "\n Disk space used (GB) " + str(disk_info("used"))  # Daniel
    message += "\n Disk free (GB) " + str(disk_info("free"))  # Daniel
    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><b>Disk Percent used </b> is " + str(disk_info("percent")) # Daniel
    html += "<p><b>Disk Total (GB)</b> is " + str(disk_info("total"))  # Daniel
    html += "<p><b>Disk space used (GB)</b> is " + str(disk_info("used"))  # Daniel
    html += "<p><b>Disk free (GB)</b> is " + str(disk_info("free"))  # Daniel
    # add your HTML contribution here
    html += "</body></html>"

    print(message)
    report = open("diskusage.html", "w")
    print(html, file=report)
    report.close()

    # add any testing function here

    sleep(interval)