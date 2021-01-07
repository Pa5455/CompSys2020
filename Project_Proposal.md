# GreenHouse Automate
#### Student Name: *Patrick Curran*   Student ID: *05517834*

This project is to set up a smart polytunnel. Automation of plant watering and temp/humidity monitoring, adding camera functionality and giving user some data on plant growth vs. climatic conditions etc. 

Rescoped project from original proposal:

Camera functionality to take a period snap shot, store shot in firebase database, inlcude a reference object in background. This database of images can then be accessed at anytime and used for postprocess analysis, such as comparing temp trends and growth rate and may watering amounts. As a cool side effect a time lapse could be made filtering out a selecting of images. ALso my web app will take the latest snapshot from firebase and display it on screen.

Auto_Watering as planned, user can specify what the dialy water dosage is to be via web app, they select 0 if they want it to be off, and then 0.5 incements up to 2 litres. The frequency of watering is set in Thingspeak time control. Water level in tank is also displayed on web app (MQTT to thingsspeak and then iframe HTML elememt taken from things speak to web app. The daily ammount set is done via html button sending a channel update in thingsspeak. The raspberry pi then requests a get url from the thingspeak channel fiels taking the last entry and passsing it into the watering function. The watering will now use a 12V pump activated by a 12V relay normaly open. Conditions set in teh python software will not allow the pump to be activted if tank is empty, and also the user gets a tweet when level is getting low. In the python code. The tank is a drim sored inside the poly tunnel, as the water can naturally be warmed up creating less shock. 

Some research on Tomatoe growing conditions, found that a Vapor Presure decifit of 0.9 to 1.2 kPA was ideal growing conditions. A calculation channel using MATLAB analysis in thingsspeak can run a calculation based on temp and humidity to give the vapor pressure decifit output in Pa. The user will be notified when outside this range and can then go and act to remidy this.

There is automatic vent control, a servo is actiaved and when above a temperature threshold. Python code looks after the automation, but thingspeak does monitor if vent is open or closed (via MQTT). If temp goes further beyond threshold user gets an alert and then can take further action, maybe a mist or big fan.

Door state is monitored by push button, if the button is activated (pushed by door) then a signal is sent with the door state, the user can see this on the web app or in the things speak channels. If the door is open an alert is also sent to the user, which they can ignore if they actually have opened the door.

Arduino not used as not neccessary. I have not included scraping weather data. The data collected can be used in a database for following year, so maybe water ammount required can be estimated.

Python used on PI, javascript, html and css used in web app and data stored in Database


I am leaving the scope open slightly as to how far I can push up the grading spectrum, with the 5 points below I can easily work form baseline to excellent/outstanding, which is how I am going to approach this assignment, once I have a good mark I can push it on more, and have all iterations saved in GIT repo. 

1) Water will come from a rain barrel, syphoned into the polytunnel water distribution system. A sensor in the rain barrel will show how much water is present in barrel. A simple relay valve will control the water flow, on or off. The duration of the valve opening time will depend on the volume of water in the barrel, as less volume is expected to come out when water is at low levels, this can be calibrated and either fed back to IOT platform such as ThingSpeak to run calculation on how long the relay valve should be left open, or else run it in code. I will avoid using moisture sensors as want to keep wires in ground to a minimum. (Future proofing for my automatic weeding robot!)

2) Temperature and humidity, an important feature here is to minimise high levels of humidity in the polytunnel to avoid fungus growing on leaves etc, again ThingSpeak can be used to run calculation and alert owner, and/or open vent/turn on fan to take humidity out of the air. This would be similar to the dew point calc in the Labs. 

3) Camera will be used for a couple of purposes, one to document the growing season, maybe in a time-lapse fashion. Maybe a weekly photo fed into a data base to show progress(or lack of)and select images to web site or app. It can also be a good way to maybe live stream the watering process so that the customer can double check even distribution at their discretion, so choice of live feed or recording during watering process.  As a way of adding some more complexity, the camera could monitor plant leaf colour (yellow bad, green good, green to blue not good etc), it could monitor plant height and alert customer to maybe perform an action such as prune plants or maybe plants are ready for a particular type of fertiliser. Recognise weeds and alert user to act. Images sent to personal PC with more processing power if the PI cannot handle it.

4) Leaving a door open by mistake is not a good idea for a poly tunnel, especially in wind, accelerometer to monitor movement on door, or a contactor to alert owner if door is not closed and no person is detected in polytunnel. automatic on of radio when enter the polytunnel as an extra feature. 

5) Web application to monitor parameters, and maybe perform manual control if needed. Maybe pull weather data from internet to predict when vents should be open etc, rain fall from previous years vs. amount of water needed for summer, buffer tank requirements to avoid using tap water. Wind direction information to be careful which side vent opens etc.. 

With all the above, I have enough to go at, using Networking module for communication, web dev/ICT skills to make a web application/web site and obviously programming. 

## Tools, Technologies and Equipment

Hardware:
Raspberry PI, Arduino I have lying around, look into USB C power bank with power delivery. Researching into use of MQTT for sensor data using a ESP32 module, (low power usage can just charge up once per week maybe)

The raspberry PI will act as a server and the Arduino as a client, MQTT possible communication for sensor data from Arduino to PI. I need to figure out how to get the camera data. Maybe not use Arduino at all and go with a PI with GPIO, and a second pi at in house to communicate to the PI in the polytunnel, maybe make an IOT network, I don’t think my home Wi-Fi will make it to the polytunnel, Some further research here/shopping to do but the general concept is there. If all else fails I might use a hardwire LAN across the garden!

Ultrasonic sensor for water level monitor, valve relay (operated with 3v or 5v will be ok as only blocking a syphon so not massive power needed). Humidity and temperature sensors. Depending on time I might only simulate opening a vent by flashing a light instead, or raising a flag with a servo motor. 

Thingspeak as IOT platform (will investigate others but this seems to be good enough. 

Python as hard coding language for Arduino etc.  JavaScript for web site, use of glitch if can get to revisit the ICT labs.

## Project Repository
Pa5455/CompSys2020/Project_Proposal.md


