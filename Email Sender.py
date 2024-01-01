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

#Subject and body of email
subject = "Happy New Year!"
body = """
Best wishes for you and your loved ones for 2024!
"""

#Create instance of email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

#Use smptlib to login and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
