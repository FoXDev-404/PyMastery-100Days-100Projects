# Automating Data Entry with Web Scraping
from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import time

# Web scraping part
response = requests.get("https://appbrewery.github.io/Zillow-Clone")
soup = BeautifulSoup(response.content, 'html.parser')

property_price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
property_prices = []
for price in property_price:
    cleaned_price = price.get_text().strip()
    cleaned_price = re.sub(r'\+.*', '', cleaned_price)
    cleaned_price = re.sub(r'/.*', '', cleaned_price)
    cleaned_price = cleaned_price.strip()
    property_prices.append(cleaned_price)

property_address = soup.find_all('address', {'data-test': 'property-card-addr'})
property_addresses = []
for address in property_address:
    cleaned_address = address.get_text().strip()
    cleaned_address = re.sub(r'\n+', ' ', cleaned_address)
    cleaned_address = cleaned_address.replace('|', '')
    cleaned_address = re.sub(r'\s+', ' ', cleaned_address)
    property_addresses.append(cleaned_address.strip())

property_links = soup.find_all(name="a", class_="property-card-link")
property_urls = [link.get("href") for link in property_links]

print(f"Found {len(property_prices)} properties to process...")

# Selenium Part Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdqVBqoy-mGZ-nMOHLufjv6QLwImPjVALBvUOclS8GJkm2ILg/viewform?usp=header"

# Fill form for each property
for i in range(len(property_prices)):
    print(f"Processing property {i+1}/{len(property_prices)}")

    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Open form URL
            driver.get(form_url)

            # Wait longer for form to fully load
            wait = WebDriverWait(driver, 15)
            time.sleep(3)

            # Wait for the first input to be clickable
            address_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @aria-labelledby]")))
            address_input.clear()
            address_input.send_keys(property_addresses[i])

            # Find all text inputs
            time.sleep(1)
            text_inputs = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='text' and @aria-labelledby]")))

            # Wait for elements to appear
            if len(text_inputs) > 1:
                price_input = wait.until(EC.element_to_be_clickable(text_inputs[1]))
                price_input.clear()
                price_input.send_keys(property_prices[i])

            if len(text_inputs) > 2:
                link_input = wait.until(EC.element_to_be_clickable(text_inputs[2]))
                link_input.clear()
                link_input.send_keys(property_urls[i])

            time.sleep(2)

            # Submit the form
            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')] | //div[@role='button'][contains(., 'Submit')]")))
            driver.execute_script("arguments[0].click();", submit_button)

            time.sleep(3)

            print(f"Submitted property {i+1}: {property_addresses[i]}")
            break

        except (TimeoutException, ElementNotInteractableException) as e:
            retry_count += 1
            print(f"Attempt {retry_count} failed for property {i+1}, retrying...")
            if retry_count >= max_retries:
                print(f"Failed to process property {i+1} after {max_retries} attempts: {property_addresses[i]}")
            else:
                time.sleep(5)
        except Exception as e:
            print(f"Unexpected error processing property {i+1}: {e}")
            break

print("Form submission completed!")
input("Press enter to exit...")
driver.close()
driver.quit()
