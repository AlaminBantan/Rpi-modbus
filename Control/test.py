import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel_13 = 21 #change channel_13 based on relay

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_13, GPIO.OUT)

def pump_off(pin):
    GPIO.output(pin, GPIO.HIGH)  

def pump_on(pin):
    GPIO.output(pin, GPIO.LOW)  

try:
    while True:
      
        # Get the current time
        current_time = datetime.now().time()

        # Define the start and end times
        start_time_pump = time(6, 00)
        end_time_pump = time(18, 00)

        # Check if the current time is between 6:00 AM and 6:00 PM:
        if start_time_pump <= current_time <= end_time_pump:
            print("The current time is between 6 AM and 6 PM")
            print("Fan in zone C is on now")
            pump_on(channel_13)
            t.sleep(180)
        else:
            print("no change to shading now")
            pump_off(channel_13)
            t.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
