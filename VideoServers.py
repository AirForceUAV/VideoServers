import Queue
import threading
import time
import base64
import paho.mqtt.client as mqtt

ImagesQueue = Queue.Queue()

def on_connect(client,userdata,rc):
    #print "Connected with result code" + str(rc)
    client.subscribe("Video")

def on_message(client ,userdata, msg):
    if msg.topic == "Video":
        ImagesQueue.put(base64.b64decode(str(msg.payload)))
    #print msg.topic + " " + str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1",1883,60)
client.loop_start()

