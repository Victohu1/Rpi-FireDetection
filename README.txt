Simple Fire detector and Receiver using MQTT standard for IoT messaging

Instructions to compile/ execute: On the rpi that would be responsible for fire detection, please attach a red and blue led, a temperature and humidity sensor, and a buzzer. 
On the rpi that would be responsible for the fire montior, please attach a lcd screen, and a button. Once those are completed. Simply run "python3 rpi_detector.py" on the detector,
and "python3 rpi_montior.py" on the monitor. 
Furthermore, please install the MQTT and Twilio dependencies. If you don't already have them, open your terminal and write the following commands: 
	pip3 install twilio
	pip3 install paho-mqtt
	pip3 install pynput 
	(if you don't have pip3): sudo apt install python3-pip
	
External libraries used: 
paho-mqtt, twilio 


