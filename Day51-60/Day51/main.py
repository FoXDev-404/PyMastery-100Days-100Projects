from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_DOWN = 150
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        # Accept cookie consent if present
        try:
            consent_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            consent_button.click()
            print("Accepted cookie consent.")
            time.sleep(2)
        except:
            print("No cookie banner detected.")

        # Click the Go button and start speed test
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        print("Speed test started... waiting 60 seconds...")
        time.sleep(60)  # Wait for test to complete

        self.down = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get('https://x.com/i/flow/login')
        wait = WebDriverWait(self.driver, 20)
        username_input = wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
        )))
        username_input.send_keys(TWITTER_USERNAME)
        username_input.send_keys(Keys.ENTER)
        time.sleep(3)

        try:
            verify_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
            verify_input.send_keys(TWITTER_EMAIL)
            verify_input.send_keys(Keys.ENTER)
            print("Verification step completed.")
            time.sleep(3)
        except:
            print("No verification step needed.")

        password_input = wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        )))
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        post_input = wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        post_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        # post_button.click()



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

input("✅ Done. Press Enter to exit (and manually close browser)...")