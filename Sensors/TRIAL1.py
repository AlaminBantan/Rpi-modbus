import serial
import io
from time import sleep

def read_device(serial_wrapper, device_number):
    try:
        # Open the device
        serial_wrapper.write(f"OPEN {device_number}\r\n")
        serial_wrapper.flush()
        print(f"Device {device_number} is opened")
        sleep(5)

        # Send the data request
        serial_wrapper.write("SEND\r\n")
        serial_wrapper.flush()
        print("Send")
        sleep(10)

        # Read and print the data
        data = serial_wrapper.readlines()
        print(f"Data from Device {device_number}: {data}")
        sleep(3)

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print(f"Ctrl+C received. Closing Device {device_number}")
    finally:
        # Close the device
        serial_wrapper.write("CLOSE\r\n")
        serial_wrapper.flush()
        print(f"Device {device_number} closed")
        sleep(5)

# Serial Configuration for Device 31
serial_THUM_31 = serial.Serial("/dev/ttyACM0",
                               baudrate=4800,
                               bytesize=serial.SEVENBITS,
                               parity=serial.PARITY_EVEN,
                               stopbits=serial.STOPBITS_ONE,
                               xonxoff=False,
                               timeout=2)
THUM_31 = io.TextIOWrapper(io.BufferedRWPair(serial_THUM_31, serial_THUM_31))

# Serial Configuration for Device 32
serial_THUM_32 = serial.Serial("/dev/ttyACM0",
                               baudrate=4800,
                               bytesize=serial.SEVENBITS,
                               parity=serial.PARITY_EVEN,
                               stopbits=serial.STOPBITS_ONE,
                               xonxoff=False,
                               timeout=2)
THUM_32 = io.TextIOWrapper(io.BufferedRWPair(serial_THUM_32, serial_THUM_32))

# Serial Configuration for Device 33
serial_THUM_33 = serial.Serial("/dev/ttyACM0",
                               baudrate=4800,
                               bytesize=serial.SEVENBITS,
                               parity=serial.PARITY_EVEN,
                               stopbits=serial.STOPBITS_ONE,
                               xonxoff=False,
                               timeout=2)
THUM_33 = io.TextIOWrapper(io.BufferedRWPair(serial_THUM_33, serial_THUM_33))

# Serial Configuration for Device 34
serial_THUM_34 = serial.Serial("/dev/ttyACM0",
                               baudrate=4800,
                               bytesize=serial.SEVENBITS,
                               parity=serial.PARITY_EVEN,
                               stopbits=serial.STOPBITS_ONE,
                               xonxoff=False,
                               timeout=2)
THUM_34 = io.TextIOWrapper(io.BufferedRWPair(serial_THUM_34, serial_THUM_34))

try:
    # Read from Device 31
    read_device(THUM_31, "31")

    # Read from Device 32
    read_device(THUM_32, "32")

    # Read from Device 33
    read_device(THUM_33, "33")

    # Read from Device 34
    read_device(THUM_34, "34")

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")
finally:
    # Close all open ports
    serial_THUM_31.close()
    serial_THUM_32.close()
    serial_THUM_33.close()
    serial_THUM_34.close()
