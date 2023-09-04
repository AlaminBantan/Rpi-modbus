import minimalmodbus
from time import sleep, strftime
import csv
import os


mb_address = 1  # Modbus address of sensor

PAR_sensy = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called PAR_sensy (port name, slave address (in decimal))

PAR_sensy.serial.baudrate = 19200 				# BaudRate
PAR_sensy.serial.bytesize = 8					# Number of data bits to be requested
PAR_sensy.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_sensy.serial.stopbits = 1					# Number of stop bits
PAR_sensy.serial.timeout  = 0.5					# Timeout time in seconds
PAR_sensy.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
PAR_sensy.clear_buffers_before_each_transaction = True
PAR_sensy.close_port_after_each_call = True

csv_header = ["Date", "Time", "PAR Intensity (umol.m^-2.s^-1)"]

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
    PAR_intensity = PAR_sensy.read_float(0, 3, 2, 0)

    # Append data to the current day's CSV file
    with open(f"data_{current_date}.csv", mode="a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([current_date, current_time, PAR_intensity])

    # Check if it's past 12 AM, and if so, exit the loop
    if current_time >= "23:59:59":
        break

    sleep(60)

PAR_sensy.serial.close()
print("Ports Now Closed")
