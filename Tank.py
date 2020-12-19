#!/usr/bin/env python

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library

GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
GPIO.setwarnings(False)                    #Get rid of pin allready in use error

TRIG = 17                                  #Associate pin 23 to TRIG for Sonar monitoring
ECHO = 22                                  #Associate pin 24 to ECHO for Sonar monitoring
Relay_pin = 27                             #Assosiate pin 27 for relay siganl (12V pump) 



print ("Distance measurement in progress") #just allowing time for sonar to settle

GPIO.setup(TRIG,GPIO.OUT)                  #Set Trig on sonar pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set ECHO on sonar pin as GPIO in
GPIO.setup(Relay_pin, GPIO.OUT, initial=GPIO.LOW) #Set relay pin as output, and initilise as low for off

def pump_on():                               #Function for activating relay, 12v pump on
    GPIO.output(Relay_pin, True)
    print ("pump is runing")

def pump_off():                              #Function for activating relay, 12v pump on
    GPIO.output(Relay_pin, False)
    print ("pump is off")

def reading():                               #Defining function to take sonar reading
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    time.sleep(2)                            #Delay of 2 seconds, allow to "settle"

    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance * 2)/2         #Round distance to nearest half centimeter
    if distance > 2 and distance < 28:       #Check whether the distance is within range
      return distance 
      

    else:
      pump_off()
      print ("Out Of Range")                   #display out of range


