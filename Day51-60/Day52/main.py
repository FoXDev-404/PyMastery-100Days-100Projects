import time
import os
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

# Login information
EMAIL = os.getenv("INSTA_EMAIL")
USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")
INSTAGRAM_URL = "https://www.instagram.com/"

class InstaFollower:

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=self.chrome_options)
        self.driver.get(INSTAGRAM_URL)

    def login(self):
        time.sleep(5)
        # Enter username
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(USERNAME)

        # Enter password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)

        # Click login button
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        self.delay()

        # Handle "Save Your Login Info" popup
        try:
            not_now_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
            not_now_button.click()
            self.delay()
        except NoSuchElementException:
            print("No 'Save Login Info' popup found")

        # Handle notifications popup
        try:
            not_now_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
            not_now_button.click()
            self.delay()
        except NoSuchElementException:
            print("No notifications popup found")

    def delay(self):
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)

    def find_followers(self):
        # Navigate to search
        search_icon = self.driver.find_element(By.XPATH, "//span[contains(@class, 'x1lliihq') and contains(@class, 'x1plvlek')]//span[text()='Search']")
        search_icon.click()
        self.delay()

        # Search for the target account
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.send_keys("mad_about_food")
        time.sleep(3)

        # Click on the first result
        first_result = self.driver.find_element(By.XPATH, "//div[@role='button']//span[contains(text(), 'mad_about_food')]")
        first_result.click()
        self.delay()

        # Click on followers
        followers_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
        followers_link.click()
        self.delay()

    def follow(self):
        # Scroll and follow users
        for i in range(10):
            try:
                # Find follow buttons (more reliable selector)
                follow_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Follow']")

                if follow_buttons:
                    follow_buttons[0].click()
                    print(f"Followed user {i + 1}")
                    self.delay()

                    # Scroll down to load more users
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                             self.driver.find_element(By.XPATH, "//div[@role='dialog']"))
                    time.sleep(2)
                else:
                    print("No more follow buttons found")
                    break

            except NoSuchElementException as e:
                print(f"Error following user {i + 1}: {e}")
                continue
            except Exception as e:
                print(f"Unexpected error: {e}")
                break

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    if not all([EMAIL, USERNAME, PASSWORD]):
        print("Please set INSTA_EMAIL, INSTA_USER, and INSTA_PASS environment variables")
        exit(1)

    insta_bot = InstaFollower()
    try:
        insta_bot.login()
        time.sleep(10)
        insta_bot.find_followers()
        time.sleep(5)
        insta_bot.follow()
        print("Well done, Congrats!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press Enter to close the browser...")
        insta_bot.quit()
