#!/usr/bin/env python

#Tank has 3 functions, turn on pump, turn off pump and also to take reading of volume in tank using sonar sensor
#Safety features built in, if tank is empty or does not have enogh water for requested dosage volume then will not turn on pump
#pump is a 12v pump which is activated with a NO relay by pin 27 on pi
#Works really well, as a backup the user gets a tweat when tank is near low.



import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
GPIO.setwarnings(False)                    #Get rid of pin allready in use error

TRIG = 17                                  #Associate pin 23 to TRIG for Sonar monitoring
ECHO = 22                                  #Associate pin 24 to ECHO for Sonar monitoring
Relay_pin = 27                             #Assosiate pin 27 for relay siganl (12V pump) 

GPIO.setup(TRIG,GPIO.OUT)                  #Set Trig on sonar pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set ECHO on sonar pin as GPIO in
GPIO.setup(Relay_pin, GPIO.OUT, initial=GPIO.LOW) #Set relay pin as output, and initilise as low for off

def pump_on():                              #Function for activating relay, 12v pump on
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
      volume = 10 - (distance * 0.3704)        #Volume is calculated from 10 litre container minus empty space calibrtaed to 0.3704 litres per centimeter
      if volume > 0.01 and volume < 10:         #Check whether the volume is within range
         volume=round(volume,2)
         return volume
    
      else:
        pump_off()                             #should override any pump on command and make sure its off
        print ("Out Of Range")                 #display out of range


 









