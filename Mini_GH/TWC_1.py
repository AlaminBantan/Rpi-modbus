import minimalmodbus
from time import sleep

TWC_1 = minimalmodbus.Instrument('/dev/ttyACM0', 0)
TWC_1.serial.baudrate = 9600  
TWC_1.serial.bytesize = 8 
TWC_1.serial.parity = minimalmodbus.serial.PARITY_NONE  
TWC_1.serial.stopbits = 1  
TWC_1.mode = minimalmodbus.MODE_RTU
TWC_1.clear_buffers_before_each_transaction = True
TWC_1.close_port_after_each_call = True


TWC_1.write_register(512,1, 0, 16, False)


