import minimalmodbus # Don't forget to import the library!!
from time import sleep


IR_1 = minimalmodbus.Instrument('/dev/ttyACM0', 1, debug=True)
IR_1.serial.baudrate = 1200
IR_1.serial.parity = minimalmodbus.serial.PARITY_EVEN
IR_1.serial.bytesize = 7
IR_1.serial.stopbits = 1

try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		IR = IR_1.read_float(1, 3, 2, 0)
	

	
		
		print("\n"*50)
		print(f"IR is:{IR}")

	
except KeyboardInterrupt:
	
	# Piece of mind close out
	IR_1.serial.close()
	print("Ports Now Closed")


