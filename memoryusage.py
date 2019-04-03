#!/usr/bin/env python3



import psutil

usage = psutil.virtual_memory()


def memory_usage(memusage="mem"):
    if memusage == "mem":
        return usage
