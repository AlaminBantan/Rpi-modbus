import RPi.GPIO as GPIO
from datetime import datetime, time
import threading
import time as t

# Define GPIO channels
channel_mist = 26
channel_fan1 = 21
channel_fan2 = 20
channel_pump = 13
channel_shade_ex = 19
channel_shade_ret = 16

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel_mist, GPIO.OUT)
GPIO.setup(channel_fan1, GPIO.OUT)
GPIO.setup(channel_fan2, GPIO.OUT)
GPIO.setup(channel_pump, GPIO.OUT)
GPIO.setup(channel_shade_ex, GPIO.OUT)
GPIO.setup(channel_shade_ret, GPIO.OUT)

# Define functions for each device
def mist_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def mist_on(pin):
    GPIO.output(pin, GPIO.LOW)

def fan1_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def fan1_on(pin):
    GPIO.output(pin, GPIO.LOW)

def fan2_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def fan2_on(pin):
    GPIO.output(pin, GPIO.LOW)

def pump_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def pump_on(pin):
    GPIO.output(pin, GPIO.LOW)

def shade_ex_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def shade_ex_on(pin):
    GPIO.output(pin, GPIO.LOW)

def shade_ret_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def shade_ret_on(pin):
    GPIO.output(pin, GPIO.LOW)

# Define functions to control devices in threads
def mist_thread():
    while True:
        current_time = datetime.now().time()

        if (time(8, 0) <= current_time <= time(16, 0)):
            print("mist is on")
            mist_on(channel_mist)
            t.sleep(8)
            print("mist is off")
            mist_off(channel_mist)
            t.sleep(1432)
        else:
            mist_off(channel_mist)

def fan1_thread():
    while True:
        current_time = datetime.now().time()

        if (time(6, 0) <= current_time <= time(7, 59, 49)) or ((time(16, 0) <= current_time <= time(18,0))):
            fan1_on(channel_fan1)
        elif (time(7,59,50) <= current_time <= time(16,0)):
            print("The current time is between 8:00 AM and 16:00 AM.")
            print("mist is on, fan 1 is off")
            fan1_off(channel_fan1)
            t.sleep(30)
            print("mist is off, fan 1 is on")
            fan1_on(channel_fan1)
            t.sleep(1410)
        else:
            fan1_off(channel_fan1)

def fan2_thread():
    while True:
        current_time = datetime.now().time()

        if (time(6, 0) <= current_time <= time(7, 59, 49)) or ((time(16, 0) <= current_time <= time(18,0))):
            fan2_on(channel_fan2)
        elif (time(7,59,55) <= current_time <= time(16,0)):
            print("mist is on, fan 2 is off")
            fan2_off(channel_fan2)
            t.sleep(30)
            print("mist is off, fan 2 is on")
            fan2_on(channel_fan2)
            t.sleep(1410)
        else:
            fan2_off(channel_fan2)

def pump_thread():
    while True:
        current_time = datetime.now().time()

        if time(6, 0) <= current_time <= time(18, 0):
            pump_on(channel_pump)
        else:
            pump_off(channel_pump)

def shade_ex_thread():
    while True:
        current_time = datetime.now().time()

        if time(10, 30) <= current_time <= time(10, 33):
            shade_ex_on(channel_shade_ex)
        else:
            shade_ex_off(channel_shade_ex)

def shade_ret_thread():
    while True:
        current_time = datetime.now().time()

        if time(1, 30) <= current_time <= time(1, 33):
            shade_ret_on(channel_shade_ret)
        else:
            shade_ret_off(channel_shade_ret)

try:
    # Start threads for each device
    threading.Thread(target=mist_thread).start()
    threading.Thread(target=fan1_thread).start()
    threading.Thread(target=fan2_thread).start()
    threading.Thread(target=pump_thread).start()
    threading.Thread(target=shade_ex_thread).start()
    threading.Thread(target=shade_ret_thread).start()

    # Keep the main thread running
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()
