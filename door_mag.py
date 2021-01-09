#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   

PIN = 24
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def door():
    while True:
        state = GPIO.input(PIN)
        return state

