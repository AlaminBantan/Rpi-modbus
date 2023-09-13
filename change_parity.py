import minimalmodbus # Don't forget to import the library!!
from time import sleep




Solar_10 = minimalmodbus.Instrument('/dev/ttyUSB0', 10, debug=False)	# Make an "instrument" object called Solar_10 (port name, slave address (in decimal))
Solar_10.serial.baudrate = 19200 
Solar_10.serial.bytesize = 8					# Number of data bits to be requested
Solar_10.serial.stopbits = 1					# Number of stop bits
Solar_10.serial.timeout  = 0.5					# Timeout time in seconds
Solar_10.mode = minimalmodbus.MODE_RTU			



# Good practice to clean up before and after each execution
Solar_10.clear_buffers_before_each_transaction = True
Solar_10.close_port_after_each_call = True


Solar_10.write_register(52,2,0,16, False)