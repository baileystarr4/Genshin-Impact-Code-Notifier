from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.hoyolab.com/creatorCollection/535336")

# driver.maximize_window()
# time.sleep(10)
try:
    skip_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/div[1]/div/button'))    
    )
    skip_button.click()
except:
    print("NOT FOUND 1")
try:
    newest_article = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'code')]"))    
    )
    newest_article.click()
except:
    print("NOT FOUND 2")
# try:
#     code = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "a[href^='https://genshin.hoyoverse.com/en/gift']"))    
#     )
#     code.click()
# except:
#     print("NOT FOUND 3")
try:
    code = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href^='https://genshin.hoyoverse.com/en/gift']"))    
    )
    code.click()
except:
    print("NOT FOUND 4")