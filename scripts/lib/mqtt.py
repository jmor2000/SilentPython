from lib.core import parent
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import queue
import time

G_q_msg = queue.Queue()
G_sub_items = []

#=================================================================
#=================================================================
#=================================================================
# The callback for when the client receives a CONNACK response from the server.
def callback_on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    global G_sub_items
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for ia in G_sub_items:
        client.subscribe(str(ia),1)

# The callback for when a PUBLISH message is received from the server.
def callback_on_message(client, userdata, msg):
    global G_q_msg
    G_q_msg.put(msg)

#=================================================================
#=================================================================
#=================================================================



class client(parent):
    def __init__(self):
        #-------inherit the methods and properties from its parent.
        super().__init__("This is a MQTT Client")
        #-------Set child properties
        self.connection = mqtt.Client

    #=================================================================[Connect to the database]
    def connect(self, address="", port=0):
        try:
            if self.error.value['state'] == False:           
                #...................................................
                #...................................................
                #...................................................              
                self.connection = mqtt.Client()
                self.connection.on_connect = callback_on_connect
                self.connection.on_message = callback_on_message
                self.connection.connect_async(address, port)
                #...................................................
                #...................................................
                #...................................................     
            self.error.clear()    
        except Exception as e: 
            self.error.set(True, "mqtt_connect: " + str(e), 0)

    def start(self, state=False):
        try:
            if self.error.value['state'] == False:  
                #...................................................
                #...................................................
                #...................................................           
                if state == True:
                    self.connection.loop_start()
                else:
                    self.connection.loop_stop
                time.sleep(1) #wait for connection
                #...................................................
                #...................................................
                #................................................... 
            self.error.clear()
        except Exception as e: 
            self.error.set(True, "mqtt_start: " + str(e), 0)

    def is_connected(self):
        try:
            #...................................................
            #...................................................
            #...................................................         
            mybool = self.connection.is_connected()
            return mybool
            #...................................................
            #...................................................
            #...................................................  
        except Exception as e: 
            self.error.set(True, "mqtt_isconnected: " + str(e), 0)

    #=================================================================[Connect to the database]
    def write(self, topic="", value=0.000):
        try:
            #...................................................
            #...................................................
            #...................................................     
            self.connection.publish(topic, value)
            print(f'....................MQTT Write :{topic}')
            #...................................................
            #...................................................
            #...................................................
            self.error.clear()
        except Exception as e: 
            self.error.set(True, "mqtt_write: " + str(e), 0)


