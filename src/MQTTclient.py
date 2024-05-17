from utils.imports import *
from utils.utils import utils
from SensorManager import SensorManager

class mqttclient():
    def __init__(self) -> None:
        u = utils()
        self.sm1 = SensorManager()
        self.sm2 = SensorManager()
        print(u.get_ip())

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
        topic = msg.topic
        if topic == "righthand/input":
            self.publish("server/callback", f"rcvd R") 
            data = self.sm1.interpreteMotion(msg.message)
            requests.post("http://localhost:8000/post_right", data)
        elif topic == "lefthand/input":
            self.publish("server/callback", f"rcvd L") 
            data = self.sm2.interpreteMotion(msg.message)
            requests.post("http://localhost:8000/post_left", data)
        
        self.publish("server/interp", f"data : {data}") 