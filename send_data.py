import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import re

# Email configuration
sender_email = "bantanalamin@gmail.com"
sender_password = "Ab!78803812"
receiver_email = "alamin.bantan@kaust.edu.sa"
subject = "CSVs from Raspberry Pi"

# Directory containing CSV files
csv_directory = "/home/cdacea/Sensors_modbus/PAR_data/"

# Get a list of CSV files with date format in the filename
csv_files = [filename for filename in os.listdir(csv_directory) if re.match(r"data_\d{2}-\d{2}-\d{4}\.csv", filename)]

# Create the email content
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach each CSV file
for csv_filename in csv_files:
    csv_file_path = os.path.join(csv_directory, csv_filename)
    with open(csv_file_path, "r") as csv_file:
        csv_data = csv_file.read()

    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(csv_data.encode())
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", f"attachment; filename={csv_filename}")
    msg.attach(attachment)

# Connect to the SMTP server and send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
