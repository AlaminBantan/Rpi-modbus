import minimalmodbus
from time import sleep

id = 1
time_it = 10
c = 0
n_inst = minimalmodbus.Instrument('/dev/ttyACM1', id, debug=False)  # port name, slave address (in decimal)
n_inst.serial.baudrate = 19200

n_inst.write_register(52,0,0,16, False)