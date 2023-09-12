import minimalmodbus # Don't forget to import the library!!
from time import sleep


Solar_15 = minimalmodbus.Instrument('/dev/ttyUSB0', 15, debug=False)	# Make an "instrument" object called Solar_15 (port name, slave address (in decimal))
Solar_15.serial.baudrate = 19200 		

Solar_15 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)	# Make an "instrument" object called Solar_15 (port name, slave address (in decimal))
Solar_15.serial.baudrate = 19200 		


# Good practice to clean up before and after each execution
Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True

Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation_10 = Solar_15.read_float(0, 3, 2, 0)
		slave_10 = Solar_15.read_float(16,3,2,0)
		Baud_10 = Solar_15.read_float(22,3,2,0)
		
		Solar_Radiation_15 = Solar_15.read_float(0, 3, 2, 0)
		slave_15 = Solar_15.read_float(16,3,2,0)
		Baud_15 = Solar_15.read_float(22,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation in zone B is: {Solar_Radiation_10} W.m^-2")
		print(f"Slave Id of pyranometer in zone B is: {slave_10} and Baud rate is {Baud_10}")
		print(f"Solar radiation in zone C is: {Solar_Radiation_15} W.m^-2")
		print(f"Slave Id of pyranometer in zone C is: {slave_15} and Baud rate is {Baud_15}")
		print("------------------------------------------")
		
		
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	Solar_15.serial.close()
	Solar_15.serial.close()
	print("Ports Now Closed")