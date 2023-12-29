from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, strftime
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

language_button_present = EC.presence_of_element_located((By.ID, 'js-link-box-pl'))
WebDriverWait(driver, 5).until(language_button_present)

print(driver.current_url)
language_button = driver.find_element(By.ID, 'js-link-box-pl')
language_button.click()

search_text = driver.find_element(By.NAME, 'search')
search_text.send_keys("Border Collie")
search_text.send_keys(Keys.ENTER)


today = datetime.today().strftime('%Y%m%d')
time_now = datetime.now().strftime('%H%M')

driver.save_screenshot(f'./screenshots/scr_{today}{time_now}.png')





sleep(3)