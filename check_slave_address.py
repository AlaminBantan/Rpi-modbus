import minimalmodbus
import serial

# Define the range of Modbus addresses to scan
start_address = 1  # Starting address
end_address = 247  # Ending address (the maximum valid Modbus address)

# Specify the serial port where the sensor is connected
serial_port = '/dev/ttyUSB0'  # Replace with your serial port

# Function to check if a slave address is valid
def is_valid_slave_address(address, port):
    try:
        instrument = minimalmodbus.Instrument(port, address)
        instrument.read_register(0, 3, 2, 0)  # Try to read a register
        return True
    except (ValueError, IOError, minimalmodbus.ModbusException, serial.SerialException):
        return False

# Scan the range of Modbus addresses
print("Scanning Modbus addresses...")
found_addresses = []
for address in range(start_address, end_address + 1):
    if is_valid_slave_address(address, serial_port):
        found_addresses.append(address)

# Display the results
if found_addresses:
    print("Found valid slave addresses:", found_addresses)
else:
    print("No valid slave addresses found in the specified range.")

