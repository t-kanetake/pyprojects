# project: email sender
# created: 12/10/2023

# imports libraries necessary for function
from email.message import EmailMessage
import ssl
import smtplib


# paste e-mail address here
email_sender = "example@gmail.com"
# uses an app password to access the e-mail account
email_password = ""
email_receiver = "username@example.com"

# subject and body/contents of the email
subject = "SAW"
body = """
do you want to play a game?"""

# creates an instance of the email that conforms to the EmailMessage class
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

# creates a secure connection to the server
context = ssl.create_default_context()

# connects to the server and sends the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())
