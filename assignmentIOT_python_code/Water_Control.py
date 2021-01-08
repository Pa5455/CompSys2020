#!/usr/bin/env python

#This file is the sript for watering control
#From the glitch app, the user can click a button, 0.0, 0.5,1.0,1.5 and 2 litres
#This posts a http request to thingspeak channel. The GET URL below then looks for the the last entry,
#The last entry is what will be set as "volume_dosage" and will be the value used during the daily watering
#See MQTT_Thingspeak.py, this activates the watering function here in this file, and also see the link 
# #between the HTTP_request.py file also

from time import sleep
import requests
import Tank  #the volume readings in the tank are in here, as well as pump on and pump off commands

url='https://api.thingspeak.com/channels/1265472/fields/8/last.json?api_key41ZP4NVI87FRZA9D'  #this is used to get the voluem_dosage from the web app

def watering():
    response=requests.get(url)
    condition=response.json()['field8'] #a value is read from field 8 in thingspeak channel, which has been written to using a HTTP post via webapp
    volume_dosage=float(condition) #sting is converted to float for variabel to be used.
    print(condition)
    pump_on_duration = volume_dosage / 0.06                   #pump will pump 0.06 litres per second

    Tank.reading()                                              #takes an initial tank level reading
    volume_before = Tank.reading()
    vol_before_round = round(volume_before,1)

    if volume_before < .02:                                                      #if the tank level is empty a message
        print("Tank is Empty, fill it up")                                         
    elif volume_before < volume_dosage:                                            #else if the requested water dosage is greater than current tank volume, another message 
        print("There is not enough water in the tank for this water dosage, only", vol_before_round, "litres remaining")

    else:                                                           #when first 2 conditions of if statement are not true, then program continues
        Tank.pump_on()
        sleep(pump_on_duration)                                     #using sleep fuction from time to pass variable from pump_on_duratiom calc in line 6

        Tank.pump_off()                                             #pump turns off anf then the tank readings are taken again and volume used confirmed

        sleep(2)                                                    #get away from any interferance from pump operation

        volume_after = round(Tank.reading(),2)
        
        volume_used = volume_before - volume_after
        volume_used = round(volume_used, 2) 
       
        
        #print("Volume used",volume_used,"Litres")
        #print("Volume remaining in tank", volume_after,"Litres")


