import serial
import io
from time import sleep
from datetime import datetime

THUM_34 = serial.Serial("/dev/ttyACM0",
                   baudrate=19200,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False)
HUM_34 = io.TextIOWrapper(io.BufferedRWPair(THUM_34, THUM_34))
try:
    while True:
        HUM_34.write("open34\n")
        HUM_34.flush()
        sleep(0.5)
        HUM_34.write("send 34\n")
        data=THUM_34.readline()
        print(f"{data}")
        HUM_34.flush()
        sleep(0.5)
        HUM_34.write("close \n")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")