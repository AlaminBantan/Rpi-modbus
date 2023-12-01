import yagmail

# Set up your yagmail instance
email_address = 'bantanalamin@gmail.com'
password = 'muzomvmpwxiczzmo'
yag = yagmail.SMTP(email_address, password)

try:
    # Compose the email
    to = ['alamin.bantan@kaust.edu.sa']
    subject = 'Reading of the zones'
    body = 'These are the light data from zones b and c'

    # Attach the file
    attachment1 = "/home/cdacea/GH_data/modified_data_15min.csv"

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
