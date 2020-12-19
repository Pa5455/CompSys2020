#!/usr/bin/env python
from time import sleep

import Tank
volume_dosage = 0.5
pump_on_duration = volume_dosage / 0.0563                   #pump will pump 0.0563 litres per second

Tank.reading()                                              #takes an initial tank level reading
distance_before = Tank.reading()
volume_before = 10 - (distance_before * 0.3704)
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

    distance_after = Tank.reading()
    volume_after = 10 - (distance_after * 0.3704)
    volume_used = volume_before - volume_after
    volume_used = round(volume_used, 1) 
    

    print("Volume used",volume_used,"Litres")
    print("Volume remianing in tank", volume_after)





