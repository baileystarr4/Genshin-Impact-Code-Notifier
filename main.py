from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    driver.quit()

#driver.quit()