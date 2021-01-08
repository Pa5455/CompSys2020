#!/usr/bin/python3

from urllib.request import urlopen
import  json
import  time
from temp_hum import environment_temp 
from temp_hum import environment_humid 
from Tank import reading
import door_mag

WRITE_API_KEY='K89UM98Z1CQD03BA'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY



def writeData(temperature,humidity,Water_level,door_mag):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s' % (temperature,humidity,Water_level,door_mag))
    # Closing the connection
    conn.close()

while True:
    temp=environment_temp()
    humid=environment_humid()
    level=reading()
    door_state=door_mag.door()
    time.sleep(5)
    writeData(temp,humid,level,door_state)
    time.sleep(60)