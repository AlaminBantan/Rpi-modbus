import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t
import threading

channel_16 = 16
channel_14 = 14
channel_15 = 15

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_16, GPIO.OUT)
GPIO.setup(channel_14, GPIO.OUT)
GPIO.setup(channel_15, GPIO.OUT)

def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def motor_on(pin):
    GPIO.output(pin, GPIO.LOW)

def motor_thread(pin, name):
    try:
        while True:
            print(f"Motor {name} is low")
            motor_on(pin)
            t.sleep(5)
            print(f"Motor {name} is high")
            motor_off(pin)
            t.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()

# Create threads for each motor
motor_14_thread = threading.Thread(target=motor_thread, args=(channel_14, "14"))
motor_15_thread = threading.Thread(target=motor_thread, args=(channel_15, "15"))
motor_16_thread = threading.Thread(target=motor_thread, args=(channel_16, "16"))

try:
    # Start the threads
    motor_14_thread.start()
    motor_15_thread.start()
    motor_16_thread.start()

    # Wait for all threads to finish
    motor_14_thread.join()
    motor_15_thread.join()
    motor_16_thread.join()

except KeyboardInterrupt:
    GPIO.cleanup()
