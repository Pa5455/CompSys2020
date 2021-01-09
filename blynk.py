#!/usr/bin/env python
import blynklib
from time import sleep
from Tank import reading
from Water_Control import watering

from temp_hum import environment_temp
from temp_hum import environment_humid



BLYNK_AUTH = 'k42BhIAhtEv6i2AYOFSNDg3r_LhO5Chb'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)



# register handler for virtual pin V1(volume) reading
@blynk.handle_event('read V1')
def read_virtual_pin_handler(pin):
        volume=reading()
        #print('V1 Read:' + str(volume), 'Litres')  # print volume to console
        blynk.virtual_write(pin,volume)

@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin1):
        temp=environment_temp()
        #print('V2 Read:' + str(temp), 'Degrees C')  # print temperature to console
        blynk.virtual_write(pin1,temp)

@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin3):
        humid=environment_humid()
        #print('V3 Read:' + str(humid), 'Humidity')  # print humidity to console
        blynk.virtual_write(pin3,humid)

@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print('V4:'+ str(value))
    volume_dosage=int(value[0])
    watering(volume_dosage)

while True:
        blynk.run()