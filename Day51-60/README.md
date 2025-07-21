<a name="day-51-60"></a>

# Days 51–60: Web Automation & API Integration - Advanced

<details>
<summary>📋 Table of Contents</summary>

- [Days 51–60: Web Automation & API Integration - Advanced](#days-5160-web-automation--api-integration---advanced)
  - [Day 51: Internet Speed Twitter Bot 🌐](#day-51-internet-speed-twitter-bot-)

</details>

---

## 📅 Day 51–60 Projects [1/10 Completed]

<a name="day-51-internet-speed-twitter-bot"></a>

## Day 51: Internet Speed Twitter Bot 🌐

- **Description**: An automated bot that tests your internet speed using Speedtest.net and tweets at your internet service provider if the speeds are below what you're paying for. The bot handles cookie consent, performs speed tests, logs into Twitter/X, and posts complaint tweets automatically.
- **What I Learned**:
  - **Selenium WebDriver** – Advanced browser automation for web scraping and interaction
  - **Environment Variables** – Secure storage of credentials using `.env` files for sensitive data
  - **Web Element Location** – Finding elements using XPath, CSS selectors, and other locators
  - **WebDriverWait** – Handling dynamic content and waiting for elements to load properly
  - **Social Media Automation** – Automated posting to Twitter/X with error handling
  - **Exception Handling** – Managing various scenarios like verification steps and missing elements
- **How to Use**:
  1. Install required packages: `pip install selenium webdriver-manager python-dotenv`.
  2. Create a `.env` file with your Twitter credentials (`TWITTER_EMAIL`, `TWITTER_USERNAME`, `TWITTER_PASSWORD`).
  3. Set your promised internet speeds in the script (`PROMISED_DOWN`, `PROMISED_UP`).
  4. Run `main.py` in the `Day51` folder.
  5. The bot will test your internet speed and tweet if speeds are below promised values.
- **Prerequisites**:
  - Python 3.x
  - `selenium`, `webdriver-manager`, `python-dotenv` libraries
  - Chrome browser and ChromeDriver (automatically managed)
  - Twitter/X account with login credentials

### Features
- Automated internet speed testing using speedtest.net
- Cookie consent handling for GDPR compliance
- Twitter/X login automation with verification step handling
- Automated tweet composition and posting
- Speed comparison with promised speeds
- Comprehensive error handling for various scenarios

### Link to Code

[View Code →](Day51/main.py)

---

*More days coming soon...*
