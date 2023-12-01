import yagmail

# Set up your yagmail instance
email_address = 'bantanalamin@gmail.com'
password = 'muzomvmpwxiczzmo'
yag = yagmail.SMTP(email_address, password)

try:
    # Compose the email
    to = ['alamin.bantan@kaust.edu.sa', 'rebekah.waller@kaust.edu.sa']
    subject = 'Climatic of the zones'
    body = 'These are the climatic data from zones b and c'

    # Attach the file
    attachment1 = "/home/cdacea/GH_data/modified_data_15min.csv"
    attachment2 ="/home/cdacea/Rpi-modbus/par_plot.svg"
    attachment3 ="/home/cdacea/Rpi-modbus/solar_radiation_plot.svg"
    attachment4 ="/home/cdacea/Rpi-modbus/temperature_plot.svg"
    attachment5 ="/home/cdacea/Rpi-modbus/humidity_plot.svg"
    attachment6 ="/home/cdacea/Rpi-modbus/co2_concentration_plot.svg"



    # Send the email
    yag.send(to, subject, [body, attachment1, attachment2, attachment3, attachment4, attachment5, attachment6])

    # Log success or other relevant information
    print("Email sent successfully!")

except Exception as e:
    # Log the error
    print(f"Error: {e}")

finally:
    # Logout
    yag.close()
