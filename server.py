#!/usr/bin/env python3

#author: Lam Ngo

import os
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

from bluetooth import *

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase("Hey Little Me")
    recognizer.expect_phrase("Turn on the LED")
    recognizer.expect_phrase("Turn off the LED")

    aiy.audio.get_recorder().start()

    port = 1
    sock = BluetoothSocket(RFCOMM)
    nb = discover_devices()
    if len(nb) > 0:
        sock.connect((nb[0],1))
        
    while True:
        aiy.audio.say("Set up Complete. Ready!")
