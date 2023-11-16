import serial
import time
import io
from datetime import datetime

IR_0 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_0 = io.TextIOWrapper(io.BufferedRWPair(IR_0, IR_0))
try:
    while True:
        # command_command_5 is the Slave ID + M!, to take measurement
        command_0 = "0M!\r"
        IR_0.write(command_0)
        IR_0.flush()
        time.sleep(1)
        # read bit
        data_str_0 ="0D0!\r"
        IR_0.write(data_str_0)
        data_0 = IR_0.readline()
        IR_0.flush()
        time.sleep(1)
        if len(data_0.split('+'))> 1:
            print(f"Temperature of the surface 0 is: {data_0.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")