#!/usr/bin/env python3


import psutil

usage = psutil.virtual_memory()


def memory_usage(memusage="all"):
    if memusage == "all":
        return usage
    elif memusage == "free":
        return psutil.virtual_memory().free
    elif memusage == "total":
        return psutil.virtual_memory().total
    elif memusage == "avaiable":
        return psutil.virtual_memory().available
    elif memusage == "percent":
        return psutil.virtual_memory().percent
    elif memusage == "used":
        return psutil.virtual_memory().used
