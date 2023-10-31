import RPi.GPIO as GPIO
from datetime import datetime, time
import time as t
import threading

channel_14 = 14
channel_15 = 15
channel_18 = 18
channel_23 = 23
channel_24 = 24
channel_25 = 25

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_14, GPIO.OUT)
GPIO.setup(channel_15, GPIO.OUT)
GPIO.setup(channel_18, GPIO.OUT)
GPIO.setup(channel_23, GPIO.OUT)
GPIO.setup(channel_24, GPIO.OUT)
GPIO.setup(channel_25, GPIO.OUT)

def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def motor_on(pin):
    GPIO.output(pin, GPIO.LOW)

def motor_thread(pin, name):
    try:
        while True:
            print(f"Motor {name} is low")
            motor_on(pin)
            t.sleep(10)
            print(f"Motor {name} is high")
            motor_off(pin)
            t.sleep(10)
    except KeyboardInterrupt:
        GPIO.cleanup()

# Create threads for each motor
motor_14_thread = threading.Thread(target=motor_thread, args=(channel_14, "14"))
motor_15_thread = threading.Thread(target=motor_thread, args=(channel_15, "15"))
motor_18_thread = threading.Thread(target=motor_thread, args=(channel_18, "18"))
motor_23_thread = threading.Thread(target=motor_thread, args=(channel_23, "23"))
motor_24_thread = threading.Thread(target=motor_thread, args=(channel_24, "24"))
motor_25_thread = threading.Thread(target=motor_thread, args=(channel_25, "25"))

try:
    # Start the threads
    motor_14_thread.start()
    motor_15_thread.start()
    motor_18_thread.start()
    motor_23_thread.start()
    motor_24_thread.start()
    motor_25_thread.start()

    # Wait for all threads to finish
    motor_14_thread.join()
    motor_15_thread.join()
    motor_18_thread.join()
    motor_23_thread.join()
    motor_24_thread.join()
    motor_25_thread.join()

except KeyboardInterrupt:
    GPIO.cleanup()

