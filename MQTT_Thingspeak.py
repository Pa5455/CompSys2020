#This is the main python script which runs the monitoring system
#It  publishes to MQTT things speak channel using paho mqtt client
#Also it brings in the autmation of watering. In things speak there is a time control set up to get a tackback command
#This talkback command can be used then in the HTTP_request.py when calling watering fuction
#ThingHTTP will use a PUT command to change the command string for a period no longer than 1 minute each day
#This ensures that the while loop below will catch the pump on command (takes just under a minute to get through it)



import paho.mqtt.client as mqtt
from temp_hum import environment_temp 
from temp_hum import environment_humid 
from Tank import reading
import door_mag
import vent
import time
import http_request
from Tomato_smile import cam

client = mqtt.Client()
client.connect("mqtt.thingspeak.com",1883,80)

channelID = "1265472"
apiKey = "K89UM98Z1CQD03BA"

def writeData(temperature,humidity,Water_level,door_mag,vent_pos):   #this fuction takes in the parameters that are to be written to thingspeak in teh cloud (field5 is already used as a calcualtion channel)
    client.publish("channels/%s/publish/%s" % (channelID,apiKey), 'field1=%s&field2=%s&field3=%s&field4=%s&field6=%s' % (temperature,humidity,Water_level,door_mag,vent_pos,))
    

while True:                       #this while loop will cycle through, takes just under a minute to get through the variuos functions
    temp=environment_temp()       # calls up the temperature  sensor reading
    humid=environment_humid()     #calls up the humidity sensor reading
    level=reading()               #calls up the return value of voluem in tank from function reading in Tank.py
    door_state=door_mag.door()    #checks the door fucntion in door mag py field. Was originall a magnet but changed it to a push button
    vent_condition=vent.auto_vent() #checks if vent is open or closed based on last servo position
    writeData(temp,humid,level,door_state,vent_condition) #writes into the writeData for the MQTT publish
    time.sleep(10)
    http_request.auto_water()      #calling function auto_water in http_request py file, if condion on is met, then the watering takes place, with the last requested ammount
    cam()                      #taking a picture and sending to firebase database, which shows up on the web app
    #time.sleep(10)                  
    
  
 
