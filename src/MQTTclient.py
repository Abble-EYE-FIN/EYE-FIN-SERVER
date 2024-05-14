from utils.imports import *
from utils.utils import utils

class mqttclient():
    def __init__(self) -> None:
        util = utils()
        print(util.get_ip())
        self.client = mqtt.Client("server_pubs") 
        
        self.client.on_connect = self.on_connect 
        self.client.on_message = self.on_message
        
        self.client.will_set('server/status', b'{"status": "Off"}')
        
        self.client.connect("localhost", 1883, 60) 
        self.client.loop_forever()

    def on_connect(self, client, userdata : str, flags, rc):
        print(f"Connected with result code {rc}")
        self.client.subscribe('righthand/input')
        self.client.subscribe('lefthand/input')

    def publish(self, topic : str, message : str):
        try:
            self.client.publish(topic, payload=message, qos=0, retain=False)
            return True
        except:
            return False
        
    def on_message(self, client, userdata, msg):
        message = msg.payload
        topic = msg.topic
        print("topic : ", topic)
        print("message : ", message)
        
        self.publish("server/response", f"rcv {message}") 