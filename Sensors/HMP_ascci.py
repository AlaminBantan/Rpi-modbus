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
                   timeout=1)
THUM_34 = io.TextIOWrapper(io.BufferedRWPair(THUM_34, THUM_34))
try:
    while True:
        THUM_34.write("open 34\n")
        THUM_34.flush()
        sleep(0.5)
        THUM_34.write("send\n")
        data=THUM_34.readline()
        print(f"{data}")
        THUM_34.flush()
        sleep(0.5)
        THUM_34.write("close\n")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")



    