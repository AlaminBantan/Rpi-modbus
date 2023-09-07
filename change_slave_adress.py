import minimalmodbus # Don't forget to import the library!!



mb_address = 1 # Modbus address of sensor

sensy = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called sensy (port name, slave address (in decimal))

sensy.serial.baudrate = 19200 				# BaudRate
sensy.serial.bytesize = 8					# Number of data bits to be requested
sensy.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
sensy.serial.stopbits = 1					# Number of stop bits
sensy.serial.timeout  = 0.5					# Timeout time in seconds
sensy.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
sensy.clear_buffers_before_each_transaction = True
sensy.close_port_after_each_call = True




try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		PAR_intensity = sensy.read_float(0, 3, 2, 0)
		Slave_ID = sensy.read_bit(48 , 2)
	
		
		print("\n"*25)
		print("Sensor Data--------------------------------")
		print(f"PAR Intensity is: {PAR_intensity} umol.m^-2.s^-1")
		print(f"Slave ID is: {Slave_ID} umol.m^-2.s^-1")
		print("------------------------------------------")
		
		
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	PAR_sensy.serial.close()
	print("Ports Now Closed")
