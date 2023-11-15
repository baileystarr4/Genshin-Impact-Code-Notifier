from WebScraper import *
# from Notifier import *

web_scraper = WebScraper()

link = web_scraper.find_code_and_link()

# notifier = Notifier()
# notifier.send_sms_via_email(link=link, number="NUMBER", provider="AT&T")