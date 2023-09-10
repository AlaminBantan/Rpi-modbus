import minimalmodbus
from time import sleep

def configure_sensor(mb_address):
    sensor = minimalmodbus.Instrument('/dev/ttyUSB0', mb_address)

    sensor.clear_buffers_before_each_transaction = True
    sensor.close_port_after_each_call = True
    return sensor

def read_sensor_data(sensor, register_address):
    intensity = sensor.read_float(0, 3, 2, 0)
    slave = sensor.read_float(16, 3, 2, 0)
    return intensity, slave

try:
    PAR_1 = configure_sensor(1)
    PAR_2 = configure_sensor(2)
    Solar_10 = configure_sensor(10)
    Solar_15 = configure_sensor(15)

    while True:
        PAR_intensity_1, Slave_1 = read_sensor_data(PAR_1, 0)
        PAR_intensity_2, Slave_2 = read_sensor_data(PAR_2, 0)
        Solar_Radiation_10, Slave_10 = read_sensor_data(Solar_10, 0)
        Solar_Radiation_15, Slave_15 = read_sensor_data(Solar_15, 0)

        print("\n"*50)
        print("Sensor Data--------------------------------")
        print(f"PAR Intensity 1: {PAR_intensity_1} umol.m^-2.s^-1")
        print(f"Slave ID 1: {Slave_1}")
        print(f"PAR Intensity 2: {PAR_intensity_2} umol.m^-2.s^-1")
        print(f"Slave ID 2: {Slave_2}")
        print(f"Solar Radiation 10: {Solar_Radiation_10} W.m^-2")
        print(f"Slave ID 10: {Slave_10}")
        print(f"Solar Radiation 15: {Solar_Radiation_15} W.m^-2")
        print(f"Slave ID 15: {Slave_15}")
        print("------------------------------------------")

        print("")
        print("")
        print("")
        sleep(1)

except KeyboardInterrupt:

    # Piece of mind close out
    PAR_1.serial.close()
    PAR_2.serial.close()
    Solar_10.serial.close()
    Solar_15.serial.close()
    print("Ports Now Closed")
