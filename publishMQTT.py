
import config
import state

import paho.mqtt.client


def publish(topic, payload):

    if (config.SWDEBUG):
        print("--->Sending MQTT Packet<---")
    # state.mqtt_client.publish("SkyWeather2", state.currentStateJSON)
    # state.mqtt_client.publish("SkyWeather2", state.StateJSON)
    state.mqtt_client.publish(topic, payload)


