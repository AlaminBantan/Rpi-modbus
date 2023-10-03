import minimalmodbus # Don't forget to import the library!!
from time import sleep


Thum_20 = minimalmodbus.Instrument('/dev/ttyACM0', 240, debug=False)
Thum_20.serial.baudrate = 19200


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


