import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel_16 = 16 #change channel_16 based on relay

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_16, GPIO.OUT)

def pump_off(pin):
    GPIO.output(pin, GPIO.HIGH)  

def pump_on(pin):
    GPIO.output(pin, GPIO.LOW)  

try:
    while True:
            print("GPIO is low")
            pump_on(channel_16)
            t.sleep(5)
            print("GPIO is low")
            pump_off(channel_16)
            t.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
