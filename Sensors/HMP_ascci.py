import serial
import io
from time import sleep
from datetime import datetime

serial_THUM = serial.Serial("/dev/ttyACM0",
                   baudrate=4800,
                   bytesize=serial.SEVENBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=2)

THUM_33 = io.TextIOWrapper(io.BufferedRWPair(serial_THUM, serial_THUM))

try:
    THUM_33.write("open 33\r\n")
    THUM_33.flush()
    print("33 is opened")
    while True:
        THUM_33.write("send\r\n")
        print("send")
        THUM_33.flush()
        sleep(1)
        data_33 = THUM_33.readline()
        print(f"data is: {data_33}")
        THUM_33.flush()
        sleep(2)
        THUM_33.write("close\r\n")
        print("closed")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")

