import minimalmodbus

# Create an instrument instance
TWC_1 = minimalmodbus.Instrument('/dev/ttyACM0', 1)

# Configure serial communication parameters
TWC_1.serial.baudrate = 9600
TWC_1.serial.bytesize = 8
TWC_1.serial.parity = minimalmodbus.serial.PARITY_NONE
TWC_1.serial.stopbits = 1
TWC_1.mode = minimalmodbus.MODE_RTU
TWC_1.clear_buffers_before_each_transaction = True
TWC_1.close_port_after_each_call = True

# Define function codes for reading registers
READ_HOLDING_REGISTER = 3
READ_INPUT_REGISTER = 4

# Define the register addresses
TEMPERATURE_ADDRESS = 0x0000
VWC_ADDRESS = 0x0001
EC_ADDRESS = 0x0002
SALINITY_ADDRESS = 0x0003
TDS_ADDRESS = 0x0004

# Function to read a register given its address and function code
def read_register(address, function_code):
    try:
        if function_code == READ_HOLDING_REGISTER:
            value = TWC_1.read_register(address, function_code=function_code, signed=True)
        elif function_code == READ_INPUT_REGISTER:
            value = TWC_1.read_register(address, function_code=function_code)
        else:
            raise ValueError("Invalid function code")
        
        return value
    except Exception as e:
        print(f"Error reading register at address {address}: {e}")
        return None

# Read the registers
temperature = read_register(TEMPERATURE_ADDRESS, READ_HOLDING_REGISTER)
vwc = read_register(VWC_ADDRESS, READ_HOLDING_REGISTER)
ec = read_register(EC_ADDRESS, READ_HOLDING_REGISTER)
salinity = read_register(SALINITY_ADDRESS, READ_HOLDING_REGISTER)
tds = read_register(TDS_ADDRESS, READ_HOLDING_REGISTER)

# Print the values
if temperature is not None:
    print(f"Temperature: {temperature / 100:.2f} ℃")
if vwc is not None:
    print(f"Volumetric Water Content: {vwc / 100:.2f}%")
if ec is not None:
    print(f"Electrical Conductivity: {ec} us/cm")
if salinity is not None:
    print(f"Salinity: {salinity} mg/L")
if tds is not None:
    print(f"TDS: {tds} mg/L")
