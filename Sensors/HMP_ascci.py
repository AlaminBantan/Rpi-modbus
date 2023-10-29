import serial
import time
import io
import csv
from datetime import datetime

THUM_240 = serial.Serial("/dev/ttyACM0",
                   baudrate=19200,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
THUM_240 = io.TextIOWrapper(io.BufferedRWPair(THUM_240, THUM_240))
try:
    while True:
        THUM_240.write("OPEN 33")
        time.sleep(1)
        THUM_240.write("SEND 33")
        data=THUM_240.readline()
        
        print(f"{data}")
        THUM_240.write("CLOSE 33")        

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")