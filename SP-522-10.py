import minimalmodbus # Don't forget to import the library!!
from time import sleep



Solar_10 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)	# Make an "instrument" object called Solar_10 (port name, slave address (in decimal))
Solar_10.serial.baudrate = 19200 	



# Good practice to clean up before and after each execution
Solar_10.clear_buffers_before_each_transaction = True
Solar_10.close_port_after_each_call = True


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation = Solar_10.read_float(0, 3, 2, 0)
		slave = Solar_10.read_float(16,3,2,0)
		Baud = Solar_10.read_float(22,3,2,0)
		Parity = Solar_10.read_float(24,3,2,0)
		Stopbit = Solar_10.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {Solar_Radiation} W.m^-2")
		print(f"slaveid={slave}, Baud={Baud}, Parit={Parity}, Stopbit={Stopbit}")

		print("------------------------------------------")
		
		
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Solar_10.serial.close()
	print("Ports Now Closed")
