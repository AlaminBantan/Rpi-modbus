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

        # Calculate the time remaining until the first cycle at 6:20 am
        time_until_first_cycle = (6 - current_hour) * 60 + (20 - current_minute)
        if time_until_first_cycle > 0:
            print(f"Waiting for {time_until_first_cycle} minutes until the first cycle starts.")
            time.sleep(time_until_first_cycle * 60)

        while True:
            current_time = time.localtime(time.time())
            current_hour = current_time.tm_hour

            if current_hour >= 6 and current_hour < 18:  # Changed to run from 6 am to 6 pm
                relay1_off(channel)
                time.sleep(30)
                relay1_on(channel)
                time.sleep(1170)
            else:
                relay1_on(channel)
                time.sleep(1170)

    except KeyboardInterrupt:
        GPIO.cleanup()
