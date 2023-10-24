from WebScraper import *
from Notifier import *

web_scraper = WebScraper()

link = web_scraper.find_code_and_link()

notifier = Notifier()
notifier.send_email(link)