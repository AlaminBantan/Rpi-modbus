import serial
import time
import io
import csv
from datetime import datetime

IR_3 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_3 = io.TextIOWrapper(io.BufferedRWPair(IR_3, IR_3))
try:
    while True:
        # Command is the Slave ID + M!, to take measurement
        command = "3M!\r"
        IR_3.write(command)
        IR_3.flush()
        time.sleep(1)
        # read bit
        data_str ="3D0!\r"
        IR_3.write(data_str)
        data = IR_3.readline()
        IR_3.flush()
        time.sleep(1)
        if len(data.split('+'))> 1:
            print(f"Temperature of the surface is: {data.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")