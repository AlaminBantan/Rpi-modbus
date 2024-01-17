import minimalmodbus 
from time import sleep
import datetime
import csv
import os

# Configuration of SQ-618 ID=5
PAR_5 = minimalmodbus.Instrument('/dev/ttyACM0', 5)
PAR_5.serial.baudrate = 19200
PAR_5.serial.bytesize = 8
PAR_5.serial.parity = minimalmodbus.serial.PARITY_EVEN
PAR_5.serial.stopbits = 1
PAR_5.serial.timeout = 0.5
PAR_5.mode = minimalmodbus.MODE_RTU
PAR_5.clear_buffers_before_each_transaction = True
PAR_5.close_port_after_each_call = True

# Configuration of SP-522 ID=10
Solar_15 = minimalmodbus.Instrument('/dev/ttyACM0', 15)
Solar_15.serial.baudrate = 19200
Solar_15.serial.bytesize = 8
Solar_15.serial.parity = minimalmodbus.serial.PARITY_EVEN
Solar_15.serial.stopbits = 1
Solar_15.serial.timeout = 0.5
Solar_15.mode = minimalmodbus.MODE_RTU
Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True



# Define a function to get the current date and time in the required format
def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y"), now.strftime("%H:%M")

# Define the file path for the CSV file
Climatic_data_pathway = "/home/cdacea/south_GH/south_climatic_data.csv"

# Check if the file is empty
file_exists = os.path.exists(Climatic_data_pathway) and os.path.getsize(Climatic_data_pathway) > 0

try:
    with open(Climatic_data_pathway, mode='a', newline='') as csv_file:
        fieldnames = ['Date', 'Time', 'PAR_south', 'Solar_radiation_south']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header only if the file is empty
        if not file_exists:
            writer.writeheader()



        while True:
            date, time = get_datetime()

            try:
                # Read data from PAR_5
                PAR_intensity_5 = PAR_5.read_float(0, 3, 2, 0)
                sleep(5)
                writer.writerow({'Date': date, 'Time': time, 'PAR_south': PAR_intensity_5})
                sleep(5)
            except Exception as e:
                now = get_datetime()
                print(f"Error reading PAR_5 at {now[1]} on {now[0]}: {e}")


            try:
                # Read data from Solar_15
                Solar_Radiation_15 = Solar_15.read_float(0, 3, 2, 0)
                sleep(5)
                writer.writerow({'Date': date, 'Time': time, 'Solar_radiation_south': Solar_Radiation_15})
                sleep(5)
            except Exception as e:
                now = get_datetime()
                print(f"Error reading Solar_15 at {now[1]} on {now[0]}: {e}")


except KeyboardInterrupt:
    # Close serial ports only if they are open
    if Solar_15.serial.is_open:
        Solar_15.serial.close()

    if PAR_5.serial.is_open:
        PAR_5.serial.close()

    print("Ports Closed")
