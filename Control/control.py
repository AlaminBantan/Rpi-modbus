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
        current_time = time.localtime(time.time())
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec

        if (current_hour == 6 and current_minute >= 00 and current_second >= 45) and (current_hour < 18):
            relay1_off(channel)
            time.sleep(10)
            relay1_on(channel)
            time.sleep(10)
        else:
            relay1_on(channel)
            time.sleep(1)           
except KeyboardInterrupt:
    GPIO.cleanup()