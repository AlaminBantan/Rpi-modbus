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


if __name__ == '__main__':
    try:
        relay1_on(channel)
        time.sleep(1)
        relay1_off(channel)
        time.sleep(4)
        relay1_on(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()