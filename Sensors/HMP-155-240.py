import serial
import time
import io
import csv
from datetime import datetime

THUM_240 = serial.Serial("/dev/ttyACM0",
                   baudrate=4800,
                   bytesize=serial.SEVENBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
THUM_240 = io.TextIOWrapper(io.BufferedRWPair(THUM_240, THUM_240))
try:
    while True:
        THUM_240.write("R")
        data = THUM_240.readline()
        
        # Assuming the response format is "RH= 54.4 %RH Ta= 26.8 'C"
        parts = data.split()
        
        # Check if the response format is correct
        if len(parts) >= 6 and parts[0] == 'RH=' and parts[2] == '%RH' and parts[3] == 'Ta=' and parts[5] == "'C":
            # Extract humidity and temperature values
            humidity = float(parts[1])
            temperature = float(parts[4])

            print(f"The humidity is {humidity} and the temperature is {temperature} °C")
        else:
            print("Invalid response format")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")
