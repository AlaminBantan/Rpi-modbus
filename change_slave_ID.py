import minimalmodbus # Don't forget to import the library!!
from time import sleep




PAR_sensy = minimalmodbus.Instrument('/dev/ttyUSB0', slave_address)	# Make an "instrument" object called PAR_sensy (port name, slave address (in decimal))

PAR_sensy.serial.baudrate = 19200 				# BaudRate
PAR_sensy.serial.bytesize = 8					# Number of data bits to be requested
PAR_sensy.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
PAR_sensy.serial.stopbits = 1					# Number of stop bits
PAR_sensy.serial.timeout  = 0.5					# Timeout time in seconds
PAR_sensy.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
PAR_sensy.clear_buffers_before_each_transaction = True
PAR_sensy.close_port_after_each_call = True

#write_register(registeraddress: int, value: Union[int, float], number_of_decimals: int = 0, functioncode: int = 16, signed: bool = False) → None
PAR_sensy.write_register(48,2, 0, 16, False)