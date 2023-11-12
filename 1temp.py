import serial
import io
from time import sleep

def initialize_sensor(port, sensor_number):
    serial_sensor = serial.Serial(port,
                                  baudrate=4800,
                                  bytesize=serial.SEVENBITS,
                                  parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_ONE,
                                  xonxoff=False,
                                  timeout=2)

    hum_sensor = io.TextIOWrapper(io.BufferedRWPair(serial_sensor, serial_sensor))

    try:
        while True:
            hum_sensor.write(f"open {sensor_number}")
            print("open")
            hum_sensor.flush()
            sleep(1)
            hum_sensor.write("send")
            print("send")
            hum_sensor.flush()
            sleep(1)
            data = hum_sensor.readline()
            print(f"data is: {data}")
            hum_sensor.flush()
            sleep(1)
            hum_sensor.write("close")
            print("close")
            sleep(2)

    except KeyboardInterrupt:
        # Clean up when interrupted
        print(f"Sensor {sensor_number} Port Closed")


# Example usage for sensors 34, 33, 32, 31
initialize_sensor("/dev/ttyACM0", 34)
initialize_sensor("/dev/ttyACM0", 33)
initialize_sensor("/dev/ttyACM0", 32)
initialize_sensor("/dev/ttyACM0", 31)
