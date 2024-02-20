import minimalmodbus
from time import sleep

TWC_1 = minimalmodbus.Instrument('/dev/ttyACM0', 5)
TWC_1.serial.baudrate = 9600  
TWC_1.serial.bytesize = 8 
TWC_1.serial.parity = minimalmodbus.serial.PARITY_NONE  
TWC_1.serial.stopbits = 1  
TWC_1.mode = minimalmodbus.MODE_RTU
TWC_1.clear_buffers_before_each_transaction = True
TWC_1.close_port_after_each_call = True

#Change the slave address to 2
#new_slave_address = 4
#TWC_1.write_register(512, new_slave_address, functioncode=6, number_of_decimals=0, signed=False)


try:
   while True:
    temp_1=TWC_1.read_register(0, number_of_decimals=0, functioncode= 3 ,signed=False)
    print(f"Temp is {temp_1}")
    sleep(1)

except KeyboardInterrupt:
   TWC_1.serial.close()
   print("TWC_1 closed")

# Read the temperature register
#temperature_raw = TWC_1.read_register(0, functioncode=3, number_of_decimals=0, signed=True)
#temperature_celsius = temperature_raw / 100.0  # Convert to Celsius

#print("Temperature:", temperature_celsius, "°C")
