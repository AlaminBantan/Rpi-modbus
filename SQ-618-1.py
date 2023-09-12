import minimalmodbus # Don't forget to import the library!!
from time import sleep

PAR_1 = minimalmodbus.Instrument('/dev/ttyUSB0',1)	# Make an "instrument" object called PAR_1 (port name, slave address (in decimal))

PAR_1.serial.baudrate = 19200 	

# Good practice to clean up before and after each execution
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		PAR_intensity_1 = PAR_1.read_float(0, 3, 2, 0) 
		Slave_1 = PAR_1.read_float(16,3,2,0)
		Baud_1=PAR_1.read_float(22, 3, 2  0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"PAR Intensity is: {PAR_intensity_1} umol.m^-2.s^-1")
		print(f"Slave ID is: {Slave_1}, baud rate is {Baud_1}")
		print("------------------------------------------")
		
		
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	PAR_1.serial.close()
	print("Ports Now Closed")
