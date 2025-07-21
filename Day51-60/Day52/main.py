from selenium import webdriver


SIMILAR_ACCOUNT = 'INSTAGRAM ACCOUNT YOU WANT TO BECOME'
USERNAME = 'YOUR INSTAGRAM EMAIL'
PASSWORD = 'YOUR INSTAGRAM PASSWORD'


class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()