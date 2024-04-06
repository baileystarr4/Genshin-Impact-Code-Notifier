from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Notifier import *

class WebScraper:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        # makes chrome window pop up. for testing and error corrections
        # self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.error_notifier = Notifier()

    def find_links(self):
        # Open Brutefact's Redeem Codes and Web Events collection page on the Hoyolab website
            self.driver.get("https://www.hoyolab.com/creatorCollection/535336")

            # Leaving as comment for when they change the website again. 
            # Currently there is no log in pop-up

            # # Look for the iframe where the login popup is located
            # try:
            #     iframe = WebDriverWait(self.driver, 10).until(
            #         EC.presence_of_element_located((By.ID, 'hyv-account-sdk-frame'))
            #     )
            #     self.driver.switch_to.frame(iframe)
            # except:
            #     error_message = "Frame not found"
            #     # self.error_notifier.send_error(error_message)
            #     return error_message

            # # Look for the close button on the login pop-up and click when found.
            # try:
            #     close_button = WebDriverWait(self.driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/button'))    
            #     )
            #     close_button.click()
            # except:
            #     error_message = "Close button not found."
            #     # self.error_notifier.send_error(error_message)
            #     return error_message
            
            # Look for skip button on pop-up and click when found.
            try:
                self.driver.switch_to.default_content()
                skip_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/button'))    
                )
                skip_button.click()
            except:
                error_message = "Skip button not clicked."
                self.error_notifier.send_error(error_message)
                return 

            # Look for newest article mentioning a code and click when found.    
            try:
                newest_article = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(@title, 'Code')]"))    
                )
                newest_article.click()
            except:
                error_message = "Code article not found"
                self.error_notifier.send_error(error_message)
                return

            # Look for the code link and click when found.
            try:
                codes = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href^='https://genshin.hoyoverse.com/en/gift']"))    
                )
                links = []
                for link in codes:
                    links.append(link.get_attribute('href'))
                self.driver.quit()
                return links
            except:
                error_message = "Code link not found"
                self.error_notifier.send_error(error_message)
                return 