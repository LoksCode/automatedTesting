from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
sleep(5)