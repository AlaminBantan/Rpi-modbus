import serial
import time
import io


se = serial.Serial("/dev/ttyUSB0",
                baudrate=9600,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                xonxoff=False,
                timeout=1)

sio = io.TextIOWrapper(io.BufferedRWPair(se,se))

try:
    while True:
    #Command is the Slave ID + M!, to take measurement
        command = "?1"
        print(f"{command} sent")
        sio.write(command)
        sio.flush()
        time.sleep(0.2)
        data = sio.readlines()
        print(data)
        time.sleep(2)
except KeyboardInterrupt:
    print("closed")