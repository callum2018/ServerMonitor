#!/usr/bin/env python3

"""
needs vext.gi and playsound
Playsound: This imports playsound from the python files which allows the mp3 file to play 
through terminal without manually running it, playsound also needs vext.gi to work properly.
gTTS : This imports google text-to-speech from the python files.
"""

from gtts import gTTS
from playsound import playsound

def speak(text):
        """This function runs google text to speech and sdays whatever the text is."""
    filename = "speech.mp3"
    talk = gTTS(text)
    talk.save(filename) """Saves a file as speech.mp3"""
    playsound(filename)
