import minimalmodbus 
from time import sleep
import datetime
import csv

# Configuration of SQ-618 ID=1
PAR_1 = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
PAR_1.serial.baudrate = 19200
PAR_1.serial.bytesize = 8
PAR_1.serial.parity = minimalmodbus.serial.PARITY_EVEN
PAR_1.serial.stopbits = 1
PAR_1.serial.timeout = 0.5
PAR_1.mode = minimalmodbus.MODE_RTU
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True

# Configuration of SQ-618 ID=2
PAR_2 = minimalmodbus.Instrument('/dev/ttyUSB0', 2)
PAR_2.serial.baudrate = 19200
PAR_2.serial.bytesize = 8
PAR_2.serial.parity = minimalmodbus.serial.PARITY_EVEN
PAR_2.serial.stopbits = 1
PAR_2.serial.timeout = 0.5
PAR_2.mode = minimalmodbus.MODE_RTU
PAR_2.clear_buffers_before_each_transaction = True
PAR_2.close_port_after_each_call = True

# Configuration of SQ-618 ID=3
PAR_3 = minimalmodbus.Instrument('/dev/ttyUSB0', 3)
PAR_3.serial.baudrate = 19200
PAR_3.serial.bytesize = 8
PAR_3.serial.parity = minimalmodbus.serial.PARITY_EVEN
PAR_3.serial.stopbits = 1
PAR_3.serial.timeout = 0.5
PAR_3.mode = minimalmodbus.MODE_RTU
PAR_3.clear_buffers_before_each_transaction = True
PAR_3.close_port_after_each_call = True

# Configuration of SQ-618 ID=4
PAR_4 = minimalmodbus.Instrument('/dev/ttyUSB0', 4)
PAR_4.serial.baudrate = 19200
PAR_4.serial.bytesize = 8
PAR_4.serial.parity = minimalmodbus.serial.PARITY_EVEN
PAR_4.serial.stopbits = 1
PAR_4.serial.timeout = 0.5
PAR_4.mode = minimalmodbus.MODE_RTU
PAR_4.clear_buffers_before_each_transaction = True
PAR_4.close_port_after_each_call = True

# Configuration of SP-522 ID=11
Solar_11 = minimalmodbus.Instrument('/dev/ttyUSB0', 11, debug=False)
Solar_11.serial.baudrate = 19200
Solar_11.serial.bytesize = 8
Solar_11.serial.parity = minimalmodbus.serial.PARITY_EVEN
Solar_11.serial.stopbits = 1
Solar_11.serial.timeout = 0.5
Solar_11.mode = minimalmodbus.MODE_RTU
Solar_11.clear_buffers_before_each_transaction = True
Solar_11.close_port_after_each_call = True

# Configuration of SP-522 ID=12
Solar_12 = minimalmodbus.Instrument('/dev/ttyUSB0', 12, debug=False)
Solar_12.serial.baudrate = 19200
Solar_12.serial.bytesize = 8
Solar_12.serial.parity = minimalmodbus.serial.PARITY_EVEN
Solar_12.serial.stopbits = 1
Solar_12.serial.timeout = 0.5
Solar_12.mode = minimalmodbus.MODE_RTU
Solar_12.clear_buffers_before_each_transaction = True
Solar_12.close_port_after_each_call = True

# Configuration of SP-522 ID=13
Solar_13 = minimalmodbus.Instrument('/dev/ttyUSB0', 13, debug=False)
Solar_13.serial.baudrate = 19200
Solar_13.serial.bytesize = 8
Solar_13.serial.parity = minimalmodbus.serial.PARITY_EVEN
Solar_13.serial.stopbits = 1
Solar_13.serial.timeout = 0.5
Solar_13.mode = minimalmodbus.MODE_RTU
Solar_13.clear_buffers_before_each_transaction = True
Solar_13.close_port_after_each_call = True

# Configuration of SP-522 ID=14
Solar_14 = minimalmodbus.Instrument('/dev/ttyUSB0', 14, debug=False)
Solar_14.serial.baudrate = 19200
Solar_14.serial.bytesize = 8
Solar_14.serial.parity = minimalmodbus.serial.PARITY_EVEN
Solar_14.serial.stopbits = 1
Solar_14.serial.timeout = 0.5
Solar_14.mode = minimalmodbus.MODE_RTU
Solar_14.clear_buffers_before_each_transaction = True
Solar_14.close_port_after_each_call = True

# Configuration of GMP-252 ID=41
carbo_41 = minimalmodbus.Instrument('/dev/ttyUSB0', 41)
carbo_41.serial.baudrate = 19200
carbo_41.serial.bytesize = 8
carbo_41.serial.parity = minimalmodbus.serial.PARITY_NONE
carbo_41.serial.stopbits = 2
carbo_41.mode = minimalmodbus.MODE_RTU
carbo_41.clear_buffers_before_each_transaction = True
carbo_41.close_port_after_each_call = True

# Configuration of GMP-252 ID=42
carbo_42 = minimalmodbus.Instrument('/dev/ttyUSB0', 42)
carbo_42.serial.baudrate = 19200
carbo_42.serial.bytesize = 8
carbo_42.serial.parity = minimalmodbus.serial.PARITY_NONE
carbo_42.serial.stopbits = 2
carbo_42.mode = minimalmodbus.MODE_RTU
carbo_42.clear_buffers_before_each_transaction = True
carbo_42.close_port_after_each_call = True

# Define a function to get the current date and time in the required format
def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y"), now.strftime("%H:%M")

# Define the file path for the CSV file
PAR_csv_file_path = "/home/cdacea/GH_data/PAR.csv"
Solar_csv_file_path = "/home/cdacea/GH_data/Solar.csv"
Carbon_csv_file_path = "/home/cdacea/GH_data/Carbon.csv"

try:

    with open(PAR_csv_file_path, mode='a', newline='') as csv_file:
        fieldnames = ['Date', 'Time', 'Zone', 'Subzone', 'PAR']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

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

    with open(Solar_csv_file_path, mode='a', newline='') as csv_file:
        fieldnames = ['Date', 'Time', 'Zone', 'Subzone', 'Solar radiation']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        while True:
            date, time = get_datetime()

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

    with open(Carbon_csv_file_path, mode='a', newline='') as csv_file:
        fieldnames = ['Date', 'Time', 'Zone', 'Subzone', 'CO2 ppm']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        while True:
            date, time = get_datetime()
            try:
                carbon_conc_41 = carbo_41.read_float(1, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "1", 'CO2 ppm': carbon_conc_41})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading carbo_41 at {now[1]} on {now[0]}: {e}")
            try:
                carbon_conc_42 = carbo_42.read_float(1, 3, 2, 0)
                sleep(4)
                writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "1", 'CO2 ppm': carbon_conc_42})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading carbo_42 at {now[1]} on {now[0]}: {e}")

except KeyboardInterrupt:
    # Close serial ports only if they are open
    if carbo_41.serial.is_open:
        carbo_41.serial.close()
    if carbo_42.serial.is_open:
        carbo_42.serial.close()

    if Solar_11.serial.is_open:
        Solar_11.serial.close()
    if Solar_12.serial.is_open:
        Solar_12.serial.close()
    if Solar_13.serial.is_open:
        Solar_13.serial.close()
    if Solar_14.serial.is_open:
        Solar_14.serial.close()

    if PAR_1.serial.is_open:
        PAR_1.serial.close()
    if PAR_2.serial.is_open:
        PAR_2.serial.close()
    if PAR_3.serial.is_open:
        PAR_3.serial.close()
    if PAR_4.serial.is_open:
        PAR_4.serial.close()

    print("Ports Closed")