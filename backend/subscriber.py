import json

import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "smartclimate/+/readings"


def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to broker, code:", reason_code)
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"{msg.topic}: {data}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.loop_forever()


if __name__ == "__main__":
    main()
