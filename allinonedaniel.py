#!/usr/bin/env python3

import psutil
import os


def cpu_usage(usage="usage"):
    if usage == "usage":
        return psutil.cpu_percent(interval=1)


def shut_down(shutdown="shut"):
    if shutdown == "shut":
        return os.system('shutdown -P')


disk = psutil.disk_usage('/')


def disk_info(metric="percent"):
    """Returns disk information: valid options are percent, total, used, or free. Measures in GB rounded to 2 decimal places."""
    if metric == "percent":
        return disk.percent
    elif metric == "total":
        return round((disk.total / (1024.0 ** 3)), 2)
    elif metric == "used":
        return round((disk.used / (1024.0 ** 3)), 2)
    elif metric == "free":
        return round((disk.free / (1024.0 ** 3)), 2)


usage = psutil.virtual_memory()


def memory_usage(memusage="all"):
    if memusage == "all":
        return usage
    elif memusage == "free":
        return round(psutil.virtual_memory().free / (1024.0 ** 3), 2)
    elif memusage == "total":
        return round(psutil.virtual_memory().total / (1024.0 ** 3), 2)
    elif memusage == "available":
        return round(psutil.virtual_memory().available / (1024.0 ** 3), 2)
    elif memusage == "percent":
        return psutil.virtual_memory().percent
    elif memusage == "used":
        return round(psutil.virtual_memory().used / (1024.0 ** 3), 2)
