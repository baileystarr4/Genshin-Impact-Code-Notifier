import smtplib, ssl
from .providers import PROVIDERS
import os
from website.website.wsgi import *
from genshin_code_notifier.models import User
from dotenv import load_dotenv

class Notifier:
    """
    A class used to send various text notifications.

    Methods
    ----------
    send_links(links)
        Sends a text for each code redemption link found to all subscribers.
    send_error(error_message)
        Sends a text containing an error message to me when the Hoyolab 
        website's HTML changes and causes the web scarper fail.
    send_welcome_text(phone_number, first_name, provider)
        Sends a welcome text to new subscribers.

    """
    def __init__(self):
        """
        Constructs all necessary attributes for the Notifier object.
        """

        load_dotenv()
        self.SENDER_EMAIL = os.getenv("SENDER_EMAIL")
        self.SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 465
        
    def send_links(self, links):
        """
        Sends a text for each code redemption link found to all subscribers.

        Parameters
        ----------
        links : list
            a list of the new code redemption links
        """

        for user in User.objects.all():
            number = user.phone_number
            provider = user.carrier
            receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

            for link in links:
                email_message = (f"To:{receiver_email}\n"
                                 f"Here's the new Genshin code!\n{link}")
                
                with smtplib.SMTP_SSL(
                    self.SMTP_SERVER, self.SMTP_PORT, 
                    context=ssl.create_default_context()
                ) as email:
                    email.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
                    email.sendmail(
                        self.SENDER_EMAIL, receiver_email, email_message)

    def send_error(self, error_message):
        """
        Sends a text containing an error message to me when the Hoyolab 
        website's HTML changes and causes the web scarper fail.

        Parameters
        ----------
        error_message : str
            the error that caused the webscraper to fail
        """

        me = User.objects.get(first_name="Admin")

        receiver_email = f'{me.phone_number}@{PROVIDERS.get(me.carrier).get("sms")}'
        
        email_message = (f"To:{receiver_email}\n! Web Scraper Error !\n"
                            f"{error_message}")
        
        with smtplib.SMTP_SSL(
            self.SMTP_SERVER, self.SMTP_PORT, context=ssl.create_default_context()
        ) as email:
            email.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
            email.sendmail(self.SENDER_EMAIL, receiver_email, email_message)


    # Sends a success / welcome text to the new subscriber
    def send_welcome_text(self, phone_number, first_name, provider):
        """
        Sends a welcome text to new subscribers.

        Parameters
        ----------
        phone_number : str
            the user's phone number
        first_name : str
            the user's first name
        provider : str
            the user's phone provider
        """    

        receiver_email = f'{phone_number}@{PROVIDERS.get(provider).get("sms")}'

        email_message = (f"To:{receiver_email}\n\nWelcome {first_name}!\n"
                          "You will receive new codes as they are released.")
        
        with smtplib.SMTP_SSL(
            self.SMTP_SERVER, self.SMTP_PORT, context=ssl.create_default_context()
        ) as email:
            email.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
            email.sendmail(self.SENDER_EMAIL, receiver_email, email_message)