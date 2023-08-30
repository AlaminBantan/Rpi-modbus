import minimalmodbus
from time import sleep, strftime
import csv
import os
import yagmail

mb_address = 1  # Modbus address of the sensor

sensy_boi = minimalmodbus.Instrument('/dev/ttyUSB0', mb_address)

sensy_boi.serial.baudrate = 19200
sensy_boi.serial.bytesize = 8
sensy_boi.serial.parity = minimalmodbus.serial.PARITY_EVEN
sensy_boi.serial.stopbits = 1
sensy_boi.serial.timeout = 0.5
sensy_boi.mode = minimalmodbus.MODE_RTU

sensy_boi.clear_buffers_before_each_transaction = True
sensy_boi.close_port_after_each_call = True

csv_header = ["Date", "Time", "Light Intensity (umol.m^-2.s^-1)"]

# Define your email settings
email_sender = 'bantanalamin@gmail.com'  # Replace with your sender email
email_password = 'muzomvmpwxiczzmo'  # Replace with your sender email password
email_receiver = 'alamin.bantan@kaust.edu.sa'  # Replace with the recipient email address

# Set up yagmail SMTP connection
yag = yagmail.SMTP(email_sender, email_password)

while True:
    current_date = strftime("%m-%d-%Y")
    current_time = strftime("%H:%M")

    if current_time == "00:30":
        previous_date = (strftime("%m-%d-%Y", (strftime("%s") - 24*60*60)))
        if os.path.exists(f"data_{previous_date}.csv"):
            # Send the CSV file as an email attachment
            email_subject = f"Sensor Data {previous_date}"
            email_contents = f"Hi Amin, attached is the sensor data CSV for {previous_date}"
            attachment_path = f"data_{previous_date}.csv"

            yag.send(
                to=email_receiver,
                subject=email_subject,
                contents=email_contents,
                attachments=attachment_path,
            )

            print("Email sent successfully")

    if current_time >= "23:59:59":
        break

    sleep(60)

sensy_boi.serial.close()
print("Ports Now Closed")
