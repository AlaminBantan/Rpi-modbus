import RPi.GPIO as GPIO
from datetime import datetime, time
import threading
import time as t

# Define GPIO channels
channel_fan1 = 25 #connect the set 1 of fans from zone B and C to relay1 (147,179)
channel_fan2 = 24 #connect the set 2 of fans from zone B and C to relay2 (148,180)
channel_mist = 23 #connect the misting pump to relay 3 (221)
channel_pump = 14 #connect the wet pad pump from zones B and C to relay 6 (129,152)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel_mist, GPIO.OUT)
GPIO.setup(channel_fan1, GPIO.OUT)
GPIO.setup(channel_fan2, GPIO.OUT)
GPIO.setup(channel_pump, GPIO.OUT)


# Define functions for each device

#mist
def mist_off(pin):
    GPIO.output(pin, GPIO.HIGH)
def mist_on(pin):
    GPIO.output(pin, GPIO.LOW)

#fan1
def fan1_off(pin):
    GPIO.output(pin, GPIO.HIGH)
def fan1_on(pin):
    GPIO.output(pin, GPIO.LOW)

#fan2
def fan2_off(pin):
    GPIO.output(pin, GPIO.HIGH)
def fan2_on(pin):
    GPIO.output(pin, GPIO.LOW)

#wet pad pump
def pump_off(pin):
    GPIO.output(pin, GPIO.HIGH)
def pump_on(pin):
    GPIO.output(pin, GPIO.LOW)


# Define functions to control devices in threads
def fan1_thread():
    while True:
        current_time = datetime.now().time()
        fan1_time_ranges = [
            (time(6, 0, 0), time(7, 59, 50)),
            (time(8, 0, 20), time(8, 23, 50)),
            (time(8, 24, 20), time(8, 47, 50)),
            (time(8, 48, 20), time(9, 11, 50)),
            (time(9, 12, 20), time(9, 35, 50)),
            (time(9, 36, 20), time(9, 59, 50)),
            (time(10, 0, 20), time(10, 23, 50)),
            (time(10, 24, 20), time(10, 47, 50)),
            (time(10, 48, 20), time(11, 11, 50)),
            (time(11, 12, 20), time(11, 35, 50)),
            (time(11, 36, 20), time(11, 59, 50)),
            (time(12, 0, 20), time(12, 23, 50)),
            (time(12, 24, 20), time(12, 47, 50)),
            (time(12, 48, 20), time(1, 11, 50)),
            (time(1, 12, 20), time(1, 35, 50)),
            (time(1, 36, 20), time(1, 59, 50)),
            (time(2, 0, 20), time(2, 23, 50)),
            (time(2, 24, 20), time(2, 47, 50)),
            (time(2, 48, 20), time(3, 11, 50)),
            (time(3, 12, 20), time(3, 35, 50)),
            (time(3, 36, 20), time(3, 59, 50)),
            (time(4, 0, 20), time(18, 0, 0))
        ]

        fan1_time = any(fan1_start_time <= current_time <= fan1_end_time for fan1_start_time, fan1_end_time in fan1_time_ranges)

        if fan1_time:
            fan1_on(channel_fan1)
            t.sleep(1)
        else:
            fan1_off(channel_fan1)
            t.sleep(5)


def fan2_thread():
    while True:
        current_time = datetime.now().time()
        fan2_time_ranges = [
            (time(6, 0, 0), time(7, 59, 55)),
            (time(8, 0, 25), time(8, 23, 55)),
            (time(8, 24, 25), time(8, 47, 55)),
            (time(8, 48, 25), time(9, 11, 55)),
            (time(9, 12, 25), time(9, 35, 55)),
            (time(9, 36, 25), time(9, 59, 55)),
            (time(10, 0, 25), time(10, 23, 55)),
            (time(10, 24, 25), time(10, 47, 55)),
            (time(10, 48, 25), time(11, 11, 55)),
            (time(11, 12, 25), time(11, 35, 55)),
            (time(11, 36, 25), time(11, 59, 55)),
            (time(12, 0, 25), time(12, 23, 55)),
            (time(12, 24, 25), time(12, 47, 55)),
            (time(12, 48, 25), time(1, 11, 55)),
            (time(1, 12, 25), time(1, 35, 55)),
            (time(1, 36, 25), time(1, 59, 55)),
            (time(2, 0, 25), time(2, 23, 55)),
            (time(2, 24, 25), time(2, 47, 55)),
            (time(2, 48, 25), time(3, 11, 55)),
            (time(3, 12, 25), time(3, 35, 55)),
            (time(3, 36, 25), time(3, 59, 55)),
            (time(4, 0, 25), time(18, 0, 0))
        ]

        fan2_time = any(fan2_start_time <= current_time <= fan2_end_time for fan2_start_time, fan2_end_time in fan2_time_ranges)

        if fan2_time:
            fan2_on(channel_fan2)
        else:
            fan2_off(channel_fan2)

def mist_thread():
     while True:
        current_time = datetime.now().time()
        misting_time_ranges = [
            (time(8, 0, 0), time(8, 0, 8)),
            (time(8, 24, 0), time(8, 24, 8)),
            (time(8, 48, 0), time(8, 48, 8)),
            (time(9, 12, 0), time(9, 12, 8)),
            (time(9, 36, 0), time(9, 36, 8)),
            (time(10, 0, 0), time(10, 0, 8)),
            (time(10, 24, 0), time(10, 24, 8)),
            (time(10, 48, 0), time(10, 48, 8)),
            (time(11, 12, 0), time(11, 12, 8)),
            (time(11, 36, 0), time(11, 36, 8)),
            (time(12, 0, 0), time(12, 0, 8)),
            (time(12, 24, 0), time(12, 24, 8)),
            (time(12, 48, 0), time(12, 48, 8)),
            (time(13, 12, 0), time(13, 12, 8)),
            (time(13, 36, 0), time(13, 36, 8)),
            (time(14, 0, 0), time(14, 0, 8)),
            (time(14, 24, 0), time(14, 24, 8)),
            (time(14, 48, 0), time(14, 48, 8)),
            (time(15, 12, 0), time(15, 12, 8)),
            (time(15, 36, 0), time(15, 36, 8)),
            (time(16, 0, 0), time(16, 0, 8))
        ]

        misting_time = any(mist_start_time <= current_time <= mist_end_time for mist_start_time, mist_end_time in misting_time_ranges)

        if misting_time:
            print("mist is on")
            mist_on(channel_mist)
        else:
            mist_off(channel_mist)

def pump_thread():
    while True:
        current_time = datetime.now().time()

        if time(6, 0) <= current_time <= time(18, 0):
            pump_on(channel_pump)
        else:
            pump_off(channel_pump)
            
            


try:
    # Start threads for each device
    threading.Thread(target=fan1_thread).start()
    threading.Thread(target=fan2_thread).start()
    threading.Thread(target=mist_thread).start()
    threading.Thread(target=pump_thread).start()


except KeyboardInterrupt:
    GPIO.cleanup()
