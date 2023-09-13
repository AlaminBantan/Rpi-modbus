import minimalmodbus # Don't forget to import the library!!
from time import sleep

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



try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation_10 = Solar_10.read_float(0, 3, 2, 0)
		slave_10 = Solar_10.read_float(16,3,2,0)
		Baud_10 = Solar_10.read_float(22,3,2,0)
		Parity_10 = Solar_10.read_float(24,3,2,0)
		Stopbit_10 = Solar_10.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {Solar_Radiation_10} W.m^-2")
		print(f"slaveid={slave_10}, Baud={Baud_10}, Parit={Parity_10}, Stopbit={Stopbit_10}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Solar_10.serial.close()
	print("Port 10 Now Closed")


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation_15 = Solar_15.read_float(0, 3, 2, 0)
		slave_15 = Solar_15.read_float(16,3,2,0)
		Baud_15 = Solar_15.read_float(22,3,2,0)
		Parity_15 = Solar_15.read_float(24,3,2,0)
		Stopbit_15 = Solar_15.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {Solar_Radiation_15} W.m^-2")
		print(f"slaveid={slave_15}, Baud={Baud_15}, Parit={Parity_15}, Stopbit={Stopbit_15}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Solar_15.serial.close()
	print("Port 15 Now Closed")

try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		PAR_intensity_1 = PAR_1.read_float(0, 3, 2, 0)
		slave_1 = PAR_1.read_float(16,3,2,0)
		Baud_1 = PAR_1.read_float(22,3,2,0)
		Parity_1 = PAR_1.read_float(24,3,2,0)
		Stopbit_1 = PAR_1.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {PAR_intensity_1} W.m^-2")
		print(f"slaveid={slave_1}, Baud={Baud_1}, Parit={Parity_1}, Stopbit={Stopbit_1}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	PAR_1.serial.close()
	print("Port 1 Now Closed")
