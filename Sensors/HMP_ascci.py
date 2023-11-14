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
    while True:
        THUM_33.write("OPEN 33\r\n")
        THUM_33.flush()
        print("33 is opened")
        sleep(5)

        THUM_33.write("SEND\r\n")
        THUM_33.flush()
        print("send")
        sleep(10)
        
        data_33 = THUM_33.readlines()
        print(f"data is: {data_33}")
        sleep(3)

        THUM_33.write("CLOSE\r\n")
        print("closed")
        sleep(5)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")

