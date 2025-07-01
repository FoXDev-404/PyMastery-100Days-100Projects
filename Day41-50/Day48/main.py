from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/iQOO-Snapdragon-Processor-SuperComputing-Smartphone/dp/B0F83LL1D2/")

try:
    # Wait for the price element to be present
    price_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
    )

    # Use get_attribute instead of .text to reliably fetch text
    price_text = price_element.get_attribute("innerText").strip()

    print(f"The price is ₹{price_text}")

except Exception as e:
    print("Price could not be found:", e)

# driver.quit()  # Optional if using detach
