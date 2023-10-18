import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel = 2 #change channel based on relay

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Suppress GPIO warnings
GPIO.setup(channel, GPIO.OUT)

def fan_off(pin):
    GPIO.output(pin, GPIO.HIGH)  

def fan_on(pin):
    GPIO.output(pin, GPIO.LOW)  

try:
    while True:
      
        # Get the current time
        current_time = datetime.now().time()

        # Define the start and end times
        start_time_f1 = time(6, 0, 45)
        morning_time_f1 = time(9,59,45)
        end_time_f1 = time(18, 0)

        # Check if the current time is between 6:00:45 AM and 6:00 PM
        if start_time_f1 <= current_time <= morning_time_f1:
            print("The current time is between 6:00 AM and 10:00 PM.")
            print("fan is on")
            fan_on(channel)
            t.sleep(1140)
            print("fan is off")
            fan_off(channel)
            t.sleep(60)
        elif morning_time_f1 <= current_time <= end_time_f1:
            print("The current time is between 10:00 AM and 6:00 PM.")
            print("fan is off")
            fan_off(channel)
            t.sleep(60)
            print("fan is on")
            fan_on(channel)
            t.sleep(1740)

        else:
            print("its night time, go and rest")
            fan_off(channel)
            t.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
