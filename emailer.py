import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Emailer:
    def __init__(self, name, contact, subject, body):
        self.name = name
        self.contact = contact
        self.subject = subject
        self.body = body

        self.SENDER_EMAIL = open("secrets.txt", "r").readlines()[0]
        self.RECEIVER_EMAIL = "baileystarrc4@gmail.com"

    def create_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.SENDER_EMAIL
        message["To"] = self.RECEIVER_EMAIL

        text = f"""\
            {self.body} \n
            Name: {self.name} \n
            Contact: {self.contact}"""
        
        email = MIMEText(text, "plain")
        message.attach(email)

        return message.as_string()

    def send_email(self):
        email_message = self.create_email()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=ssl.create_default_context()
        ) as email:
            email.login(self.SENDER_EMAIL, open("secrets.txt", "r").readlines()[1])
            email.sendmail(self.SENDER_EMAIL, self.RECEIVER_EMAIL, email_message)