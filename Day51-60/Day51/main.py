from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'YOUR TWITTER EMAIL'
TWITTER_PASSWORD = 'YOUR TWITTER PASSWORD'

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
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
