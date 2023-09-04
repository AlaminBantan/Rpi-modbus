import minimalmodbus # Don't forget to import the library!!



mb_address = 1 # Modbus address of sensor

Solar_sensy = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called Solar_sensy (port name, slave address (in decimal))

Solar_sensy.serial.baudrate = 19200 				# BaudRate
Solar_sensy.serial.bytesize = 8					# Number of data bits to be requested
Solar_sensy.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
Solar_sensy.serial.stopbits = 1					# Number of stop bits
Solar_sensy.serial.timeout  = 0.5					# Timeout time in seconds
Solar_sensy.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

# Good practice to clean up before and after each execution
Solar_sensy.clear_buffers_before_each_transaction = True
Solar_sensy.close_port_after_each_call = True


Solar_sensy.write_float(16,3,2,0)

new = Solar_sensy.read_float(16,3,2,0)

print(f"the new slave address is: {new}")