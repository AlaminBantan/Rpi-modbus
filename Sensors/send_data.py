import yagmail

# Set up your yagmail instance
yag = yagmail.SMTP('bantanalamin@gmail.com', 'muzomvmpwxiczzmo')

# Compose the email
to = 'alamin.bantan@kaust.edu.sa'
subject = 'Reading of the zones'
body = 'These are the light data from zones b and c'

# Attach the file
attachment1 = "Light_comparison.csv"
attachment2 = "Light_comparison11.csv"

# Send the email
yag.send(to, subject, [body, attachment1, attachment2])

# Logout
yag.close()
