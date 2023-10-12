import RPi.GPIO as GPIO
import time

channel = 2

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def mist_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn mist on

def mist_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn mist off

try:
    while True:
        current_time = time.localtime(time.time())
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        if (current_hour == 6 and current_minute >= 20) and (current_hour < 18 and current_minute >= 00):
            mist_on(channel)
            time.sleep(30)
            mist_off(channel)
            time.sleep(1170)
        else:
            mist_off(channel)
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
