import pandas as pd
import yagmail
from datetime import datetime

# Read the CSV file
df = pd.read_csv("/home/cdacea/south_GH/south_climate.csv")

# Convert 'datetime' column to datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# Set 'datetime' column as the index
df.set_index('datetime', inplace=True)

# Group by datetime for each minute and average every 15 minutes
result = df.resample('15min').mean()

# Save the result to CSV
modified_file_path = "/home/cdacea/south_GH/south_modified.csv"
result.to_csv(modified_file_path)

# Set up your yagmail instance
email_address = 'bantanalamin@gmail.com'
password = 'muzomvmpwxiczzmo'
yag = yagmail.SMTP(email_address, password)

try:
    # Compose the email
    to = ['alamin.bantan@kaust.edu.sa']
    
    # Generate today's date
    today_date = datetime.now().strftime('%Y-%m-%d')
    
    # Update the subject with today's date
    subject = f'Climatic of the south_GH: {today_date}'
    
    body = f'These are the climatic data from south_GH {today_date}'

    # Attach the modified file
    attachment1 = modified_file_path

    # Send the email
    yag.send(to, subject, [body, attachment1])

    # Log success or other relevant information
    print("Email sent successfully!")

except Exception as e:
    # Log the error
    print(f"Error: {e}")

finally:
    # Logout
    yag.close()
