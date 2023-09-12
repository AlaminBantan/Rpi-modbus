import minimalmodbus # Don't forget to import the library!!
from time import sleep


mb_address = 1 # Modbus address of sensor

PAR_1 = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called PAR_1 (port name, slave address (in decimal))

PAR_1.serial.baudrate = 19200 				# BaudRate
PAR_1.serial.bytesize = 8					# Number of data bits to be requested
PAR_1.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_1.serial.stopbits = 1					# Number of stop bits
PAR_1.serial.timeout  = 0.5					# Timeout time in seconds
PAR_1.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		PAR_intensity = PAR_1.read_float(0, 3, 2, 0) 
		Slave = PAR_1.read_float(16,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"PAR Intensity is: {PAR_intensity} umol.m^-2.s^-1")
		print(f"Slave ID is: {Slave}")
		print("------------------------------------------")
		
		
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	PAR_1.serial.close()
	print("Ports Now Closed")