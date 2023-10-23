import RPi.GPIO as GPIO
import time

# Define the GPIO pins for each motor
channels = [21, 20, 16, 26]

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channels, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on

def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off

    
if __name__ == '__main__':
    try:
        while True:

            motor_on(21)
            time.sleep(5)
            motor_off(21)
            time.sleep(5)

            motor_on(20)
            time.sleep(4)
            motor_off(20)
            time.sleep(4)

            motor_on(16)
            time.sleep(4)
            motor_off(16)
            time.sleep(4)

            motor_on(26)
            time.sleep(4)
            motor_off(26)
            time.sleep(4)


    except KeyboardInterrupt:
        GPIO.cleanup()
