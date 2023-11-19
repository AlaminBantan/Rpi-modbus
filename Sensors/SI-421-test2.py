import serial
import time
import io
import logging

logging.basicConfig(level=logging.INFO)

def configure_sensor(port, sensor_id):
    sensor = serial.Serial(port,
                           baudrate=9600,
                           bytesize=serial.EIGHTBITS,
                           parity=serial.PARITY_NONE,
                           stopbits=serial.STOPBITS_ONE,
                           xonxoff=False,
                           timeout=1)
    sensor = io.TextIOWrapper(io.BufferedRWPair(sensor, sensor))

    logging.info(f"Configured sensor {sensor_id} on port {port}")
    return sensor

def communicate_with_sensor(sensor, sensor_id):
    command = f"{sensor_id}M!\r"
    sensor.write(command)
    logging.info(f"Take measurement {sensor_id}")
    sensor.flush()
    time.sleep(1)

    data_str = f"{sensor_id}D0!\r"
    sensor.write(data_str)
    sensor.flush()
    logging.info(f"Read measurement {sensor_id}")

    data = sensor.readlines()
    sensor.flush()
    time.sleep(1)

    logging.info(f"Data at sensor {sensor_id} is {data}")
    time.sleep(2)

# Configure sensors
IR_0 = configure_sensor("/dev/ttyACM0", 0)
IR_1 = configure_sensor("/dev/ttyACM1", 1)
IR_2 = configure_sensor("/dev/ttyACM2", 2)
IR_3 = configure_sensor("/dev/ttyACM3", 3)
IR_4 = configure_sensor("/dev/ttyACM4", 4)
IR_5 = configure_sensor("/dev/ttyACM5", 5)

try:
    while True:
        communicate_with_sensor(IR_0, 0)
        communicate_with_sensor(IR_1, 1)
        communicate_with_sensor(IR_2, 2)
        communicate_with_sensor(IR_3, 3)
        communicate_with_sensor(IR_4, 4)
        communicate_with_sensor(IR_5, 5)

except KeyboardInterrupt:
    # Clean up when interrupted
    logging.info("Ports Closed")
    IR_0.close()
    IR_1.close()
    IR_2.close()
    IR_3.close()
    IR_4.close()
    IR_5.close()
