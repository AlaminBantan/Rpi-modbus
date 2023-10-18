import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel = 2 #change channel based on relay

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
        start_time_m = time(6, 20)
        morning_time_m = time(10,0)
        end_time_m = time(18, 0)

        # Check if the current time is between 6:20 AM and 6:00 PM
        if start_time_m <= current_time <= morning_time_m:
            print("The current time is between 6:20 AM and 10:00 AM.")
            print("mist is on")
            mist_on(channel)
            t.sleep(30)
            print("turnoff")
            mist_off(channel)
            t.sleep(1170)
        elif morning_time_m <= current_time <= end_time_m:
            print("The current time is between 10:00 AM and 6:00 PM.")
            print("mist is on")
            mist_on(channel)
            t.sleep(30)
            print("turnoff")
            mist_off(channel)
            t.sleep(1770)            
        else:
            print("Its night time to go and rest")
            mist_off(channel)
            t.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
