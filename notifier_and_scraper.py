from WebScraper import *
from Notifier import *
from Spreadsheet import *

web_scraper = WebScraper()
links = web_scraper.find_links()

# Run this code only if the web scraper was successful
if links:
    spreadsheet = Spreadsheet()
    saved_codes = spreadsheet.read_code_spreadsheet()
    
    last_code = len(saved_codes) - 1

    # if the last link scraped is not the last link in the spreadsheet, add the links to the spread sheet and send a text
    if links[-1] != saved_codes[last_code][0]:
        notifier = Notifier()
        notifier.send_links(links)
        for link in links:
            spreadsheet.write_to_code_spreadsheet(link)