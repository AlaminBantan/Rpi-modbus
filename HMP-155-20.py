import minimalmodbus # Don't forget to import the library!!
from time import sleep


Thum_20 = minimalmodbus.Instrument('/dev/ttyACM0', 240, debug=False)
Thum_20.serial.baudrate = 4800
Thum_20.serial.bytesize = 7					# Number of data bits to be requested
Thum_20.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Thum_20.serial.stopbits = 1					# Number of stop bits
Thum_20.mode = minimalmodbus.MODE_RTU	

try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Relative_humidity_20 = Thum_20.read_float(1, 3, 2, 0)
		Temperature_20 = Thum_20.read_float(3,3,2,0)

	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Humidity is: {Relative_humidity_20} %RH and Temp is: {Temperature_20} C")


		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Thum_20.serial.close()
	print("Ports Now Closed")


