#!/usr/bin/env python3

"""
This program monitors the server and outputs to screen, to HTML.
"""
from memoryusage import *
from time import sleep
# add your import

interval = 5 * 60 # 5 minutes in seconds

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\n Memory free (GB) " + str(memory_usage("free")) # Daniel
    message += "\n Memory total (GB) " + str(memory_usage("total"))  # Daniel
    message += "\n Memory available (GB) " + str(memory_usage("available"))  # Daniel
    message += "\n Memory percent (%) " + str(memory_usage("percent"))  # Daniel
    message += "\n Memory used (GB) " + str(memory_usage("used"))  # Daniel
    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><b>Memory free (GB) </b> is " + str(memory_usage("free")) # Daniel
    html += "<p><b>Memory total (GB)</b> is " + str(memory_usage("total"))  # Daniel
    html += "<p><b>Memory available (GB)</b> is " + str(memory_usage("available"))  # Daniel
    html += "<p><b>Memory percent (%)</b> is " + str(memory_usage("percent"))  # Daniel
    html += "<p><b>Memory used (GB)</b> is " + str(memory_usage("used"))  # Daniel
    # add your HTML contribution here
    html += "</body></html>"

    print(message)
    report = open("servermonitor.html", "w")
    print(html, file=report)
    report.close()

    # add any testing function here

    sleep(interval)