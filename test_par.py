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

# Good practice to clean up before and after each execution
PAR_1.clear_buffers_before_each_transaction = True
PAR_1.close_port_after_each_call = True

PAR_2.clear_buffers_before_each_transaction = True
PAR_2.close_port_after_each_call = True


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