#!/usr/bin/env python3
import time
import psutil

while True:
    current_CPU_Usage = psutil.cpu_percent(interval=1)
    print("Current %CPU Usage is: ", current_CPU_Usage)
    time.sleep(1)
