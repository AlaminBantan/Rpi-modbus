import RPi.GPIO as GPIO
import time

channel = 2

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def relay1_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn relay1 on

def relay1_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn relay1 off
try:
    while True:     
            relay1_off(channel)
            time.sleep(10)
            relay1_on(channel)
            time.sleep(10)           
except KeyboardInterrupt:
    GPIO.cleanup()