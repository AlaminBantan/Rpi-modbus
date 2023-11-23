import serial
import time
import io

IR_0 = serial.Serial("/dev/ttyUSB0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=2)
IR_0 = io.TextIOWrapper(io.BufferedRWPair(IR_0, IR_0))
try:
    while True:
        # command_command_5 is the Slave ID + M!, to take measurement
        IR_0.write("0M!\r")
        print("send")
        IR_0.flush()
        time.sleep(1)
        # read bit

        IR_0.write("0D0!\r")
        print("read")
        IR_0.flush()
        time.sleep(1)

        data_0 = IR_0.readlines()
        print("print data")
        IR_0.flush()
        print(data_0)
        time.sleep(1)


except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")