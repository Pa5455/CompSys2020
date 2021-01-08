#!/usr/bin/env python

#This a file used to return temperateu and humidy values from a DHT11 temp humidy sensor, I created 2 fuctions to make
# it easier to take them individually
import Adafruit_DHT
import time




sensor_name=Adafruit_DHT.DHT11 # initiating the DHTt sensor
sensor_pin = 23

def environment_temp():
    while True:
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
            return temperature
            #time.sleep(2)

        except RuntimeError as error:
         pass
        time.sleep(2)

def environment_humid():
    while True:
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
            return humidity 
            #time.sleep(2)

        except RuntimeError as error:
         pass
        time.sleep(2)



