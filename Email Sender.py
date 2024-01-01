from email.message import EmailMessage

#password_storage is a separate file that contains a variable with email password
from password_storage import password
import ssl 
import smtplib

email_sender = 'gabriel.briones@student.ie.edu'
#using the imported password variable
email_password = password

#Temporary disposable email
email_receiver = 'hegef82470@visignal.com'

subject = "Happy New Year!"
body = """
Best wishes for you and your loved ones for 2024!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_sender)
    smtp.sendmail(email_sender, email_receiver, em.as_string())