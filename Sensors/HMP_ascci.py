import serial
import io
from time import sleep
from datetime import datetime

THUM_34 = serial.Serial("/dev/ttyACM0",
                   baudrate=19200,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_EVEN,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False)
HUM_34 = io.TextIOWrapper(io.BufferedRWPair(THUM_34, THUM_34))
try:
    while True:
        open_34 = "OPEN 34"
        HUM_34.write(open_34)
        HUM_34.flush()
        sleep(2)
        send_34 = "SEND 34"
        HUM_34.write(send_34)
        data=THUM_34.readline()
        print(f"{data}")
        HUM_34.flush()
        sleep(2)
        close_34 = "CLOSE"
        HUM_34.write(close_34)

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")