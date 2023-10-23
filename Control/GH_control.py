import RPi.GPIO as GPIO
from datetime import datetime, time
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

try:
    while True:
        current_time = datetime.now().time()

        # Mist
        if (time(8, 0) <= current_time <= time(16, 0)):
            mist_on(channel_mist)
            t.sleep(8)
            mist_off(channel_mist)
            t.sleep(1432)
        else:
            mist_off(channel_mist)

        # Fan 1
        if (time(6, 0) <= current_time <= time(7, 59, 49)) or ((time(16, 0) <= current_time <= time(18,0))):
            fan1_on(channel_fan1)
        elif (time(7,59,50) <= current_time <= time(16,0)):
            fan1_off(channel_fan1)
            t.sleep(30)
            fan1_on(channel_fan1)
            t.sleep(1410)
        else:
            fan1_off(channel_fan1)

        # Fan 2
        if (time(6, 0) <= current_time <= time(7, 59, 49)) or ((time(16, 0) <= current_time <= time(18,0))):
            fan2_on(channel_fan2)
        elif (time(7,59,55) <= current_time <= time(16,0)):
            fan2_off(channel_fan2)
            t.sleep(30)
            fan2_on(channel_fan2)
            t.sleep(1410)
        else:
            fan1_off(channel_fan1)

        # Wet pad pump
        if time(6, 0) <= current_time <= time(18, 0):
            pump_on(channel_pump)
        else:
            pump_off(channel_pump)

        # Shade Extends
        if time(10, 30) <= current_time <= time(10, 33):
            shade_ex_on(channel_shade_ex)
        else:
            shade_ex_off(channel_shade_ex)

        # Shade Retract
        if time(1, 30) <= current_time <= time(1, 33):
            shade_ret_on(channel_shade_ret)
        else:
            shade_ret_off(channel_shade_ret)

except KeyboardInterrupt:
    GPIO.cleanup()
