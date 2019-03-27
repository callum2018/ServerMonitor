#!/usr/bin/env python3

import smtplib


def email(gmail_account, password, recipient, subject, message):
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
recipient = "rebeccamacdonald2018@mallowcollege.email"


email(gmail, password, recipient, "Warning", "This is a warning from your computer about ")
