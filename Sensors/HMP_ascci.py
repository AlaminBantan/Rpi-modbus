import serial
import time
import io
import csv
from datetime import datetime

THUM_240 = serial.Serial("/dev/ttyACM0",
                   baudrate=4800,
                   bytesize=serial.SEVENBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
THUM_240 = io.TextIOWrapper(io.BufferedRWPair(THUM_240, THUM_240))
try:
    while True:
        data ="r"
        THUM_240.read(data)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")