from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Open Brutefact's Redeem Codes and Web Events collection page on the Hoyolab website
driver.get("https://www.hoyolab.com/creatorCollection/535336")

# Look for the iframe where the login popup is located
try:
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'hyv-account-frame'))
    )
    driver.switch_to.frame(iframe)
except:
    print("Frame not found")

# Look for the close button on the login pop-up and click when found.
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/button'))    
    )
    close_button.click()
except:
    print("Close button not found")

# Look for skip button on pop-up and click when found.
try:
    driver.switch_to.default_content()
    skip_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/div[1]/div/button'))    
    )
    skip_button.click()
except:
    print("Skip button not found")

# Look for newest article mentioning a code and click when found.    
try:
    newest_article = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'code')]"))    
    )
    newest_article.click()
except:
    print("Code article not found")

# Look for the code link and click when found.
try:
    code = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href^='https://genshin.hoyoverse.com/en/gift']"))    
    )
    code.click()
except:
    print("Code link not found")