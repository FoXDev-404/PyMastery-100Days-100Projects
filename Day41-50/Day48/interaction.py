from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after process ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# # article_count.click()
#
# # Find elements by link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()
#
# # Find elements by name <Search>
# search = driver.find_element(By.CLASS_NAME, value="search-toggle").click()
# search_input = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
#
# # Sending keyboard input to Selenium
# search_input.send_keys("Python", Keys.ENTER)

#===== Challenge ======
driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

# FIll out the form
first_name.send_keys("Rajpal")
last_name.send_keys("Nishad")
email.send_keys("rajpal010304@gmail.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()

# driver.close()
# driver.quit()