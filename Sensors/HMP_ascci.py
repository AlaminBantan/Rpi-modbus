import minimalmodbus 
from time import sleep


Thum_240 = minimalmodbus.Instrument('/dev/ttyACM0', 240, debug=True)
Thum_240.serial.baudrate = 4800
Thum_240.serial.parity = minimalmodbus.serial.PARITY_EVEN
Thum_240.serial.bytesize = 7
Thum_240.serial.stopbits = 1
Thum_240.mode = minimalmodbus.MODE_ASCII		

SMODE RUN
		


