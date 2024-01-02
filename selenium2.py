from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from datetime import datetime

logins_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user',
               'error_user', 'visual_user']

password = 'secret_sauce'
driver = webdriver.Chrome()


for i in logins_list:
    driver.get("https://www.saucedemo.com/")

    login_field = driver.find_element(By.ID, 'user-name')
    login_field.send_keys(i)

    pass_field = driver.find_element(By.ID, 'password')
    pass_field.send_keys("secret_sauce")
    pass_field.send_keys(Keys.ENTER)

    if driver.current_url == 'https://www.saucedemo.com/inventory.html':
        print(f"Test Passed - the username and password were correct, page loaded successfully - Logged in on login '{i}'")
    else:
        print(f"Test failed - error occurred - didn't login on login: '{i}'")
        today = datetime.today().strftime('%Y%m%d')
        time_now = datetime.now().strftime('%H%M')
        driver.save_screenshot(f'./screenshots/scr_{today}{time_now}.png')