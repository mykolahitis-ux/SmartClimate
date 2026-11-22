import json
import time

import config
import sensors
from umqtt.simple import MQTTClient


def main():
    client = MQTTClient(config.MQTT_CLIENT_ID, config.MQTT_BROKER,
                        port=config.MQTT_PORT, ssl=True)
    client.connect()

    while True:
        payload = json.dumps(sensors.read_all())
        client.publish(config.MQTT_TOPIC, payload)
        time.sleep(config.PUBLISH_INTERVAL_SEC)


if __name__ == "__main__":
    main()
