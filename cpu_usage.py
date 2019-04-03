#!/usr/bin/env python3

import psutil


def cpu_usage(usage="usage"):
    if usage == "usage":
        return psutil.cpu_percent(interval=1)

