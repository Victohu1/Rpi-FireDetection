import paho.mqtt.client as mqtt
import time
import grovepi
import math
import twilio
from twilio.rest import Client
from grove_rgb_lcd import *

first_time = True

def on_connect(client, userdata, flags, rc):
    print("Connected to server with result code " + str(rc))
    #subscribe to the alert
    client.subscribe("victoryi/alert")
    client.message_callback_add("victoryi/alert", alert_callback)

#Default message callback
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

#callback for the alert
def alert_callback(client, userdata, msg):
    setRGB(255,0,0)
    message = str(msg.payload, "utf-8")
    setText_norefresh(message)
    global first_time
    if(first_time):
        msg_client = Client("AC3198ab6982d097e6683bfd810ddb1fb7", "cc3bf141d6bf8278f00d5d911ad42582")
        msg_client.messages.create(to="+16025712781", from_="+14243810367", body="Rasberry PI at eclipse.usc.edu:11000 is on fire!")
        first_time = False
        
if __name__ == '__main__':

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x01)
    setRGB(70,140,140)
    button = 3 #port d3 used for the button
    notNotified = True

    while True:
        if(grovepi.digitalRead(button) == 1):
            print("SOUNDING ALARM")
            client.publish("victoryi/alarm", "Sound Alarm")
        time.sleep(1)
