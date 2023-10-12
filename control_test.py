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
        while True:
            current_time = time.localtime(time.time())
            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min

            if current_hour >= 6 and current_hour < 18:  # Changed to run from 6 am to 6 pm
                if current_minute < 30:
                    relay1_off(channel)
                    time.sleep(30)
                else:
                    relay1_on(channel)
                    time.sleep(60)
            else:
                relay1_on(channel)
                time.sleep(60)

    except KeyboardInterrupt:
        GPIO.cleanup()
