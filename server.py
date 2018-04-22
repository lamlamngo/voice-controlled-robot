#!/usr/bin/env python3

#author: Lam Ngo

import os
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import time

from bluetooth import *

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase("Hey Little Me")
    recognizer.expect_phrase("Turn on the light")
    recognizer.expect_phrase("Turn off the light")

    aiy.audio.get_recorder().start()

    port = 1
    sock = BluetoothSocket(RFCOMM)
    nb = discover_devices()
    led = aiy.voicehat.get_led()
    if len(nb) > 0:
        sock.connect((nb[0],1))

    aiy.audio.say("Set up Complete. Ready!")
    led.set_state(aiy.voicehat.LED.OFF)
    while True:

        text = recognizer.recognize()

        print (text)
        
        if text is None:
            print ("Nothing")
            led.set_state(aiy.voicehat.LED.OFF)
        else:
            if "hey little me" in text:
                it = time.time()
                done = False
                led.set_state(aiy.voicehat.LED.ON)

                while time.time() - it < 5 and not done:
                    text = recognizer.recognize()
                    print ("about to start")

                    if text is not None:
                        if "turn on the light" in text:
                            sock.send("A")
                            aiy.audio.say("done")
                            done = True
                        elif "turn off the light" in text:
                            sock.send("B")
                            aiy.audio.say("done")
                            done = True
                        else:
                            aiy.audio.say("commands not recognized")

if __name__ == '__main__':
    main()
