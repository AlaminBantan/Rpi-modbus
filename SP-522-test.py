import minimalmodbus # Don't forget to import the library!!
from time import sleep


mb_address = 6 # Modbus address of sensor

Solar_sensy = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called Solar_sensy (port name, slave address (in decimal))

Solar_sensy.serial.baudrate = 19200 				# BaudRate
Solar_sensy.serial.bytesize = 8					# Number of data bits to be requested
Solar_sensy.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_sensy.serial.stopbits = 1					# Number of stop bits
Solar_sensy.serial.timeout  = 0.5					# Timeout time in seconds
Solar_sensy.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
Solar_sensy.clear_buffers_before_each_transaction = True
Solar_sensy.close_port_after_each_call = True


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation = Solar_sensy.read_float(0, 3, 2, 0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {Solar_Radiation} W.m^-2")
		print("------------------------------------------")
		
		
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Solar_sensy.serial.close()
	print("Ports Now Closed")
