from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://a.co/d/e26OpX7")
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Find element by Name
search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)
print(search_bar.get_property("placeholder"))

# Find element by ID
button = driver.find_element(By.ID, "submit")
print(button.size)

# Find element by CSS Selectors
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)


# driver.close()
driver.quit()