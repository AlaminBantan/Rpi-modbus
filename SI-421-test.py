import serial
import time
import io

#configuration of SI-421 ID=0
IR_0 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_0 = io.TextIOWrapper(io.BufferedRWPair(IR_0, IR_0))

#configuration of SI-421 ID=1
IR_1 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_1 = io.TextIOWrapper(io.BufferedRWPair(IR_1, IR_1))

#configuration of SI-421 ID=2
IR_2 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_2 = io.TextIOWrapper(io.BufferedRWPair(IR_2, IR_2))

#configuration of SI-421 ID=3
IR_3 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_3 = io.TextIOWrapper(io.BufferedRWPair(IR_3, IR_3))

#configuration of SI-421 ID=4
IR_4 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_4 = io.TextIOWrapper(io.BufferedRWPair(IR_4, IR_4))

#configuration of SI-421 ID=5
IR_5 = serial.Serial("/dev/ttyACM0",
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   xonxoff=False,
                   timeout=1)
IR_5 = io.TextIOWrapper(io.BufferedRWPair(IR_5, IR_5))
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

try:
    while True:
        # command_1 is the Slave ID + M!, to take measurement
        command_1 = "1M!\r"
        IR_1.write(command_1)
        IR_1.flush()
        time.sleep(1)
        # read bit
        data_str_1 ="1D0!\r"
        IR_1.write(data_str_1)
        data_1 = IR_1.readline()
        
        IR_1.flush()
        time.sleep(1)
        if len(data_1.split('+'))> 1:
            print(f"Temperature of the surface is: {data_1.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")

try:
    while True:
        # command_2 is the Slave ID + M!, to take measurement
        command_2 = "2M!\r"
        IR_2.write(command_2)
        IR_2.flush()
        time.sleep(1)
        # read bit
        data_str_2 ="2D0!\r"
        IR_2.write(data_str_2)
        data_2 = IR_2.readline()
        IR_2.flush()
        time.sleep(1)
        if len(data_2.split('+'))> 1:
            print(f"Temperature of the surface is: {data_2.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")

try:
    while True:
        # command_3 is the Slave ID + M!, to take measurement
        command_3 = "3M!\r"
        IR_3.write(command_3)
        IR_3.flush()
        time.sleep(1)
        # read bit
        data_str ="3D0!\r"
        IR_3.write(data_str)
        data_3 = IR_3.readline()
        IR_3.flush()
        time.sleep(1)
        if len(data_3.split('+'))> 1:
            print(f"Temperature of the surface 3 is: {data_3.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")


try:
    while True:
        # command_4 is the Slave ID + M!, to take measurement
        command_4 = "4M!\r"
        IR_4.write(command_4)
        IR_4.flush()
        time.sleep(1)
        # read bit
        data_str ="4D0!\r"
        IR_4.write(data_str)
        data_4 = IR_4.readline()
        IR_4.flush()
        time.sleep(1)
        if len(data_4.split('+'))> 1:
            print(f"Temperature of the surface 4 is: {data_4.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")


try:
    while True:
        # command_5 is the Slave ID + M!, to take measurement
        command_5 = "5M!\r"
        IR_5.write(command_5)
        IR_5.flush()
        time.sleep(1)
        # read bit
        data_str ="5D0!\r"
        IR_5.write(data_str)
        data_5 = IR_5.readline()
        IR_5.flush()
        time.sleep(1)
        if len(data_5.split('+'))> 1:
            print(f"Temperature of the surface 5 is: {data_5.split('+')[1]} degrees celcius")
except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")