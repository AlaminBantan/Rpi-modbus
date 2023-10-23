import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel_16 = 16 #change channel_16 based on relay

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Suppress GPIO warnings
GPIO.setup(channel_16, GPIO.OUT)

def shade_ret_off(pin):
    GPIO.output(pin, GPIO.HIGH)  

def shade_ret_on(pin):
    GPIO.output(pin, GPIO.LOW)  

try:
    while True:
      
        # Get the current time
        current_time = datetime.now().time()

        # Define the start and end times
        start_time_shade_ret = time(1, 30)
        end_time_shade_ret = time(1, 33)

        # Check if the current time is between 1:30 AM and 1:33 AM:
        if start_time_shade_ret <= current_time <= end_time_shade_ret:
            print("The current time is 1:30, shades will be retracted now")
            print("shade is retracting now")
            shade_ret_on(channel_16)
            t.sleep(180)
        else:
            print("no change to shading now")
            shade_ret_off(channel_16)
            t.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
