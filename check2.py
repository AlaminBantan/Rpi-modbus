import minimalmodbus

# Specify the serial port and Modbus communication parameters
port = '/dev/ttyUSB0'
baudrate = 19200
bytesize = 8
parity = minimalmodbus.serial.PARITY_NONE
stopbits = 1
timeout = 1  # Adjust the timeout as needed

# Known Modbus register to read (you may need to adjust this)
register_address = 0

# Try different slave addresses
for slave_address in range(1, 255):
    try:
        instrument = minimalmodbus.Instrument(port, slave_address)
        instrument.serial.baudrate = baudrate
        instrument.serial.bytesize = bytesize
        instrument.serial.parity = parity
        instrument.serial.stopbits = stopbits
        instrument.serial.timeout = timeout

        # Try reading a known register from the sensor
        value = instrument.read_register(0, 3, 2, 0)

        print(f"Slave address {slave_address} responded with data: {value}")

        # If you receive data without errors, this may be the correct address
        # You can add further logic to verify that the response is as expected
        # and decide whether this address is the correct one for your sensor.
        
    except (ValueError, IOError, minimalmodbus.ModbusException, serial.SerialException):
        # If there was an error (e.g., no response or communication error),
        # continue to the next address.
        pass