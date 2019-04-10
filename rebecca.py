"""Module to return uptime information."""

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
    """this is the send email."""
    content = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (gmail_account, recipient, subject, message)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_account, password)
    server.sendmail(gmail_account, recipient, content)
    server.close()

gmail = "roomnineteenclass@gmail.com"
password = "************"
recipient = "roomnineteenclass@gmail.com"


email(gmail, password, recipient, "", "This is a warning from your computer about the *****.")



filename = "cpu.log"
gmail = "roomnineteenclass@gmail.com"
password = "***********"
recipient = "roomnineteenclass@gmail.com"
