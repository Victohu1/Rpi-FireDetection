"""EE 250L Lab 04 Starter Code

Run vm_subscriber.py in a separate terminal on your VM."""

"""
Name: Victor Hui (Worked alone)
github repo: https://github.com/usc-ee250-spring2021/lab05-victoryi.git
"""

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("victoryi/ultrasonicRanger")
    client.message_callback_add("victoryi/ultrasonicRanger", cus_callback)

    client.subscribe("victoryi/button")
    client.message_callback_add("victoryi/button",button_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def cus_callback(client, userdata, msg):
    #print("Received a message on:", msg.topic, "therefore running cus_callback")
    print("VM:[" + str(msg.payload,"utf-8") + "] cm")

def button_callback(client, userdata, msg):
    print(str(msg.payload,"utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        #print("delete this line")
        time.sleep(1)
            

