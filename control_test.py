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

        if (current_hour == 11 and current_minute > 4) and (current_hour < 18 and current_minute >= 00):
            relay1_off(channel)
            time.sleep(30)
            relay1_on(channel)
            time.sleep(1170)
        else:
            relay1_on(channel)
            time.sleep(1170)

except KeyboardInterrupt:
    GPIO.cleanup()
