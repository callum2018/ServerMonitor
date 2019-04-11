#!/usr/bin/env python3

"""
needs vext.gi and playsound

"""

from gtts import gTTS
from playsound import playsound


def speak(text):
    """"""
    filename = "speech.mp3"
    talk = gTTS(text)
    talk.save(filename)
    playsound(filename)
