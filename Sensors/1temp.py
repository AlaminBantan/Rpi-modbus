import serial
import io
import threading
from time import sleep
from datetime import datetime

port = "/dev/ttyACM0"
def read_sensor(port, 33):
    serial_sensor = serial.Serial(port,
                                  baudrate=4800,
                                  bytesize=serial.SEVENBITS,
                                  parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_ONE,
                                  xonxoff=False,
                                  timeout=5)
    hum_sensor = io.TextIOWrapper(io.BufferedRWPair(serial_sensor, serial_sensor))

    try:
        hum_sensor.write(f"open 33\r\n")  # Open a connection to the sensor
        hum_sensor.flush()
        print(f"Sensor 33: opened connection")
        sleep(2)  # Allow time for the sensor to initialize

        while True:
            hum_sensor.write("SEND\r\n")  # Request a reading
            hum_sensor.flush()
            data = hum_sensor.readline().strip()
            
            # Get the current timestamp
            timestamp = datetime.now().strftime("%I:%M:%S %p")
            
            print(f"Sensor 33: data is {data} at {timestamp}")

            # Optional: Stop continuous output if needed
            # hum_sensor.write("S\r\n")
            # hum_sensor.flush()

            sleep(5)  # Adjust as needed based on your interval requirements

    except KeyboardInterrupt:
        # Clean up when interrupted
        print(f"Sensor 33 Port Closed")
    finally:
        # Close the serial port to ensure clean termination
        serial_sensor.close()