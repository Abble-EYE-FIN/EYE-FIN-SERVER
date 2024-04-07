import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    # Send a message to the raspberry/topic every 1 second, 5 times in a row
    for i in range(5):
        # The four parameters are topic, sending content, QoS and whether retaining the message respectively
        client.publish('righthand/input', payload=i, qos=0, retain=False)
        print(f"send {i} to righthand/input")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()