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

#shade will not be controlled by the Pi, but in case we want to we can change these lines.

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




#########################################################################################################################
#Schedule:
    #6:30 fan2 and wet pad pump on.
    #10:00 misting starts (first mist 10 seconds to repressurize the lines) and every 30 mins one mist for 6 seconds
    #fan1 goes off 9 second before mist and go on 20 second after the mist ends.
    #fan2 goes off 7 second before mist and go on 22 second after the mist ends.
    #16:00 last misting.
    #18:30 fan2 and wet pad pump go off.
    #fan1 is on all day long (except misting intervals).
#########################################################################################################################



# Define functions to control devices in threads

#fans are delayed by 2 seconds to prevent electricl surge
def fan1_thread():
    while True:
        current_time = datetime.now().time()
        fan1_time_ranges = [
            (time(0, 0, 0), time(9, 59, 51)), 
            (time(10, 0, 30), time(10, 17, 51)),
            (time(10, 18, 28), time(10, 35, 51)),
            (time(10, 36, 28), time(10, 53, 51)),
            (time(10, 54, 28), time(11, 11, 51)),
            (time(11, 12, 28), time(11, 29, 51)),
            (time(11, 30, 28), time(11, 47, 51)),
            (time(11, 48, 28), time(12, 5, 51)),
            (time(12, 6, 28), time(12, 23, 51)),
            (time(12, 24, 28), time(12, 41, 51)),
            (time(12, 42, 28), time(12, 59, 51)),
            (time(13, 0, 28), time(13, 17, 51)),
            (time(13, 18, 28), time(13, 35, 51)),
            (time(13, 36, 28), time(13, 53, 51)),
            (time(13, 54, 28), time(14, 11, 51)),
            (time(14, 12, 28), time(14, 29, 51)),
            (time(14, 30, 28), time(14, 47, 51)),
            (time(14, 48, 28), time(15, 5, 51)),
            (time(15, 6, 28), time(15, 23, 51)),
            (time(15, 24, 28), time(15, 41, 51)),
            (time(15, 42, 28), time(15, 59, 51)),
            (time(16, 0, 28), time(23, 59, 59))
        ]
        fan1_time = any(fan1_start_time <= current_time <= fan1_end_time for fan1_start_time, fan1_end_time in fan1_time_ranges)

        if fan1_time:
            fan1_on(channel_fan1)
            t.sleep(0.5)
        else:
            fan1_off(channel_fan1)
            t.sleep(0.5)


def fan2_thread():
    while True:
        current_time = datetime.now().time()
        fan2_time_ranges = [
            (time(6, 30, 0), time(9, 59, 53)),
            (time(10, 0, 32), time(10, 17, 53)),
            (time(10, 18, 30), time(10, 35, 53)),
            (time(10, 36, 30), time(10, 53, 53)),
            (time(10, 54, 30), time(11, 11, 53)),
            (time(11, 12, 30), time(11, 29, 53)),
            (time(11, 30, 30), time(11, 47, 53)),
            (time(11, 48, 30), time(12, 5, 53)),
            (time(12, 6, 30), time(12, 23, 53)),
            (time(12, 24, 30), time(12, 41, 53)),
            (time(12, 42, 30), time(12, 59, 53)),
            (time(13, 0, 30), time(13, 17, 53)),
            (time(13, 18, 30), time(13, 35, 53)),
            (time(13, 36, 30), time(13, 53, 53)),
            (time(13, 54, 30), time(14, 11, 53)),
            (time(14, 12, 30), time(14, 29, 53)),
            (time(14, 30, 30), time(14, 47, 53)),
            (time(14, 48, 30), time(15, 5, 53)),
            (time(15, 6, 30), time(15, 23, 53)),
            (time(15, 24, 30), time(15, 41, 53)),
            (time(15, 42, 30), time(15, 59, 53)),
            (time(16, 0, 30), time(18, 30, 0))
        ]
        fan2_time = any(fan2_start_time <= current_time <= fan2_end_time for fan2_start_time, fan2_end_time in fan2_time_ranges)

        if fan2_time:
            fan2_on(channel_fan2)
            t.sleep(0.5)
        else:
            fan2_off(channel_fan2)
            t.sleep(0.5)

def mist_thread():
     while True:
        current_time = datetime.now().time()
        misting_time_ranges = [
            (time(10, 0, 0), time(10, 0, 10)),
            (time(10, 18, 0), time(10, 18, 8)),
            (time(10, 36, 0), time(10, 36, 8)),
            (time(10, 54, 0), time(10, 54, 8)),
            (time(11, 12, 0), time(11, 12, 8)),
            (time(11, 30, 0), time(11, 30, 8)),
            (time(11, 48, 0), time(11, 48, 8)),
            (time(12, 6, 0), time(12, 6, 8)),
            (time(12, 24, 0), time(12, 24, 8)),
            (time(12, 42, 0), time(12, 42, 8)),
            (time(13, 0, 0), time(13, 0, 8)),
            (time(13, 18, 0), time(13, 18, 8)),
            (time(13, 36, 0), time(13, 36, 8)),
            (time(13, 54, 0), time(13, 54, 8)),
            (time(14, 12, 0), time(14, 12, 8)),
            (time(14, 30, 0), time(14, 30, 8)),
            (time(14, 48, 0), time(14, 48, 8)),
            (time(15, 6, 0), time(15, 6, 8)),
            (time(15, 24, 0), time(15, 24, 8)),
            (time(15, 42, 0), time(15, 42, 8)),
            (time(16, 0, 0), time(16, 0, 8))
        ]
        misting_time = any(mist_start_time <= current_time <= mist_end_time for mist_start_time, mist_end_time in misting_time_ranges)

        if misting_time:
            print("mist is on")
            mist_on(channel_mist)
            t.sleep(0.5)
        else:
            mist_off(channel_mist)
            t.sleep(0.5)

def pump_thread():
    while True:
        current_time = datetime.now().time()

        if time(6, 30, 0) <= current_time <= time(18, 30, 0):
            pump_on(channel_pump)
            t.sleep(5)
        else:
            pump_off(channel_pump)
            t.sleep(5)
            
            
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
