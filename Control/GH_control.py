import RPi.GPIO as GPIO
from datetime import datetime, time
import threading
import time as t

# Define GPIO channels
channel_fan1 = 25 #connect the set 1 of fans from zone B and C to relay1 (147,179)
channel_fan2 = 24 #connect the set 2 of fans from zone B and C to relay2 (148,180)
channel_mist = 23 #connect the misting pump to relay 3 (221)
channel_shade_ret = 18 #connect the shade retraction motor from zones B and C to relay 4 (125,158)
channel_shade_ex = 15 #connect the shade extension motor from zones B and C to relay 5 (126,159)
channel_pump = 14 #connect the wet pad pump from zones B and C to relay 6 (129,152)

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

#shade extension
#def shade_ex_off(pin):
#    GPIO.output(pin, GPIO.HIGH)
#def shade_ex_on(pin):
#    GPIO.output(pin, GPIO.LOW)

#shade retraction
#def shade_ret_off(pin):
#    GPIO.output(pin, GPIO.HIGH)
#def shade_ret_on(pin):
#    GPIO.output(pin, GPIO.LOW)
#
# Define functions to control devices in threads
def fan1_thread():
    while True:
        current_time = datetime.now().time()
        fan1_time_ranges = [
            (time(0,0,0), time(9,59,52)),           
            (time(10, 0, 23), time(10, 29, 52)),
            (time(10, 30, 21), time(10, 59, 52)),
            (time(11, 0, 21), time(11, 29, 52)),
            (time(11, 30, 21), time(11, 59, 52)),
            (time(12, 0, 21), time(12, 29, 52)),
            (time(12, 30, 21), time(12, 59, 52)),
            (time(13, 0, 21), time(13, 29, 52)),
            (time(13, 30, 21), time(13, 59, 52)),
            (time(14, 0, 21), time(14, 29, 52)),
            (time(14, 30, 21), time(14, 59, 52)),
            (time(15, 0, 21), time(15, 29, 52)),
            (time(15, 30, 21), time(15, 59, 52)),
            (time(16, 0, 21), time(23,59,59))
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
            (time(0, 0, 0), time(9, 59, 54)),
            (time(10, 0, 25), time(10, 29, 54)),
            (time(10, 30, 23), time(10, 59, 54)),
            (time(11, 0, 23), time(11, 29, 54)),
            (time(11, 30, 23), time(11, 59, 54)),
            (time(12, 0, 23), time(12, 29, 54)),
            (time(12, 30, 23), time(12, 59, 54)),
            (time(13, 0, 23), time(13, 29, 54)),
            (time(13, 30, 23), time(13, 59, 54)),
            (time(14, 0, 23), time(14, 29, 54)),
            (time(14, 30, 23), time(14, 59, 54)),
            (time(15, 0, 23), time(15, 29, 54)),
            (time(15, 30, 23), time(15, 59, 54)),
            (time(16, 0, 23), time(23,59,59))
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
            (time(10, 0, 0), time(10, 0, 8)),
            (time(10, 30, 0), time(10, 30, 6)),
            (time(11, 0, 0), time(11, 0, 6)),
            (time(11, 30, 0), time(11, 30, 6)),
            (time(12, 0, 0), time(12, 0, 6)),
            (time(12, 30, 0), time(12, 30, 6)),
            (time(13, 0, 0), time(13, 0, 6)),
            (time(13, 30, 0), time(13, 30, 6)),
            (time(14, 0, 0), time(14, 0, 6)),
            (time(14, 30, 0), time(14, 30, 6)),
            (time(15, 0, 0), time(15, 0, 6)),
            (time(15, 30, 0), time(15, 30, 6)),
            (time(16, 0, 0), time(16, 0, 6))
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

        if time(5, 0) <= current_time <= time(17, 0):
            pump_on(channel_pump)
        else:
            pump_off(channel_pump)
            
            
#def shade_ex_thread():
#    while True:
#        current_time = datetime.now().time()
#
#       if time(10, 30) <= current_time <= time(10, 33):
#            shade_ex_on(channel_shade_ex)
#        else:
#            shade_ex_off(channel_shade_ex)

#def shade_ret_thread():
#    while True:
#        current_time = datetime.now().time()
#
#       if time(1, 30) <= current_time <= time(1, 33):
#            shade_ret_on(channel_shade_ret)
#        else:
#            shade_ret_off(channel_shade_ret)


try:
    # Start threads for each device
    threading.Thread(target=mist_thread).start()
    threading.Thread(target=fan1_thread).start()
    threading.Thread(target=fan2_thread).start()
    threading.Thread(target=pump_thread).start()
    # threading.Thread(target=shade_ex_thread).start()
    # threading.Thread(target=shade_ret_thread).start()

    # Keep the main thread running
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()
