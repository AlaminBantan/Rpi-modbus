#Test
import minimalmodbus
from time import sleep

id = 15
time_it = 10
c = 0
n_inst = minimalmodbus.Instrument('/dev/ttyS0', id, debug=False)  # port name, slave address (in decimal)
n_inst.serial.baudrate = 9600
#n_inst.serial.parity = minimalmodbus.serial.PARITY_EVEN


while True:

    try:
        #output = n_inst.read_registers(4106, 1, 4) 

        #read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float

        output = n_inst.read_float(0, 3, 2, 0)
        #output = n_inst.read_register(1)
        print('float output is ',output)
        #print('integer output is ',output)
    except minimalmodbus.NoResponseError:
        print('No answer for single holding register')
        continue
    except minimalmodbus.InvalidResponseError:
        print('checksum error')
        continue
    
    sleep(2)