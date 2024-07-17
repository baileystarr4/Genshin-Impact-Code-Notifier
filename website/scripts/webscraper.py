from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .notifier import *

class WebScraper:
    """
    A class used to scrape one of Brutefact's Hoyolab collection pages for new 
    Genshin code redemption links.

    """
    def __init__(self):
        """
        Constructs all necessary attributes for the WebScraper object.
        """
        self.service = Service(executable_path=r'/opt/chromedriver')
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument('--disable-extensions')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--no-cache')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--window-size=1024x768')
        self.chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        self.chrome_options.add_argument('--hide-scrollbars')
        self.chrome_options.add_argument('--enable-logging')
        self.chrome_options.add_argument('--log-level=0')
        self.chrome_options.add_argument('--v=99')
        self.chrome_options.add_argument('--data-path=/tmp/data-path')
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument('--homedir=/tmp')
        self.chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        self.chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        self.chrome_options.headless = True
        self.selenium_options = {
            'request_storage_base_dir': '/tmp', # Use /tmp to store captured data
            'exclude_hosts': ''
        }
        self.chrome_options.binary_location = '/opt/headless-chromium'
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options, seleniumwire_options=self.selenium_options)
        
        self.error_notifier = Notifier()
        
        self.links = []

    def find_links(self):
        """
        Scrapes Brutefact's Redeem Codes and Web Events collection page on the 
        Hoyolab website for new Genshin code redemption links.

        Returns
        ----------
        links : list 
            A list containing the new code links if successful.
        or 
        None
            None if there was an error.
        """

        # Open the collection page on Hoyolab's website
        self.driver.get("https://www.hoyolab.com/creatorCollection/535336")

        # Leaving as comment for when they change the website again. 
        # Currently there is no log in pop-up

        # # Look for the iframe where the login popup is located
        # try:
            # iframe = WebDriverWait(self.driver, 60).until(
            #     EC.presence_of_element_located((
            #         By.ID, 'hyv-account-sdk-frame'))
            # )
            # self.driver.switch_to.frame(iframe)
        # except:
        #     error_message = "Frame not found"
        #     # self.error_notifier.send_error(error_message)
        #     self.driver.quit()
        #     return

        # Look for the close button on the login pop-up and click when found.
        # try:
        #     close_button = WebDriverWait(self.driver, 60).until(
        #         EC.element_to_be_clickable((
        #             By.XPATH, '/html/body/div[2]/div/div/button'))    
        #     )
        #     close_button.click()
        # except:
        #     error_message = "Close button not found."
        #     # self.error_notifier.send_error(error_message)
        #     self.driver.quit()
        #     return
        
        # Look for skip button on pop-up and click when found.
        try:
            self.driver.switch_to.default_content()
            skip_button = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((
                    By.XPATH, 
                    '/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/button'))    
            )
            skip_button.click()
        except:
            error_message = "Skip button not clicked."
            self.error_notifier.send_error(error_message)
            self.driver.quit()
            return
        # Look for newest article mentioning a code and click when found.    
        try:
            newest_article = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((
                    By.XPATH, 
                    "//span[contains(@title, 'Code')]"))    
            )
            newest_article.click()
        except:
            error_message = "Code article not found"
            self.error_notifier.send_error(error_message)
            self.driver.quit()
            return

        # Look for the code link, click when found, and return the links.
        try:
            codes = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_all_elements_located((
                    By.CSS_SELECTOR, 
                    "a[href^='https://genshin.hoyoverse.com/en/gift']")))
            for link in codes:
                self.links.append(link.get_attribute('href'))
            self.driver.quit()
            return self.links
        except:
            error_message = "Code link not found"
            self.error_notifier.send_error(error_message)
            self.driver.quit()
            return
            