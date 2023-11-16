from WebScraper import *
from Notifier import *
from Spreadsheet import *

web_scraper = WebScraper()
links = web_scraper.find_links()

spreadsheet = Spreadsheet()
saved_codes = spreadsheet.read_code_spreadsheet()
 
last_code = len(saved_codes) - 1
if links[0] != saved_codes[last_code]:
    for link in links:
        spreadsheet.write_to_code_spreadsheet([link, "not sent"])
