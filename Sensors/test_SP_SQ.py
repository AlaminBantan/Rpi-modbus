import minimalmodbus # Don't forget to import the library!!
from time import sleep

#configuration of SP-522 ID=11
Solar_11 = minimalmodbus.Instrument('/dev/ttyACM0', 11, debug=False)
Solar_11.serial.baudrate = 19200 	
Solar_11.serial.bytesize = 8					# Number of data bits to be requested
Solar_11.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
Solar_11.serial.stopbits = 1					# Number of stop bits
Solar_11.serial.timeout  = 0.5					# Timeout time in seconds
Solar_11.mode = minimalmodbus.MODE_RTU			
Solar_11.clear_buffers_before_each_transaction = True
Solar_11.close_port_after_each_call = True


#configuration of SP-522 ID=13
Solar_13 = minimalmodbus.Instrument('/dev/ttyACM0', 13, debug=False)
Solar_13.serial.baudrate = 19200 	
Solar_13.serial.bytesize = 8					# Number of data bits to be requested
Solar_13.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
Solar_13.serial.stopbits = 1					# Number of stop bits
Solar_13.serial.timeout  = 0.5					# Timeout time in seconds
Solar_13.mode = minimalmodbus.MODE_RTU			
Solar_13.clear_buffers_before_each_transaction = True
Solar_13.close_port_after_each_call = True


#configuration of SQ-618 ID=1
PAR_1 = minimalmodbus.Instrument('/dev/ttyACM0',1)	# Make an "instrument" object called PAR_1 (port name, slave address (in decimal))
PAR_1.serial.baudrate = 19200 	
PAR_1.serial.bytesize = 8					# Number of data bits to be requested
PAR_1.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
PAR_1.serial.stopbits = 1					# Number of stop bits
PAR_1.serial.timeout  = 0.5					# Timeout time in seconds
PAR_1.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True

#configuration of SQ-618 ID=2
PAR_2 = minimalmodbus.Instrument('/dev/ttyACM0',3)	
PAR_2.serial.baudrate = 19200 				# BaudRate
PAR_2.serial.bytesize = 8					# Number of data bits to be requested
PAR_2.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
PAR_2.serial.stopbits = 1					# Number of stop bits
PAR_2.serial.timeout  = 0.5					# Timeout time in seconds
PAR_2.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
PAR_2.clear_buffers_before_each_transaction = True
PAR_2.close_port_after_each_call = True



try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation_11 = Solar_11.read_float(0, 3, 2, 0)
		slave_11 = Solar_11.read_float(16,3,2,0)
		Baud_11 = Solar_11.read_float(22,3,2,0)
		Parity_11 = Solar_11.read_float(24,3,2,0)
		Stopbit_11 = Solar_11.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {Solar_Radiation_11} W.m^-2")
		print(f"slaveid={slave_11}, Baud={Baud_11}, Parit={Parity_11}, Stopbit={Stopbit_11}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Solar_11.serial.close()
	print("Port 11 Now Closed")


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation_13 = Solar_13.read_float(0, 3, 2, 0)
		slave_13 = Solar_13.read_float(16,3,2,0)
		Baud_13 = Solar_13.read_float(22,3,2,0)
		Parity_13 = Solar_13.read_float(24,3,2,0)
		Stopbit_13 = Solar_13.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {Solar_Radiation_13} W.m^-2")
		print(f"slaveid={slave_13}, Baud={Baud_13}, Parit={Parity_13}, Stopbit={Stopbit_13}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Solar_13.serial.close()
	print("Port 13 Now Closed")

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
		print(f"PAR intensity is: {PAR_intensity_1} umol.m^-2")
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



try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		PAR_intensity_2 = PAR_2.read_float(0, 3, 2, 0)
		slave_2 = PAR_2.read_float(16,3,2,0)
		Baud_2 = PAR_2.read_float(22,3,2,0)
		Parity_2 = PAR_2.read_float(24,3,2,0)
		Stopbit_2 = PAR_2.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"PAR intensity is: {PAR_intensity_2} umol.m^-2")
		print(f"slaveid={slave_2}, Baud={Baud_2}, Parit={Parity_2}, Stopbit={Stopbit_2}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	PAR_2.serial.close()
	print("Port 2 Now Closed")
