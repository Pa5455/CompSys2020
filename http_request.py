#brings in the autmation of watering. In things speak there is a time control set up to get a tackback command
#This talkback command is modified using a put command in thingHTTP and timecontrol
#ThingHTTP will use a PUT command to change the command string form ON to OFF for a period no longer than 1 minute each day
#This ensures that the while loop below will catch the pump on command (takes just under a minute to get through it).  

import requests
import json
import Water_Control 
url=('https://api.thingspeak.com/talkbacks/41293/commands/21323878.json?api_key=6L0X6KJT5USPJSP8')



def auto_water():
    response=requests.get(url)
    condition=response.json()['command_string']
    if condition == 'ON':                                       #When on condition is met, the function watering in fiel WAter_Control is run
        print(condition + " HTTP respose for Auto_watering")
        Water_Control.watering()   
    else:
        print(condition + " HTTP respose for Auto_watering")
        exit
       


