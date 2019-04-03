#!/usr/bin/env python3

import psutil

disk = psutil.disk_usage('/')

total = (disk.total / (1024.0 ** 3))

used = (disk.used / (1024.0 ** 3))

free = (disk.free / (1024.0 ** 3))

print("Total Space: ", round(total, 2))
print("Used Space: ", round(used, 2))
print("Free Space: ", round(free, 2))
print("Percent Used: ", disk.percent)


