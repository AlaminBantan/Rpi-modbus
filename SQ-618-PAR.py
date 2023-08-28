import minimalmodbus
from time import sleep, strftime
import csv


mb_address = 1  # Modbus address of sensor

sensy_boi = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called sensy_boi (port name, slave address (in decimal))

sensy_boi.serial.baudrate = 19200 				# BaudRate
sensy_boi.serial.bytesize = 8					# Number of data bits to be requested
sensy_boi.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
sensy_boi.serial.stopbits = 1					# Number of stop bits
sensy_boi.serial.timeout  = 0.5					# Timeout time in seconds
sensy_boi.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
sensy_boi.clear_buffers_before_each_transaction = True
sensy_boi.close_port_after_each_call = True


# Create or open the CSV file for writing
csv_filename = "PAR_sensor_data.csv"
csv_header = ["Date", "Time", "Light Intensity (umol.m^-2.s^-1)"]

try:
    with open(csv_filename, mode="w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)

        while True:
            lightintensity = sensy_boi.read_float(0, 3, 2, 0)
            current_time = strftime("%H:%M")
            current_date = strftime("%m/%d/%Y")

            # Append data to the CSV file
            csv_writer.writerow([current_date, current_time, lightintensity])

            sleep(60)
except KeyboardInterrupt:
    sensy_boi.serial.close()
    print("Ports Now Closed")
