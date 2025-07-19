from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

FB_EMAIL = 'YOUR FACEBOOK LOGIN EMAIL'
FB_PASSWORD = 'YOUR FACEBOOK PASSWORD'

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()