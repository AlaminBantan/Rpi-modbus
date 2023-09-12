import minimalmodbus 
from time import sleep


PAR_1 = minimalmodbus.Instrument('/dev/ttyUSB0', 1, debug=False)	
PAR_1.serial.baudrate = 19200 
PAR_1.serial.bytesize = 8					
PAR_1.serial.parity = minimalmodbus.serial.PARITY_EVEN	
PAR_1.serial.stopbits = 1				
PAR_1.serial.timeout  = 0.5				
PAR_1.mode = minimalmodbus.MODE_RTU				

PAR_2 = minimalmodbus.Instrument('/dev/ttyUSB0', 2, debug=False)	
PAR_2.serial.baudrate = 19200 				
PAR_2.serial.bytesize = 8					
PAR_2.serial.parity = minimalmodbus.serial.PARITY_EVEN	
PAR_2.serial.stopbits = 1					
PAR_2.serial.timeout  = 0.5					
PAR_2.mode = minimalmodbus.MODE_RTU				

Solar_10 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)	
Solar_10.serial.baudrate = 19200 
Solar_10.serial.baudrate = 19200 	
Solar_10.serial.bytesize = 8					
Solar_10.serial.parity = minimalmodbus.serial.PARITY_EVEN	
Solar_10.serial.stopbits = 1					
Solar_10.serial.timeout  = 0.5					
Solar_10.mode = minimalmodbus.MODE_RTU					

Solar_15 = minimalmodbus.Instrument('/dev/ttyUSB0', 15, debug=False)		
Solar_15.serial.baudrate = 19200 	
Solar_15.serial.bytesize = 8					
Solar_15.serial.parity = minimalmodbus.serial.PARITY_EVEN	
Solar_15.serial.stopbits = 1					
Solar_15.serial.timeout  = 0.5					
Solar_15.mode = minimalmodbus.MODE_RTU				


# Good practice to clean up before and after each execution
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True

PAR_2.clear_buffers_before_each_transaction = True
PAR_2.close_port_after_each_call = True

Solar_10.clear_buffers_before_each_transaction = True
Solar_10.close_port_after_each_call = True

Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True


# Open the CSV file for writing
with open('data_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date (mm/dd/yyyy)", "Time (hh:mm)", "PAR Intensity in Zone B", "PAR Intensity in Zone C", "Solar Radiation in Zone B", "Solar Radiation in Zone C"])

    try:
        while True: 
            # Get current date and time
            now = datetime.now()
            current_date = now.strftime("%m/%d/%Y")
            current_time = now.strftime("%H:%M")

            PAR_intensity_1 = PAR_1.read_float(0, 3, 2, 0) 

            PAR_intensity_2 = PAR_2.read_float(0, 3, 2, 0) 

            Solar_Radiation_10 = Solar_10.read_float(0, 3, 2, 0)

            Solar_Radiation_15 = Solar_15.read_float(0, 3, 2, 0)


            # Write the data to the CSV file
            writer.writerow([current_date, current_time, PAR_intensity_1, PAR_intensity_2, Solar_Radiation_10, Solar_Radiation_15])
            
            sleep(1)

    except KeyboardInterrupt:
        PAR_1.serial.close()
        PAR_2.serial.close()
        Solar_15.serial.close()
        Solar_10.serial.close()
        print("Ports Now Closed")