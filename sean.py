#!/usr/bin/env python3

from subprocess import check_output

def users():
    output = check_output(["uptime"]) .decode("utf-8").split()
    return int(output[-7])


def identity():
    return check_output(["whoami"]) .decode("utf-8").split()[0]

#print(user_info())




