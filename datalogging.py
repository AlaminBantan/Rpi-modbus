import minimalmodbus 
from time import sleep
import datetime
import csv

#configuration of SP-522 ID=10
Solar_10 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)
Solar_10.serial.baudrate = 19200 	
Solar_10.serial.bytesize = 8					# Number of data bits to be requested
Solar_10.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_10.serial.stopbits = 1					# Number of stop bits
Solar_10.serial.timeout  = 0.5					# Timeout time in seconds
Solar_10.mode = minimalmodbus.MODE_RTU			
Solar_10.clear_buffers_before_each_transaction = True
Solar_10.close_port_after_each_call = True


#configuration of SP-522 ID=15
Solar_15 = minimalmodbus.Instrument('/dev/ttyUSB0', 15, debug=False)
Solar_15.serial.baudrate = 19200 	
Solar_15.serial.bytesize = 8					# Number of data bits to be requested
Solar_15.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_15.serial.stopbits = 1					# Number of stop bits
Solar_15.serial.timeout  = 0.5					# Timeout time in seconds
Solar_15.mode = minimalmodbus.MODE_RTU			
Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True


#configuration of SQ-618 ID=1
PAR_1 = minimalmodbus.Instrument('/dev/ttyUSB0',1)	# Make an "instrument" object called PAR_1 (port name, slave address (in decimal))
PAR_1.serial.baudrate = 19200 	
PAR_1.serial.bytesize = 8					# Number of data bits to be requested
PAR_1.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_1.serial.stopbits = 1					# Number of stop bits
PAR_1.serial.timeout  = 0.5					# Timeout time in seconds
PAR_1.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True

#configuration of SQ-618 ID=2
PAR_2 = minimalmodbus.Instrument('/dev/ttyUSB0',2)	
PAR_2.serial.baudrate = 19200 				# BaudRate
PAR_2.serial.bytesize = 8					# Number of data bits to be requested
PAR_2.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_2.serial.stopbits = 1					# Number of stop bits
PAR_2.serial.timeout  = 0.5					# Timeout time in seconds
PAR_2.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
PAR_2.clear_buffers_before_each_transaction = True
PAR_2.close_port_after_each_call = True


# Define a function to get the current date and time in the required format
def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y"), now.strftime("%H:%M")

# Define the file path for the CSV file
csv_file_path = "/home/cdacea/Sensors_modbus/Rpi-modbus/Light_comparison.csv"

try:
    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['Date', 'Time', 'PAR Intensity Zone B', 'PAR Intensity Zone C', 'Solar Radiation Zone B', 'Solar Radiation Zone C']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            date, time = get_datetime()

            try:
                # Read data from PAR_1
                PAR_intensity_1 = PAR_1.read_float(0, 3, 2, 0)
                sleep(10)
                writer.writerow({'Date': date, 'Time': time, 'PAR Intensity Zone B': PAR_intensity_1})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_1 at {now[1]} on {now[0]}: {e}")

            try:
                # Read data from PAR_2
                PAR_intensity_2 = PAR_2.read_float(0, 3, 2, 0)
                sleep(10)
                writer.writerow({'Date': date, 'Time': time, 'PAR Intensity Zone C': PAR_intensity_2})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_2 at {now[1]} on {now[0]}: {e}")

            try:
                # Read data from Solar_10
                Solar_Radiation_10 = Solar_10.read_float(0, 3, 2, 0)
                sleep(10)
                writer.writerow({'Date': date, 'Time': time, 'Solar Radiation Zone B': Solar_Radiation_10})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_10 at {now[1]} on {now[0]}: {e}")
                
            try:
                # Read data from Solar_15
                Solar_Radiation_15 = Solar_15.read_float(0, 3, 2, 0)
                sleep(10)
                writer.writerow({'Date': date, 'Time': time, 'Solar Radiation Zone C': Solar_Radiation_15})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_15 at {now[1]} on {now[0]}: {e}")


except KeyboardInterrupt:
    # Piece of mind close out
    Solar_10.serial.close()
    Solar_15.serial.close()
    PAR_1.serial.close()
    PAR_2.serial.close()
    print("Ports Closed")
