import yagmail

# Set up your yagmail instance
yag = yagmail.SMTP('bantanalamin@gmail.com', 'muzomvmpwxiczzmo')

# Compose the email
to = 'alamin.bantan@kaust.edu.sa'
subject = 'Reading of the zones'
body = 'These are the light data from zones b and c'

# Attach the file
attachment = "Light_comparison.csv"

# Send the email
yag.send(to, subject, [body, attachment])

# Logout
yag.close()
