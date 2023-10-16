import RPi.GPIO as GPIO
from datetime import datetime, time
import time

channel = 2

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def mist_on(pin):
    GPIO.output(pin, GPIO.HIGH)  

def mist_off(pin):
    GPIO.output(pin, GPIO.LOW)  

try:
    while True:
      
        # Get the current time
        current_time = datetime.now().time()

        # Define the start and end times
        start_time = datetime.time(6, 20)
        end_time = datetime.time(18, 0)

        # Check if the current time is between 6:20 AM and 6:00 PM
        if start_time <= current_time <= end_time:
            print("The current time is between 6:20 AM and 6:00 PM.")
            mist_on(channel)
            time.sleep(30)
            print("turnoff")
            mist_off(channel)
            time.sleep(1170)
        else:
            print("its night time to go and rest")
            mist_off(channel)
            time.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
