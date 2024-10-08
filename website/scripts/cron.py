from .webscraper import *
from .notifier import *
from datetime import timedelta
from django.utils import timezone
from genshin_code_notifier.models import Code

def run():
    """
    Run the daily task of scraping for new links, notifying subscribers if found, 
    and deleting old links from the database.
    """
    web_scraper = WebScraper()
    links = web_scraper.find_links()

    # Continue only if the web scraper was successful.
    if links:
        try:
            # Is the code link already in the database?
            Code.objects.get(link=links[0])

        except Code.DoesNotExist:
            notifier = Notifier()
            notifier.send_links(links)

            for link in links:
                new_code = Code(link = link)
                new_code.save()

    # Delete any link older than 60 days.
    thirty_days_ago = timezone.now() - timedelta(days=60)
    Code.objects.filter(date__lte=thirty_days_ago).delete()
