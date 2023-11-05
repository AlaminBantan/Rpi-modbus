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
        open_34 = "open 34"
        THUM_240.write(open_34)

        send_34 = "send 34"
        THUM_240.write(send_34)

        data=THUM_240.readline()
        print(f"{data}")
        close_34 = "close"
        THUM_240.write(close_34)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")