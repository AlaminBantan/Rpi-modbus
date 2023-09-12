import minimalmodbus 
from time import sleep


#configuration of first pyranometer
Solar_10 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)	
Solar_10.serial.baudrate = 19200
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
Solar_10.clear_buffers_before_each_transaction = True
Solar_10.close_port_after_each_call = True

Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True


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
