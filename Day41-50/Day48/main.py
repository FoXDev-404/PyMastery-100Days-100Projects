from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script finishes
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open a product page on Amazon India
driver.get("https://www.amazon.in/iQOO-Snapdragon-Processor-SuperComputing-Smartphone/dp/B0F83LL1D2/")

try:
    # Wait for the element containing the price to appear using class name
    price_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
    )

    # ✅ Example 1: Get text using CLASS_NAME
    # This selects an element by its class name
    price_text = price_element.get_attribute("innerText").strip()
    print(f"[CLASS_NAME] Price is ₹{price_text}")

    # ✅ Example 2: Get full price block using CSS_SELECTOR
    # price_block = driver.find_element(By.CSS_SELECTOR, "span.a-price")
    # print(f"[CSS_SELECTOR] Full price block text: {price_block.text.strip()}")

    # ✅ Example 3: Get element using ID (if known; not used here, but syntax below)
    # driver.find_element(By.ID, "priceblock_ourprice")

    # ✅ Example 4: Get search bar using NAME attribute
    # search_box = driver.find_element(By.NAME, "field-keywords")
    # search_box.send_keys("iPhone 15")

    # ✅ Example 5: Find link by full LINK_TEXT
    # deals_link = driver.find_element(By.LINK_TEXT, "Today's Deals")
    # deals_link.click()

    # ✅ Example 6: Find link by PARTIAL_LINK_TEXT
    # partial_deals = driver.find_element(By.PARTIAL_LINK_TEXT, "Deals")
    # partial_deals.click()

    # ✅ Example 7: Use TAG_NAME to get first <h1> tag
    # heading = driver.find_element(By.TAG_NAME, "h1")
    # print("[TAG_NAME] Page heading:", heading.text)

    # ✅ Example 8: Using XPATH to get the same price
    # price_xpath = driver.find_element(By.XPATH, '//span[@class="a-price-whole"]')
    # print(f"[XPATH] Price from XPath: ₹{price_xpath.text.strip()}")

except Exception as e:
    print("Price could not be found:", e)

# Note: driver.quit() is not used here due to 'detach' option.
