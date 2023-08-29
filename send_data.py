import yagmail
import os
import re
from datetime import datetime, timedelta
import schedule
import time

# Email configuration
sender_email = "bantanalamin@gmail.com"
sender_password = "muzomvmpwxiczzmo"
receiver_email = "alamin.bantan@kaust.edu.sa"
subject = "CSVs from Raspberry Pi"

# Directory containing CSV files
csv_directory = "/home/cdacea/Sensors_modbus/PAR_data"

def send_csv():
    # Get the date of yesterday
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime("%m-%d-%Y")

    # Get a list of CSV files with date format in the filename
    csv_files = [filename for filename in os.listdir(csv_directory) if re.match(r"data_\d{2}-\d{2}-\d{4}\.csv", filename)]

    # Find the CSV file from yesterday
    csv_file_to_send = None
    for csv_filename in csv_files:
        if yesterday_str in csv_filename:
            csv_file_to_send = csv_filename
            break

    if csv_file_to_send:
        csv_file_path = os.path.join(csv_directory, csv_file_to_send)

        # Initialize yagmail
        yag = yagmail.SMTP(sender_email, app_password)

        # Create the email content
        contents = [
            "Here is the CSV file from Raspberry Pi for yesterday:",
            "See the attached file for details."
        ]

        # Attach the CSV file and send the email
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=contents,
            attachments=csv_file_path
        )

        # Close the connection
        yag.close()
    else:
        print("No CSV file found for yesterday.")

# Schedule the script to run every day at 6 am
schedule.every().day.at("06:00").do(send_csv)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
