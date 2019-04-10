import os


def pingtest(machine):
    """
     The program pings a chosen website or server, the '-c 1' means that it will ping just once. and the '> /dev/null' sends away the unwanted results.
     If we get an exit code of 0, it means that the site or server is working properly, otherwise it indicates that it's not running as intended.
    """
    ping = os.system("ping -c 1 " + machine + " > /dev/null" )
    #print(ping)
    if ping == 0:
        return machine + 'is running without any faults.'
    else:
        return machine + 'is not running.'


#print(pingtest("mallowcollege.ie"))
