import RPi.GPIO as GPIO
import time
from datetime import datetime, time as dt_time

channel = 2 

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def relay1_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn relay on
    print(f"Relay {pin} ON")

def relay1_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn relay off
    print(f"Relay {pin} OFF")

try:
    # Define target times
    target_on_time = datetime.combine(datetime.today(), dt_time(16, 56))
    target_off_time = datetime.combine(datetime.today(), dt_time(16, 58))
    
    while True:
        current_time = datetime.now()
        
        if current_time >= target_on_time and current_time < target_off_time:
            relay1_on(channel)
        else:
            relay1_off(channel)
            
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
