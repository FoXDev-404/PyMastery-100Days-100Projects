from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after process ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

no_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(f"{no_of_articles.text} articles in English")

# driver.close()
driver.quit()