import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "bantanalamin@gmail.com"
sender_password = "Ab!78803812"
receiver_email = "alamin.bantan@kaust.edu.sa"
subject = "PAR data from Raspberry Pi"

# Read your data
with open("*.csv", "r") as data_file:
    data = data_file.read()

# Create the email content
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(data, "plain"))

# Connect to the SMTP server and send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
