import serial
import io
from time import sleep
from datetime import datetime

THUM_34 = serial.Serial("/dev/ttyACM0",
                   baudrate=4800,
                   bytesize=serial.SEVENBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=2)

HUM_34 = io.TextIOWrapper(io.BufferedRWPair(THUM_34, THUM_34))

try:
    while True:
        HUM_34.write("open 34")
        print("open")
        HUM_34.flush()
        sleep(1)
        HUM_34.write("send")
        print("send")
        HUM_34.flush()
        sleep(1)
        data = HUM_34.readline()
        print(f"data is: {data}")
        HUM_34.flush()
        sleep(1)
        HUM_34.write("close")
        print("close")
        sleep(2)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")



THUM_33 = serial.Serial("/dev/ttyACM0",
                   baudrate=4800,
                   bytesize=serial.SEVENBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=2)

HUM_33 = io.TextIOWrapper(io.BufferedRWPair(THUM_33, THUM_33))

try:
    while True:
        HUM_33.write("open 33")
        print("open")
        HUM_33.flush()
        sleep(1)
        HUM_33.write("send")
        print("send")
        HUM_33.flush()
        sleep(1)
        data = HUM_33.readline()
        print(f"data is: {data}")
        HUM_33.flush()
        sleep(1)
        HUM_33.write("close")
        print("close")
        sleep(2)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")




THUM_32 = serial.Serial("/dev/ttyACM0",
                   baudrate=4800,
                   bytesize=serial.SEVENBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=2)

HUM_32 = io.TextIOWrapper(io.BufferedRWPair(THUM_32, THUM_32))

try:
    while True:
        HUM_32.write("open 32")
        print("open")
        HUM_32.flush()
        sleep(1)
        HUM_32.write("send")
        print("send")
        HUM_32.flush()
        sleep(1)
        data = HUM_32.readline()
        print(f"data is: {data}")
        HUM_32.flush()
        sleep(1)
        HUM_32.write("close")
        print("close")
        sleep(2)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")


THUM_31 = serial.Serial("/dev/ttyACM0",
                   baudrate=4800,
                   bytesize=serial.SEVENBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=2)

HUM_31 = io.TextIOWrapper(io.BufferedRWPair(THUM_31, THUM_31))

try:
    while True:
        HUM_31.write("open 31")
        print("open")
        HUM_31.flush()
        sleep(1)
        HUM_31.write("send")
        print("send")
        HUM_31.flush()
        sleep(1)
        data = HUM_31.readline()
        print(f"data is: {data}")
        HUM_31.flush()
        sleep(1)
        HUM_31.write("close")
        print("close")
        sleep(2)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")



    
    