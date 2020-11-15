# GreenHouse Automate
#### Student Name: *Patrick Curran*   Student ID: *05517834*

This project is to set up a smart polytunnel. Automation of plant watering and temp/humidity monitoring, adding camera functionality and giving user some data on plant growth vs. climatic conditions etc. 

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


