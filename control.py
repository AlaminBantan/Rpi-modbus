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
        current_time = time.localtime(time.time())
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        if not (current_hour == 17 and current_minute >= 11 and current_minute <= 13):
            relay1_on(channel)

        while True:
            time.sleep(60)  # Check time every minute

            current_time = time.localtime(time.time())
            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min

            if current_hour == 17 and current_minute >= 11 and current_minute <= 13:
                relay1_off(channel)
            else:
                relay1_on(channel)

    except KeyboardInterrupt:
        GPIO.cleanup()
