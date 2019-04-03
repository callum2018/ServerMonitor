#!/usr/bin/env python3


import os

check = input("Shutdown computer ? (y/n): ")
if check == 'n':
    exit()
else:
    os.system('shutdown -h 1')
