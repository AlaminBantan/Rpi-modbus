import minimalmodbus 
from time import sleep
import datetime
import csv
import serial
import time
import io

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

#configuration of SP-522 ID=11
Solar_11 = minimalmodbus.Instrument('/dev/ttyUSB0', 11, debug=False)
Solar_11.serial.baudrate = 19200
Solar_11.serial.bytesize = 8					# Number of data bits to be requested
Solar_11.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_11.serial.stopbits = 1					# Number of stop bits
Solar_11.serial.timeout  = 0.5					# Timeout time in seconds
Solar_11.mode = minimalmodbus.MODE_RTU			
Solar_11.clear_buffers_before_each_transaction = True
Solar_11.close_port_after_each_call = True

#configuration of SP-522 ID=12
Solar_12 = minimalmodbus.Instrument('/dev/ttyUSB0', 12, debug=False)
Solar_12.serial.baudrate = 19200
Solar_12.serial.bytesize = 8					# Number of data bits to be requested
Solar_12.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_12.serial.stopbits = 1					# Number of stop bits
Solar_12.serial.timeout  = 0.5					# Timeout time in seconds
Solar_12.mode = minimalmodbus.MODE_RTU	
Solar_12.clear_buffers_before_each_transaction = True
Solar_12.close_port_after_each_call = True

#configuration of SP-522 ID=13
Solar_13 = minimalmodbus.Instrument('/dev/ttyUSB0', 13, debug=False)
Solar_13.serial.baudrate = 19200
Solar_13.serial.bytesize = 8					# Number of data bits to be requested
Solar_13.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_13.serial.stopbits = 1					# Number of stop bits
Solar_13.serial.timeout  = 0.5					# Timeout time in seconds
Solar_13.mode = minimalmodbus.MODE_RTU			
Solar_13.clear_buffers_before_each_transaction = True
Solar_13.close_port_after_each_call = True

#configuration of SP-522 ID=14
Solar_14 = minimalmodbus.Instrument('/dev/ttyUSB0', 14, debug=False)
Solar_14.serial.baudrate = 19200
Solar_14.serial.bytesize = 8					# Number of data bits to be requested
Solar_14.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_14.serial.stopbits = 1					# Number of stop bits
Solar_14.serial.timeout  = 0.5					# Timeout time in seconds
Solar_14.mode = minimalmodbus.MODE_RTU	
Solar_14.clear_buffers_before_each_transaction = True
Solar_14.close_port_after_each_call = True

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


#configuration of SQ-618 ID=3
PAR_3 = minimalmodbus.Instrument('/dev/ttyUSB0',3)	# Make an "instrument" object called PAR_3 (port name, slave address (in decimal))
PAR_3.serial.baudrate = 19200 	
PAR_3.serial.bytesize = 8					# Number of data bits to be requested
PAR_3.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_3.serial.stopbits = 1					# Number of stop bits
PAR_3.serial.timeout  = 0.5					# Timeout time in seconds
PAR_3.mode = minimalmodbus.MODE_RTU	
PAR_3.clear_buffers_before_each_transaction = True
PAR_3.close_port_after_each_call = True


#configuration of SQ-618 ID=4
PAR_4 = minimalmodbus.Instrument('/dev/ttyUSB0',4)	# Make an "instrument" object called PAR_4 (port name, slave address (in decimal))
PAR_4.serial.baudrate = 19200 	
PAR_4.serial.bytesize = 8					# Number of data bits to be requested
PAR_4.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_4.serial.stopbits = 1					# Number of stop bits
PAR_4.serial.timeout  = 0.5					# Timeout time in seconds
PAR_4.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
PAR_4.clear_buffers_before_each_transaction = True
PAR_4.close_port_after_each_call = True

#configuration of SQ-618 ID=5
PAR_5 = minimalmodbus.Instrument('/dev/ttyUSB0',5)	# Make an "instrument" object called PAR_5 (port name, slave address (in decimal))
PAR_5.serial.baudrate = 19200 	
PAR_5.serial.bytesize = 8					# Number of data bits to be requested
PAR_5.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_5.serial.stopbits = 1					# Number of stop bits
PAR_5.serial.timeout  = 0.5					# Timeout time in seconds
PAR_5.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
PAR_5.clear_buffers_before_each_transaction = True
PAR_5.close_port_after_each_call = True

#configuration of SQ-618 ID=6
PAR_6 = minimalmodbus.Instrument('/dev/ttyUSB0',6)	# Make an "instrument" object called PAR_6 (port name, slave address (in decimal))
PAR_6.serial.baudrate = 19200 	
PAR_6.serial.bytesize = 8					# Number of data bits to be requested
PAR_6.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_6.serial.stopbits = 1					# Number of stop bits
PAR_6.serial.timeout  = 0.5					# Timeout time in seconds
PAR_6.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
PAR_6.clear_buffers_before_each_transaction = True
PAR_6.close_port_after_each_call = True


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




# Define a function to get the current date and time in the required format
def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y"), now.strftime("%H:%M")

# Define the file path for the CSV file
csv_file_path = "/home/cdacea/Sensors_modbus/Rpi-modbus/Light_comparison.csv"

