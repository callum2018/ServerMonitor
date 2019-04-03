#!/usr/bin/env python3


import os


def shut_down(shutdown="shut"):
    if shutdown == "shut":
        return os.system('shutdown -P')
