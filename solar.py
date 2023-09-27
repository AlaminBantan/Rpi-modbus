
#Test
import minimalmodbus
from time import sleep

id = 13
time_it = 10
c = 0
n_inst = minimalmodbus.Instrument('/dev/ttyUSB0', id, debug=False)  # port name, slave address (in decimal)
n_inst.serial.baudrate = 9600
#n_inst.serial.parity = minimalmodbus.serial.PARITY_EVEN


try:
	while True:
		
		# ~ read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) 
		Solar_Radiation_12 = n_inst.read_float(0, 3, 2, 0)
		slave_12 = n_inst.read_float(16,3,2,0)
		Baud_12 = n_inst.read_float(22,3,2,0)
		Parity_12 = n_inst.read_float(24,3,2,0)
		Stopbit_12 = n_inst.read_float(26,3,2,0)
	
		
		print("\n"*50)
		print("Sensor Data--------------------------------")
		print(f"Solar radiation is: {Solar_Radiation_12} W.m^-2")
		print(f"slaveid={slave_12}, Baud={Baud_12}, Parit={Parity_12}, Stopbit={Stopbit_12}")

		print("------------------------------------------")
		
		print("")
		print("")
		print("")
		sleep(1)
	
except KeyboardInterrupt:
	
	# Piece of mind close out
	n_inst.serial.close()
	print("Ports Now Closed")
