import serial
import time
import io
import csv
from datetime import datetime

se = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)

sio = io.TextIOWrapper(io.BufferedRWPair(se, se))
try:
    while True:
        # Command is the Slave ID + M!, to take measurement
        command = "1M!\r"
        sio.write(command)
        sio.flush()
        time.sleep(1)
        # read bit
        data_str ="1D0!\r"
        sio.write(data_str)
        data = sio.readline()
        sio.flush()
        time.sleep(1)
        if len(data.split('+'))> 1:
            print("measure:", data.split('+')[1])

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")
