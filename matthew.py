#!/usr/bin/env python3

"""
needs vext.gi and playsound

"""

from gtts import gTTS
from playsound import playsound
"""Playsound: This imports playsound from the python files which allows the mp3 file to play 
through terminal without manually running it."""


"""gTTS : This imports google text-to-speech from the python files."""

def speak(text):
        """Speak is the function and what it does is it runs google text-to-speech which will say whatever the
    message is that comes up on the screen when we run servermonitor.py"""
    filename = "speech.mp3"  """This line here saves a file as speech.mp3 which is what plays when we run
     servermonitor."""
    talk = gTTS(text)
    talk.save(filename)
    playsound(filename)
