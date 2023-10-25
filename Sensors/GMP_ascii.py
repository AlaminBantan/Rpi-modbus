import serial
import io
from datetime import datetime

carbo_240 = serial.Serial("/dev/ttyACM0",
                   baudrate=19200,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
carbo_240 = io.TextIOWrapper(io.BufferedRWPair(carbo_240, carbo_240))
try:
    while True:
        carbo_240.write("R")
        data=carbo_240.readline()
        
        print(f"{data}")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")