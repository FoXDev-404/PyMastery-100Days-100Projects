import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker")

# Wait for language selection
wait = WebDriverWait(driver, 10)
select_language = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
select_language.click()

# Run clicking loop for 5 minutes
timeout = time.time() + 60 * 5  # 5 minutes from now
cookie = driver.find_element(By.ID, value="bigCookie")

while time.time() < timeout:
    cookie.click()
