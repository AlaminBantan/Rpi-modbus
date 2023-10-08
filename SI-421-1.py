import serial
import time
import io
import csv
from datetime import datetime

IR_1 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_1 = io.TextIOWrapper(io.BufferedRWPair(IR_1, IR_1))
try:
    while True:
        # Command is the Slave ID + M!, to take measurement
        command = "1M!\r"
        IR_1.write(command)
        IR_1.flush()
        time.sleep(1)
        # read bit
        data_str ="1D0!\r"
        IR_1.write(data_str)
        data = IR_1.readline()
        IR_1.flush()
        time.sleep(1)
        if len(data.split('+'))> 1:
            print("Temperature of the surface is:", {data.split('+')[1]} "degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")