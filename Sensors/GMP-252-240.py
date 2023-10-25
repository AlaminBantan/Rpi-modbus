import minimalmodbus # Don't forget to import the library!!
from time import sleep



# Make an "instrument" object called carbo_240 (port name, slave address (in decimal))
carbo_240 = minimalmodbus.Instrument('/dev/ttyACM0',240)	

carbo_240.serial.baudrate = 19200 				# BaudRate
carbo_240.serial.bytesize = 8					# Number of data bits to be requested
carbo_240.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
carbo_240.serial.stopbits = 2					# Number of stop bits
carbo_240.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
carbo_240.clear_buffers_before_each_transaction = True
carbo_240.close_port_after_each_call = True


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		carbon_conc = carbo_240.read_float(1, 3, 2, 0)
		slave_2 = carbo_240.read_float(769,3,2,0)
		Baud_2 = carbo_240.read_float(770,3,2,0)
		Parity_2 = carbo_240.read_float(771,3,2,0)
		
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"CO2 concentration is: {carbon_conc} ppm")
		print(f"slaveid={slave_2}, Baud={Baud_2}, Parit={Parity_2}, Stopbit={Stopbit_2}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	carbo_240.serial.close()
	print("Ports Now Closed")
