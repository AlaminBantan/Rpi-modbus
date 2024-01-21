import minimalmodbus
from time import sleep

def configure_instrument(port, address):
    instrument = minimalmodbus.Instrument(port, address)
    instrument.serial.timeout = 0.5
    instrument.mode = minimalmodbus.MODE_RTU
    instrument.clear_buffers_before_each_transaction = True
    instrument.close_port_after_each_call = True
    return instrument

def read_sensor_data(instrument):
    try:
        temp = instrument.read_register(0, 0, 3, False)
        water_content = instrument.read_register(1, 0, 3, False)
        ec = instrument.read_register(3, 0, 3, False)
        salinity = instrument.read_register(4, 0, 3, False)
        tds = instrument.read_register(5, 0, 3, False)

        return temp, water_content, ec, salinity, tds
    except Exception as e:
        print(f"Error reading sensor data: {e}")
        return None

if __name__ == "__main__":
    instrument_1 = configure_instrument('/dev/ttyACM0', 1)

    try:
        while True:
            sensor_data = read_sensor_data(instrument_1)
            if sensor_data is not None:
                temp, water_content, ec, salinity, tds = sensor_data
                print(f"Temp: {temp}, Water Content: {water_content}, EC: {ec}, Salinity: {salinity}, TDS: {tds}")
            sleep(1)  # Add a sleep time to avoid high CPU usage

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Closing port.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        instrument_1.serial.close()
        print("Port now closed.")
