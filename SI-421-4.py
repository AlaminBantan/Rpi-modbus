import serial
import time
import io
import csv
from datetime import datetime

IR_4 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_4 = io.TextIOWrapper(io.BufferedRWPair(IR_4, IR_4))
try:
    while True:
        # Command is the Slave ID + M!, to take measurement
        command = "4M!\r"
        IR_4.write(command)
        IR_4.flush()
        time.sleep(1)
        # read bit
        data_str ="4D0!\r"
        IR_4.write(data_str)
        data = IR_4.readline()
        IR_4.flush()
        time.sleep(1)
        if len(data.split('+'))> 1:
            print(f"Temperature of the surface is: {data.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")