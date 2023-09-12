import minimalmodbus 
from time import sleep

#configuration of first Par sensor
PAR_1 = minimalmodbus.Instrument('/dev/ttyUSB0', 1, debug=False)	
PAR_1.serial.baudrate = 19200 
PAR_1.serial.bytesize = 8					
PAR_1.serial.parity = minimalmodbus.serial.PARITY_EVEN	
PAR_1.serial.stopbits = 1				
PAR_1.serial.timeout  = 0.5				
PAR_1.mode = minimalmodbus.MODE_RTU				

#configuration of second Par sensor
PAR_2 = minimalmodbus.Instrument('/dev/ttyUSB0', 2, debug=False)	
PAR_2.serial.baudrate = 19200 				
PAR_2.serial.bytesize = 8					
PAR_2.serial.parity = minimalmodbus.serial.PARITY_EVEN	
PAR_2.serial.stopbits = 1					
PAR_2.serial.timeout  = 0.5					
PAR_2.mode = minimalmodbus.MODE_RTU				

#configuration of first pyranometer
Solar_10 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)	
Solar_10.serial.baudrate = 19200 Solar_10.serial.baudrate = 19200 	
Solar_10.serial.bytesize = 8					
Solar_10.serial.parity = minimalmodbus.serial.PARITY_EVEN	
Solar_10.serial.stopbits = 1					
Solar_10.serial.timeout  = 0.5					
Solar_10.mode = minimalmodbus.MODE_RTU					

#configuration of second pyranometer
Solar_15 = minimalmodbus.Instrument('/dev/ttyUSB0', 15, debug=False)		
Solar_15.serial.baudrate = 19200 	
Solar_15.serial.bytesize = 8					
Solar_15.serial.parity = minimalmodbus.serial.PARITY_EVEN	
Solar_15.serial.stopbits = 1					
Solar_15.serial.timeout  = 0.5					
Solar_15.mode = minimalmodbus.MODE_RTU				


# Good practice to clean up before and after each execution
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True

PAR_2.clear_buffers_before_each_transaction = True
PAR_2.close_port_after_each_call = True

Solar_10.clear_buffers_before_each_transaction = True
Solar_10.close_port_after_each_call = True

Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True


try:
	while True: 
		PAR_intensity_1 = PAR_1.read_float(0,3,2,0) 
		Slave_1 = PAR_1.read_float(16,3,2,0)
		Baud_1 = PAR_1.read_float(22,3,2,0)
		print(f"PAR Intensity in Zone B is: {PAR_intensity_1} umol.m^-2.s^-1")
		sleep(1)
except KeyboardInterrupt:
	PAR_1.serial.close()
	
try:
	while True:
		PAR_intensity_2 = PAR_2.read_float(0,3,2,0) 
		Slave_2 = PAR_2.read_float(16,3,2,0)
		Baud_2 = PAR_2.read_float(22,3,2,0)
		print(f"PAR Intensity in Zone C is: {PAR_intensity_2} umol.m^-2.s^-1")		
		sleep(1)
except KeyboardInterrupt:
	PAR_2.serial.close()

try:
	while True:
		Solar_Radiation_10 = Solar_10.read_float(0,3,2,0)
		slave_10 = Solar_10.read_float(16,3,2,0)
		Baud_10 = Solar_10.read_float(22,3,2,0)
		print(f"Solar radiation in zone B is: {Solar_Radiation_10} W.m^-2")
		sleep(1)
except KeyboardInterrupt:
	Solar_10.serial.close()

try:
	while True:
		Solar_Radiation_15 = Solar_15.read_float(0,3,2,0)
		slave_15 = Solar_15.read_float(16,3,2,0)
		Baud_15 = Solar_15.read_float(22,3,2,0)
		print(f"Solar radiation in zone C is: {Solar_Radiation_15} W.m^-2")
		sleep(1)
except KeyboardInterrupt:
	Solar_15.serial.close()
	print("Ports Now Closed")




	




	#	print("\n"*20)
	#	print("Sensor Data in Zone B:")
	#	print("--------------------------------")
	#	print(f"PAR Intensity in Zone B is: {PAR_intensity_1} umol.m^-2.s^-1")
	#	print(f"Slave ID is: {Slave_1} and the Baud rate is {Baud_1}")
	#	print(f"Solar radiation in zone B is: {Solar_Radiation_10} W.m^-2")
	#	print(f"Slave Id of pyranometer in zone B is: {slave_10} and Baud rate is {Baud_10}")
	#	print("Sensor Data in Zone C:")
	#	print("--------------------------------")
	#	print(f"Slave ID is: {Slave_2} and the Baud rate is {Baud_2}")
	#	print(f"Solar radiation in zone C is: {Solar_Radiation_15} W.m^-2")
	#	print(f"Slave Id of pyranometer in zone C is: {slave_15} and Baud rate is {Baud_15}")
	#	print("------------------------------------------")
