import yagmail
import os
import re

# Email configuration
sender_email = "bantanalamin@gmail.com"
sender_password = "muzomvmpwxiczzmo"
receiver_email = "alamin.bantan@kaust.edu.sa"
subject = "CSVs from Raspberry Pi"

# Directory containing CSV files
csv_directory = "/home/cdacea/Sensors_modbus/PAR_data"

# Get a list of CSV files with date format in the filename
csv_files = [filename for filename in os.listdir(csv_directory) if re.match(r"data_\d{2}-\d{2}-\d{4}\.csv", filename)]

# Initialize yagmail
yag = yagmail.SMTP(sender_email, sender_password)

# Create the email content
contents = [
    "Here are the CSV files from Raspberry Pi:",
    "See attached files for details."
]

# Attach each CSV file
for csv_filename in csv_files:
    csv_file_path = os.path.join(csv_directory, csv_filename)
    yag.send(
        to=receiver_email,
        subject=subject,
        contents=contents,
        attachments=csv_file_path
    )

# Close the connection
yag.close()
