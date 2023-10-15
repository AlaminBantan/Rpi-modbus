import minimalmodbus 
from time import sleep


Thum_240 = minimalmodbus.Instrument('/dev/ttyACM0', 240, debug=True)
Thum_240.serial.baudrate = 4800
Thum_240.serial.parity = minimalmodbus.serial.PARITY_EVEN
Thum_240.serial.bytesize = 7
Thum_240.serial.stopbits = 1
Thum_240.mode = minimalmodbus.MODE_ASCII		

try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Relative_humidity_240 = Thum_240.read_float(1, 3, 2, 0)
		Temperature_240 = Thum_240.read_float(3, 3, 2, 0)

	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Humidity is: {Relative_humidity_240} %RH and Temp is: {Temperature_240} C")


		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	Thum_240.serial.close()
	print("Ports Now Closed")


