#!/usr/bin/env python3
"""Module to return uptime information, sending to email, hostname of computer.
 Using the smtplib that i imported for the email it needs gmail_account, password, recipient, subject and message. 
Using the socket function I imported to get the host name of the computer sending the message.
Using the check_output function I imported to get the uptime information which I then split up the information 
and get it to return the desired information counting from the end and counting to 0 we start at the end as the 
amount of argv can change depending on how long it has been up. 
uptime -p gives the pretty version then [1:] to give you all starting from 1 which leaves out the word up.
load is taking each peice of information and [-3] [-2][-1] and then 
adding them together to make a string and thats what is returned.
user is taking each peice of information and [-7] and returning it
time is taking each peice of information and [0]"""

__author__ = "Rebecca MacDonald"
__version__ = "1.0"
__emailaddress__ = "rebeccamacdonald2018@mallowcollege.email"

from subprocess import check_output
import socket
import smtplib

def up_time():
    """Returns the uptime."""
    output = " ".join(check_output(["uptime", "-p"]).decode("utf-8").split()[1:])
    return output

def load():
    """Returns the system load."""
    output = check_output(["uptime"]).decode("utf-8").split()
    load_1 = output[-3]
    load_2 = output[-2]
    load_3 = output[-1]
    load_average = load_1 + load_2 + load_3
    return load_average

def user():
    """Returns the number of users."""
    output = check_output(["uptime"]).decode("utf-8").split()
    user = output[-7]
    return user


def time():
    """Returns the time."""
    output = check_output(["uptime"]).decode("utf-8").split()
    time = output[0]
    return time

def get_hostname():
    """Returns the host name."""
    name = socket.gethostname()
    return name

def email(gmail_account, password, recipient, subject, message):
    """this is the send email ."""
    content = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (gmail_account, recipient, subject, message)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_account, password)
    server.sendmail(gmail_account, recipient, content)
    server.close()
