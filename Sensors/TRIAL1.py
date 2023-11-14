import serial
import io
import re
from time import sleep

def read_device(serial_wrapper, device_number):
    try:
        # Open the device
        serial_wrapper.write(f"OPEN {device_number}\r\n")
        serial_wrapper.flush()
        print(f"Device {device_number} is opened")
        sleep(3)

        # Send the data request
        serial_wrapper.write("SEND\r\n")
        serial_wrapper.flush()
        print("Send")
        sleep(3)

        # Read and print the data
        data = serial_wrapper.readlines()

        # Extract RH and Ta from the data
        rh_match = re.search(r'RH= (\d+\.\d+)', data[-1])
        ta_match = re.search(r'Ta= (\d+\.\d+)', data[-1])

        if rh_match and ta_match:
            rh_value = rh_match.group(1)
            ta_value = ta_match.group(1)
            print(f"Data from Device {device_number}: RH={rh_value}% Ta={ta_value}'C")

        sleep(3)

    except Exception as e:
        # Handle exceptions gracefully
        print(f"Error in device {device_number}: {e}")
    finally:
        # Close the device
        serial_wrapper.write("CLOSE\r\n")
        serial_wrapper.flush()
        print(f"Device {device_number} closed")
        sleep(5)

# Define device numbers in a circular manner
device_numbers = ["31", "32", "33", "34"]

# Serial configuration for all devices
serial_devices = [serial.Serial("/dev/ttyACM0",
                                baudrate=4800,
                                bytesize=serial.SEVENBITS,
                                parity=serial.PARITY_EVEN,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout=2) for _ in range(len(device_numbers))]

# TextIOWrapper objects for all devices
THUM_devices = [io.TextIOWrapper(io.BufferedRWPair(serial_device, serial_device)) for serial_device in serial_devices]

try:
    while True:
        for i, device_number in enumerate(device_numbers):
            read_device(THUM_devices[i], device_number)
            sleep(1)  # Add a small delay between devices

except KeyboardInterrupt:
    # Clean up when interrupted
    print("Ports Now Closed")
finally:
    # Close all open ports
    for serial_device in serial_devices:
        serial_device.close()