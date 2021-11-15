import paho.mqtt.client as mqtt
import time
import grovepi
import math
from grove_rgb_lcd import *


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("victoryi/alarm")
    client.message_callback_add("victoryi/alarm", alarm_callback)

    client.subscribe("victoryi/alert")
    client.message_callback_add("victoryi/alert", alert_callback)

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.playload, "utf-8"))

#callback for the alarm
def alarm_callback(client, userdata, msg):
    message = str(msg.payload, "utf-8")
    if(message == "Sound Alarm"):
        r_led = 8 #red led d8
        b_led = 7 #blue led d7
        buzz = 2 #buzzer d2
        grovepi.pinMode(r_led, "OUTPUT")
        grovepi.pinMode(b_led, "OUTPUT")
        for i in range(15):
            #BEEEEEEEEEE
            grovepi.digitalWrite(r_led,1)
            grovepi.digitalWrite(b_led,0)
            grovepi.digitalWrite(buzz,1)
            time.sleep(0.5)
            #BOOOOOOOOOO
            grovepi.digitalWrite(r_led,0)
            grovepi.digitalWrite(b_led,1)
            grovepi.digitalWrite(buzz,0)
            time.sleep(0.5)
        grovepi.digitalWrite(r_led,1)
        #alaram lights stay on after alarm

#callback for the alert
def alert_callback(client, userdata, msg):
    setRGB(255,0,0) 
    message = str(msg.payload, "utf-8")

    setText_norefresh(message)

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
   
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x01)
    setRGB(70,140,140) #random color

    button = 3 #port d3 used for the button
    ths = 4 #port d4 used for the temperature and humidity sensor
    blue = 0

    grovepi.pinMode(button, "INPUT")

    print("Beginning environmental detection")    

    while True:
        
        [temp,humidity] = grovepi.dht(ths,blue)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("Current temp = %.02f C Current humidity =%.02f%%"%(temp, humidity))

        #Ive added a button trigger to that we dont need to test it out with real fire
        if(grovepi.digitalRead(button) == 1) or ((temp > 40.00) and (humidity < 5.00)):
                client.publish("victoryi/alert", "RPI is hot, press to sound alarm")
        time.sleep(2) #2 second interval