try:
    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['Date',
                       'Time',
                       'Zone',
                       'Subzone',
                       'PAR',
                       'Solar radiation',
                       'Surface temperature',
                       'Ambient temperature',
                       'Relative humidity',
                       'CO2 Concentration']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            date, time = get_datetime()

            try:
                # Read data from PAR_1
                PAR_intensity_1 = PAR_1.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "1", 'PAR': PAR_intensity_1})

            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_1 at {now[1]} on {now[0]}: {e}")

            try:
                # Read data from PAR_2
                PAR_intensity_2 = PAR_2.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "2", 'PAR': PAR_intensity_2})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_2 at {now[1]} on {now[0]}: {e}")

            try:
                # Read data from PAR_3
                PAR_intensity_3 = PAR_3.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "3", 'PAR': PAR_intensity_3})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_3 at {now[1]} on {now[0]}: {e}")
            

            try:
                # Read data from PAR_4
                PAR_intensity_4 = PAR_4.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "1", 'PAR': PAR_intensity_4})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_4 at {now[1]} on {now[0]}: {e}")


            try:
                # Read data from PAR_5
                PAR_intensity_5 = PAR_5.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "2", 'PAR': PAR_intensity_5})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_5 at {now[1]} on {now[0]}: {e}")


            try:
                # Read data from PAR_6
                PAR_intensity_6 = PAR_6.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "3", 'PAR': PAR_intensity_6})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_2 at {now[1]} on {now[0]}: {e}")


            try:
                # Read data from Solar_10
                Solar_Radiation_10 = Solar_10.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "1", 'Solar radiation': Solar_Radiation_10})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_10 at {now[1]} on {now[0]}: {e}")
                

            try:
                # Read data from Solar_11
                Solar_Radiation_11 = Solar_11.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "2", 'Solar radiation': Solar_Radiation_11})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_11 at {now[1]} on {now[0]}: {e}")
    

            try:
                # Read data from Solar_12
                Solar_Radiation_12 = Solar_12.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "3", 'Solar radiation': Solar_Radiation_12})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_12 at {now[1]} on {now[0]}: {e}")


            try:
                # Read data from Solar_13
                Solar_Radiation_13 = Solar_13.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "1", 'Solar radiation': Solar_Radiation_13})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_13 at {now[1]} on {now[0]}: {e}")

                
            try:
                # Read data from Solar_14
                Solar_Radiation_14 = Solar_14.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "2", 'Solar radiation': Solar_Radiation_14})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_14 at {now[1]} on {now[0]}: {e}")
    

            try:
                # Read data from Solar_15
                Solar_Radiation_15 = Solar_15.read_float(0, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "3", 'Solar radiation': Solar_Radiation_15})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_15 at {now[1]} on {now[0]}: {e}")


            try:
                # Read data from IR_0
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
                    writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "1", 'Surface temperature': data_0})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading IR_0 at {now[1]} on {now[0]}: {e}")

            try:
                # Read data from IR_1
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
                    writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "2", 'Surface temperature': data_1})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading IR_1 at {now[1]} on {now[0]}: {e}")

            try:
                # Read data from IR_2
                command_2 = "2M!\r"
                IR_2.write(command_2)
                IR_2.flush()
                time.sleep(2)
                # read bit
                data_str_2 ="2D0!\r"
                IR_2.write(data_str_2)
                data_2 = IR_2.readline()
                IR_2.flush()
                time.sleep(2)
                if len(data_2.split('+'))> 1:
                    writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "3", 'Surface temperature': data_2})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading IR_2 at {now[0]} on {now[1]}: {e}")

            try:
                # Read data from IR_3
                command_3 = "3M!\r"
                IR_3.write(command_3)
                IR_3.flush()
                time.sleep(3)
                # read bit
                data_str_3 ="3D0!\r"
                IR_3.write(data_str_3)
                data_3 = IR_3.readline()
                IR_3.flush()
                time.sleep(3)
                if len(data_3.split('+'))> 1:
                    writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "1", 'Surface temperature': data_3})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading IR_3 at {now[0]} on {now[1]}: {e}")

            try:
                # Read data from IR_4
                command_4 = "4M!\r"
                IR_4.write(command_4)
                IR_4.flush()
                time.sleep(4)
                # read bit
                data_str_4 ="4D0!\r"
                IR_4.write(data_str_4)
                data_4 = IR_4.readline()
                IR_4.flush()
                time.sleep(4)
                if len(data_4.split('+'))> 1:
                    writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "2", 'Surface temperature': data_4})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading IR_4 at {now[0]} on {now[1]}: {e}")

            try:
                # Read data from IR_5
                command_5 = "5M!\r"
                IR_5.write(command_5)
                IR_5.flush()
                time.sleep(5)
                # read bit
                data_str_5 ="5D0!\r"
                IR_5.write(data_str_5)
                data_5 = IR_5.readline()
                IR_5.flush()
                time.sleep(5)
                if len(data_5.split('+'))> 1:
                    writer.writerow({'Date': date, 'Time': time, 'Zone': "C", 'Subzone': "3", 'Surface temperature': data_5})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading IR_5 at {now[0]} on {now[1]}: {e}")




except KeyboardInterrupt:
    # Piece of mind close out
    Solar_10.serial.close()
    Solar_11.serial.close()
    Solar_12.serial.close()
    Solar_13.serial.close()
    Solar_14.serial.close()
    Solar_15.serial.close()
    PAR_1.serial.close()
    PAR_2.serial.close()
    PAR_3.serial.close()
    PAR_4.serial.close()
    PAR_5.serial.close()
    PAR_6.serial.close()
    print("Ports Closed")
