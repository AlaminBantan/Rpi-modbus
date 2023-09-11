import minimalmodbus 
from time import sleep


PAR_1 = minimalmodbus.Instrument('/dev/ttyUSB0',1)	# Make an "instrument" object called PAR_1 (port name, slave address (in decimal))
PAR_1.serial.baudrate = 19200 

PAR_2 = minimalmodbus.Instrument('/dev/ttyUSB0',2)	# Make an "instrument" object called PAR_2 (port name, slave address (in decimal))
PAR_2.serial.baudrate = 19200 			

Solar_15 = minimalmodbus.Instrument('/dev/ttyUSB0', 15, debug=False)	# Make an "instrument" object called Solar_15 (port name, slave address (in decimal))
Solar_15.serial.baudrate = 19200 		

Solar_10 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)	# Make an "instrument" object called Solar_10 (port name, slave address (in decimal))
Solar_10.serial.baudrate = 19200 		


# Good practice to clean up before and after each execution
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True

PAR_2.clear_buffers_before_each_transaction = True
PAR_2.close_port_after_each_call = True

Solar_10.clear_buffers_before_each_transaction = True
Solar_10.close_port_after_each_call = True

Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		PAR_intensity_1 = PAR_1.read_float(0, 3, 2, 0) 
		Slave_1 = PAR_1.read_float(16,3,2,0)
		Baud_1 = PAR_1.read_float(22,3,2,0)
		
		PAR_intensity_2 = PAR_2.read_float(0, 3, 2, 0) 
		Slave_2 = PAR_2.read_float(16,3,2,0)
		Baud_2 = PAR_2.read_float(22,3,2,0)

		Solar_Radiation_10 = Solar_10.read_float(0, 3, 2, 0)
		slave_10 = Solar_10.read_float(16,3,2,0)
		Baud_10 = Solar_10.read_float(22,3,2,0)
		
		Solar_Radiation_15 = Solar_15.read_float(0, 3, 2, 0)
		slave_15 = Solar_15.read_float(16,3,2,0)
		Baud_15 = Solar_15.read_float(22,3,2,0)
	
		
		print("\n"*20)
		print("Sensor Data in Zone B:")
		print("--------------------------------")
		print(f"PAR Intensity in Zone B is: {PAR_intensity_1} umol.m^-2.s^-1")
		print(f"Slave ID is: {Slave_1} and the Baud rate is {Baud_1}")
		print(f"Solar radiation in zone B is: {Solar_Radiation_10} W.m^-2")
		print(f"Slave Id of pyranometer in zone B is: {slave_10} and Baud rate is {Baud_10}")
		print("Sensor Data in Zone C:")
		print("--------------------------------")
		print(f"PAR Intensity in Zone B is: {PAR_intensity_2} umol.m^-2.s^-1")
		print(f"Slave ID is: {Slave_2} and the Baud rate is {Baud_2}")
		print(f"Solar radiation in zone C is: {Solar_Radiation_15} W.m^-2")
		print(f"Slave Id of pyranometer in zone C is: {slave_15} and Baud rate is {Baud_15}")
		print("------------------------------------------")
		
		
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
		# Piece of mind close out
	PAR_1.serial.close()
	PAR_2.serial.close()
	Solar_15.serial.close()
	Solar_10.serial.close()
	print("Ports Now Closed")