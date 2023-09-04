import minimalmodbus
from time import sleep, strftime
import csv
import os


mb_address = 1  # Modbus address of sensor

Solar_sensy = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called Solar_sensy (port name, slave address (in decimal))

Solar_sensy.serial.baudrate = 19200 				# BaudRate
Solar_sensy.serial.bytesize = 8					# Number of data bits to be requested
Solar_sensy.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_sensy.serial.stopbits = 1					# Number of stop bits
Solar_sensy.serial.timeout  = 0.5					# Timeout time in seconds
Solar_sensy.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
Solar_sensy.clear_buffers_before_each_transaction = True
Solar_sensy.close_port_after_each_call = True

csv_header = ["Date", "Time", "Solar_Radiation (W.m^-2)"]

while True:
    # Get current date and time
    current_date = strftime("%m-%d-%Y")
    current_time = strftime("%H:%M")

    # Check if it's a new day and create a new CSV file
    if not os.path.exists(f"data_{current_date}.csv"):
        with open(f"data_{current_date}.csv", mode="w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(csv_header)

    # Read light intensity from the sensor
    Solar_Radiation = Solar_sensy.read_float(0, 3, 2, 0)

    # Append data to the current day's CSV file
    with open(f"data_{current_date}.csv", mode="a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([current_date, current_time, Solar_Radiation])

    # Check if it's past 12 AM, and if so, exit the loop
    if current_time >= "23:59:59":
        break

    sleep(60)

Solar_sensy.serial.close()
print("Ports Now Closed")