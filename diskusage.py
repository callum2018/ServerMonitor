#!/usr/bin/env python3

import psutil

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




