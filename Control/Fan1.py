import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t

channel_21 = 21 #change channel_21 based on relay

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Suppress GPIO warnings
GPIO.setup(channel_21, GPIO.OUT)

def fan1_off(pin):
    GPIO.output(pin, GPIO.HIGH)  

def fan1_on(pin):
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
            print("fan1 is on")
            fan1_on(channel_21)
            t.sleep(1140)
            print("fan1 is off")
            fan1_off(channel_21)
            t.sleep(60)
        elif morning_time_f1 <= current_time <= end_time_f1:
            print("The current time is between 10:00 AM and 6:00 PM.")
            print("fan1 is off")
            fan1_off(channel_21)
            t.sleep(60)
            print("fan1 is on")
            fan1_on(channel_21)
            t.sleep(1740)

        else:
            print("its night time, go and rest")
            fan1_off(channel_21)
            t.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
