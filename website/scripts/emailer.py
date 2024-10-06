import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

class Emailer:
    """
    A class used to send a message obtained via the Contact Me form to 
    my email address.

    """
    def __init__(self, name, contact, subject, body):
        """
        Constructs all necessary attributes for the Emailer object.

        Parameters
        ----------
        name : str
            the user's name
        contact : str
            the user's email address
        subject : str
            the subject of the message
        body : str
            the body of the message
        """
        self.name = name
        self.contact = contact
        self.subject = subject
        self.body = body

        load_dotenv()
        self.SENDER_EMAIL = os.getenv("SENDER_EMAIL")
        self.SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
        self.RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

    def _create_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.SENDER_EMAIL
        message["To"] = self.RECEIVER_EMAIL

        text = (f"From: Meal Planner \n"
                f"Name: {self.name} \n"
                f"Contact: {self.contact}\n"
                f"{self.body}")
        
        email = MIMEText(text, "plain")
        message.attach(email)

        return message.as_string()

    def send_email(self):
        """
        Sends an email with information obtained via the contact me form 
        to my email address.
        """
                
        email_message = self._create_email()
        
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=ssl.create_default_context()
        ) as email:
            email.login(
                self.SENDER_EMAIL, 
                self.SENDER_PASSWORD)
            email.sendmail(self.SENDER_EMAIL, self.RECEIVER_EMAIL, email_message)