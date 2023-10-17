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
        
        # Extract humidity and temperature strings
        humidity_str = parts[1]
        temperature_str = parts[3]

        # Remove units and convert to float
        humidity = float(humidity_str[3:])
        temperature = float(temperature_str[3:])

        print(f"The humidity is {humidity} and the temperature is {temperature} °C")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")
