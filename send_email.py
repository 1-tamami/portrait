import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
RECIPIENT = os.getenv("RECIPIENT")
RECIPENT_NAME = os.getenv("RECIPENT_NAME")
PASSWORD = os.getenv("PASSWORD")


class SendEmail:

    def __init__(self, client_name, client_email, client_message):
        self.client_name = client_name
        self.client_email = client_email
        self.client_message = client_message
        pass

    def send_me_notification(self):
        subject = f"📩 {self.client_name} sent a message!"
        body = f'''
Hi {RECIPENT_NAME},

Congrats! You've got a message to your homepage!
---
Client Name: {self.client_name}
Client Email: {self.client_email}
Clinet Message: {self.client_message}

Be sure to reply to her/him!

---
your life supporter
        '''
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            msg = MIMEText(body.encode('utf-8'), _subtype='plain', _charset='utf-8')
            msg['Subject'] = Header(subject.encode('utf-8'), 'utf-8')
            msg['From'] = EMAIL
            msg['To'] = RECIPIENT
            connection.send_message(msg)
            print("Email sent successfully!")