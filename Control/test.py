import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel_21 = 21 #change channel_21 based on relay

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_21, GPIO.OUT)

def pump_off(pin):
    GPIO.output(pin, GPIO.HIGH)  

def pump_on(pin):
    GPIO.output(pin, GPIO.LOW)  

try:
    while True:
            print("GPIO is low")
            pump_on(channel_21)
            t.sleep(5)
            print("GPIO is low")
            pump_off(channel_21)
            t.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
