import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from genshin_code_notifier.models import User
from dotenv import load_dotenv
import os

class Notifier:
    """
    A class used to send various email notifications.

    Methods
    ----------
    send_links(links)
        Sends an email for each code redemption link found to all subscribers.
    send_error(error_message)
        Sends an email containing an error message to me when the Hoyolab 
        website's HTML changes and causes the web scarper fail.
    send_welcome_text(phone_number, first_name, provider)
        Sends a welcome email to new subscribers.

    """
    def __init__(self):
        """
        Constructs all necessary attributes for the Notifier object.
        """

        load_dotenv()
        self.NOTIFIER_EMAIL = os.getenv("NOTIFIER_EMAIL")
        self.NOTIFIER_PASSWORD = os.getenv("NOTIFIER_PASSWORD")
        self.RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 465
        
    def _create_email(self, to, subject, body):
        """
        Builds a formatted email and returns it as a string.
        """

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.NOTIFIER_EMAIL
        message["To"] = to
        message.attach(MIMEText(body, "plain", "utf-8"))

        return message.as_string()

    def _send(self, messages):
        """
        Logs in once and sends a list of (recipient, email_string) pairs.
        A failure for one recipient is logged and doesn't stop the rest.
        """

        with smtplib.SMTP_SSL(
            self.SMTP_SERVER, self.SMTP_PORT,
            context=ssl.create_default_context()
        ) as email:
            email.login(self.NOTIFIER_EMAIL, self.NOTIFIER_PASSWORD)

            for recipient, message in messages:
                try:
                    email.sendmail(self.NOTIFIER_EMAIL, recipient, message)
                except Exception as e:
                    print(f"Failed to email {recipient}: {e}")

    def send_links(self, links):
        """
        Sends one email listing all new code redemption links to every
        subscriber.

        Parameters
        ----------
        links : list
            a list of the new code redemption links
        """

        body = ("Here are the new Genshin Impact codes:\n\n"
                + "\n".join(links))

        subscribers = (User.objects
                       .exclude(email__isnull=True)
                       .exclude(email=""))

        messages = [
            (user.email,
             self._create_email(user.email, "New Genshin codes!", body))
            for user in subscribers
        ]
        self._send(messages)

    def send_error(self, error_message):
        """
        Sends an email containing an error message to me when the Hoyolab
        website's HTML changes and causes the web scraper to fail.

        Parameters
        ----------
        error_message : str
            the error that caused the webscraper to fail
        """

        message = self._create_email(
            self.RECEIVER_EMAIL, "! Web Scraper Error !", str(error_message))
        self._send([(self.RECEIVER_EMAIL, message)])

    def send_welcome_email(self, email, first_name):
        """
        Sends a welcome email to new subscribers.

        Parameters
        ----------
        email : str
            the user's email address
        first_name : str
            the user's first name
        """

        body = (f"Welcome {first_name}!\n\n"
                "You will receive new codes as they are released.")

        message = self._create_email(
            email, "Welcome to Genshin Code Notifier!", body)
        self._send([(email, message)])