import serial
import io
import re
import csv
from time import sleep
from datetime import datetime

def read_device(serial_wrapper, device_number, csv_writer):
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

        # Extract RH and Ta from the data
        rh_match = re.search(r'RH= (\d+\.\d+)', data[-1])
        ta_match = re.search(r'Ta= (\d+\.\d+)', data[-1])

        if rh_match and ta_match:
            rh_value = rh_match.group(1)
            ta_value = ta_match.group(1)

            # Get current date and time
            now = datetime.now()
            current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

            # Write to CSV
            csv_writer.writerow([current_datetime, ta_value, rh_value])
            print(f"Data logged for Device {device_number}")

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

# Define device numbers and corresponding CSV column headers
device_columns = {
    "31": ["Temperature zone B (a)", "RH zone B (a)"],
    "32": ["Temperature zone B (b)", "RH zone B (b)"],
    "33": ["Temperature zone C (a)", "RH zone C (a)"],
    "34": ["Temperature zone C (b)", "RH zone C (b)"]
}

# Create and open the CSV file
csv_filename = "Temp/RH.csv"
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header to the CSV file
    csv_header = ["date", "time"]
    for device_number, columns in device_columns.items():
        csv_header.extend([f"{column} ({device_number})" for column in columns])
    
    csv_writer.writerow(csv_header)
    
    # Serial configuration for all devices
    serial_devices = [serial.Serial("/dev/ttyACM0",
                                    baudrate=4800,
                                    bytesize=serial.SEVENBITS,
                                    parity=serial.PARITY_EVEN,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout=2) for _ in range(len(device_columns))]

    # TextIOWrapper objects for all devices
    THUM_devices = [io.TextIOWrapper(io.BufferedRWPair(serial_device, serial_device)) for serial_device in serial_devices]

    try:
        while True:
            for i, (device_number, columns) in enumerate(device_columns.items()):
                read_device(THUM_devices[i], device_number, csv_writer)
                sleep(1)  # Add a small delay between devices

    except KeyboardInterrupt:
        # Clean up when interrupted
        print("Ports Now Closed")
    finally:
        # Close all open ports
        for serial_device in serial_devices:
            serial_device.close()
