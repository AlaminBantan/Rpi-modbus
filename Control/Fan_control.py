import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel = 2

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Suppress GPIO warnings
GPIO.setup(channel, GPIO.OUT)

def mist_off(pin):
    GPIO.output(pin, GPIO.HIGH)  

def mist_on(pin):
    GPIO.output(pin, GPIO.LOW)  

try:
    while True:
      
        # Get the current time
        current_time = datetime.now().time()

        # Define the start and end times
        start_time = time(6, 20, 45)
        end_time = time(18, 0)

        # Check if the current time is between 6:20 AM and 6:00 PM
        if start_time <= current_time <= end_time:
            print("The current time is between 6:00 AM and 6:00 PM.")
            print("fan is on")
            mist_on(channel)
            t.sleep(1140)
            print("turnoff")
            mist_off(channel)
            t.sleep(60)
        else:
            print("its night time, go and rest")
            mist_off(channel)
            t.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
