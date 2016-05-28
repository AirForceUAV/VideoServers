import Queue
import threading
import time
import base64
import threading
import paho.mqtt.client as mqtt

ImagesQueue = Queue.Queue(5)
ClientNum = 0
def on_connect(client,userdata,rc):
    #print "Connected with result code" + str(rc)
    client.subscribe("Video")

def on_message(client ,userdata, msg):
    global ClientNum
    if ClientNum > 0 and msg.topic == "Video":
        ImagesQueue.put(base64.b64decode(str(msg.payload)))
    #print msg.topic + " " + str(msg.payload)

client = mqtt.Client(client_id = "VideoPlayer")
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1",1883,60)
#client.loop_start()
t = threading.Thread(target=client.loop_start)
t.start()

#class VideoStream(object):
#    def OnConnect(
#    def __init__(self):
#        self.images = Queue.Queue()
#        self.client = mqtt.Client()
#        self.on_connect(client,userdata,rc)
#        

