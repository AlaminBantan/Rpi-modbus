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

THUM_34 = io.TextIOWrapper(io.BufferedRWPair(THUM_34, THUM_34))

try:
    while True:
        THUM_34.write("send")
        print("send")
        THUM_34.flush()
        sleep(1)
        data_34 = THUM_34.readline()
        print(f"data is: {data_34}")
        THUM_34.flush()
        sleep(2)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")

