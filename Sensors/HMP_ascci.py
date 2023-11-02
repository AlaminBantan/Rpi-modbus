import serial
import io
from time import sleep
from datetime import datetime

THUM_240 = serial.Serial("/dev/ttyACM0",
                   baudrate=19200,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False)
THUM_240 = io.TextIOWrapper(io.BufferedRWPair(THUM_240, THUM_240))
try:
    while True:
        THUM_240.write("Open 34")
        sleep(3)
        THUM_240.write("send 34")
        data=THUM_240.readline()
        print(f"{data}")
        THUM_240.write("close")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")