#!/usr/bin/env python3


import psutil

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
