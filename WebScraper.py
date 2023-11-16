from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebScraper:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)

    def find_links(self):
        # Open Brutefact's Redeem Codes and Web Events collection page on the Hoyolab website
            self.driver.get("https://www.hoyolab.com/creatorCollection/535336")

            # Look for the iframe where the login popup is located
            try:
                iframe = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'hyv-account-sdk-frame'))
                )
                self.driver.switch_to.frame(iframe)
            except:
                print("Frame not found")

            # Look for the close button on the login pop-up and click when found.
            try:
                close_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/button'))    
                )
                close_button.click()
            except:
                print("Close button not found.")
            
            # Look for skip button on pop-up and click when found.
            try:
                self.driver.switch_to.default_content()
                skip_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/div[1]/div/button'))    
                )
                skip_button.click()
            # Fixing close button bug where the scraper would move on without clicking close    
            except:
                print("Close button not clicked. Reopening browser")
                self.driver.quit()
                return self.find_code_and_link()

            # Look for newest article mentioning a code and click when found.    
            try:
                newest_article = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'code')]"))    
                )
                newest_article.click()
            except:
                print("Code article not found")

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
                print("Code link not found")