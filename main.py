from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.hoyolab.com/creatorCollection/535336")

# driver.maximize_window()

# skip_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div/button")
# skip_button.click()
# codes = driver.find_element(By.CSS_SELECTOR, "title*='code'")
# print(codes)