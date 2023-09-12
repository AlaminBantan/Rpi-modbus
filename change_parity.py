import minimalmodbus # Don't forget to import the library!!
from time import sleep


mb_address = 15 # Modbus address of sensor

Solar_15 = minimalmodbus.Instrument('/dev/ttyUSB0', mb_address, debug=False)	# Make an "instrument" object called Solar_15 (port name, slave address (in decimal))

Solar_15.serial.baudrate = 19200 		


# Good practice to clean up before and after each execution
Solar_15.clear_buffers_before_each_transaction = True
Solar_15.close_port_after_each_call = True


Solar_15.write_register(52,2, 0, 16, False)