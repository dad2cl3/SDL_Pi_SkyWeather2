#!/usr/bin/env python3

# SwithchDoc Labs September 2018
# Public Domain


from __future__ import print_function
from builtins import str
import sys

sys.path.append('./SDL_Pi_HM3301')
import time
import pigpio
import SDL_Pi_HM3301

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

import config
import datetime, json, publishMQTT
<<<<<<< HEAD

SENSOR_NAME = 'Laser PM2.5 Dust Sensor (HM3301)'
SENSOR_CHANNEL = 20
=======

SENSOR_NAME = 'Laser PM2.5 Dust Sensor (HM3301)'
SENSOR_CHANNEL = 20

>>>>>>> e8dc3a67df731bed2a80ef59a9d875c1e3c7ac95
# print("config.DustSensorSCL=", config.DustSensorSCL)
# print("config.DustSensorSDA=", config.DustSensorSDA)

import state

GPIO.setup(config.DustSensorPowerPin, GPIO.OUT)
GPIO.output(config.DustSensorPowerPin, True)


def powerOnDustSensor():
    GPIO.setup(config.DustSensorPowerPin, GPIO.OUT)
    GPIO.output(config.DustSensorPowerPin, False)
    GPIO.output(config.DustSensorPowerPin, True)
    time.sleep(1)


def powerOffDustSensor():
    GPIO.setup(config.DustSensorPowerPin, GPIO.OUT)
    GPIO.output(config.DustSensorPowerPin, True)
    GPIO.output(config.DustSensorPowerPin, False)
    time.sleep(1)


myPi = pigpio.pi()

try:
    hm3301 = SDL_Pi_HM3301.SDL_Pi_HM3301(
        SDA=config.DustSensorSDA,
        SCL=config.DustSensorSCL,
        pi=myPi)
except:
    myPi.bb_i2c_close(config.DustSensorSDA)
    myPi.stop()

    hm3301 = SDL_Pi_HM3301.SDL_Pi_HM3301(
        SDA=config.DustSensorSDA,
        SCL=config.DustSensorSCL,
        pi=myPi)


def read_AQI():
<<<<<<< HEAD
    print('Inside dust sensor...')
    if (config.SWDEBUG):
        print('###############')
        print("Reading AQI")
        print('###############')
=======
    if (config.SWDEBUG):
        print("###############")
        print("Reading AQI")
        print("###############")
>>>>>>> e8dc3a67df731bed2a80ef59a9d875c1e3c7ac95

    if (config.SWDEBUG):
        print("Turning Dust Power On")
    powerOnDustSensor()

    # delay for 30 seconds for calibrated reading
<<<<<<< HEAD

    time.sleep(30)
    time.sleep(0.1)

    myData = hm3301.get_data()
=======
    time.sleep(30)
    time.sleep(0.1)

    try:
        myData = hm3301.get_data()
    except Exception as e:
        print('=================================')
        print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
        print(e)
        print('=================================')
        return 0

>>>>>>> e8dc3a67df731bed2a80ef59a9d875c1e3c7ac95
    if (config.SWDEBUG):
        print("data=", myData)
    if (hm3301.checksum() != True):
        if (config.SWDEBUG):
            print("Checksum Error!")
        myData = hm3301.get_data()
        if (hm3301.checksum() != True):
            if (config.SWDEBUG):
<<<<<<< HEAD
                print("2 Checksum Errors!")
                return 0

=======
                reading = {
                    "time": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z'),
                    "model": SENSOR_NAME,
                    "channel": SENSOR_CHANNEL
                }
                publishMQTT.publish('ws/mallory/airquality/telemetry/', json.dumps(reading))
                print("2 Checksum Errors!")
                return 0

    # successful reading
>>>>>>> e8dc3a67df731bed2a80ef59a9d875c1e3c7ac95
    myAQI = hm3301.get_aqi()
    if (config.SWDEBUG):
        hm3301.print_data()
        print("AQI=", myAQI)

    # hm3301.close()
    powerOffDustSensor()
<<<<<<< HEAD

    state.AQI = myAQI

    reading = {
        "time": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z'),
        "model": SENSOR_NAME,
        "channel": SENSOR_CHANNEL,
        "reading": {
            "value": myAQI,
            "units": "AQI"
        }
    }

=======
    state.AQI = myAQI

    reading = {
        "time": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z'),
        "model": SENSOR_NAME,
        "channel": SENSOR_CHANNEL,
        "reading": {
            "value": myAQI,
            "units": "AQI"
        }
    }

>>>>>>> e8dc3a67df731bed2a80ef59a9d875c1e3c7ac95
    publishMQTT.publish('ws/mallory/airquality/telemetry/', json.dumps(reading))


def print_data():
    hm3301.print_data()


def get_aqi():
    myAQI = hm3301.get_aqi()
    return myAQI


def get_data():
    myData = hm3301.get_data()
    return myData
