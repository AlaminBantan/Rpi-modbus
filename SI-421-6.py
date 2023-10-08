import serial
import time
import io
import csv
from datetime import datetime

IR_6 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_6 = io.TextIOWrapper(io.BufferedRWPair(IR_6, IR_6))
try:
    while True:
        # command_command_5 is the Slave ID + M!, to take measurement
        command_6 = "6M!\r"
        IR_6.write(command_6)
        IR_6.flush()
        time.sleep(1)
        # read bit
        data_str_6 ="6D0!\r"
        IR_6.write(data_str)
        data_6 = IR_6.readline()
        IR_6.flush()
        time.sleep(1)
        if len(data_6.split('+'))> 1:
            print(f"Temperature of the surface 6 is: {data_6.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")