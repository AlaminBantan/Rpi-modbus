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

# Email configuration
sender_email = "bantanalamin@gmail.com"
sender_password = "muzomvmpwxiczzmo"
receiver_email = "alamin.bantan@kaust.edu.sa"
subject = "CSVs from Raspberry Pi"


# Set up yagmail SMTP connection
yag = yagmail.SMTP(email_sender, email_password)

while True:
    current_date = strftime("%m-%d-%Y")
    current_time = strftime("%H:%M")

    if not os.path.exists(f"data_{current_date}.csv"):
        with open(f"data_{current_date}.csv", mode="w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(csv_header)
            
    lightintensity = sensy_boi.read_float(0, 3, 2, 0)

    with open(f"data_{current_date}.csv", mode="a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([current_date, current_time, lightintensity])
        
        # Send the CSV file as an email attachment
        email_subject = f"PAR sensor Data {current_date}"
        email_contents = f"Hello Amin, check the attached sensor data CSV for {current_date}"
        attachment_path = f"data_{current_date}.csv"
        
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
