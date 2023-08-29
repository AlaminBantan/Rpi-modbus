import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv

# Email configuration
sender_email = "bantanalamin@gmail.com"
sender_password = "Ab!78803812"
receiver_email = "alamin.bantan@kaust.edu.sa"
subject = "CSV from Raspberry Pi"

# Read CSV data
csv_file_path = "/home/cdacea/Sensors_modbus/PAR_data/data_08-29-2023.csv"
with open(csv_file_path, "r") as csv_file:
    csv_data = csv_file.read()

# Create the email content
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the CSV file
attachment = MIMEBase("application", "octet-stream")
attachment.set_payload(csv_data.encode())
encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", f"attachment; filename=data.csv")
msg.attach(attachment)

# Connect to the SMTP server and send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
