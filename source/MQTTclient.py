from utils.imports import *
from utils.utils import utils

class mqttclient():
    def __init__(self) -> None:
        self.client = mqtt.Client() 
        self.client.connect("broker.emqx.io", 1883, 60) 
        self.client.on_connect('righthand/input')
        self.client.on_connect('lefthand/input')
        self.client.loop_forever()
        pass

    def on_connect(self, userdata, topic : str, flags, rc):
        print(f"Connected with result code {rc}")
        self.client.subscribe(topic)

    def publish(self, topic : str, message : str):
        try:
            self.client.publish(topic, payload=message, qos=0, retain=False)
            return True
        except:
            return False
        
    def on_message(self, client, userdata, msg):
        message = msg.payload
        topic = msg.topic
        