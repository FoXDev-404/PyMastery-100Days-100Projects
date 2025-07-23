<a name="day-51-60"></a>

# Days 51–60: Web Automation & Web Development - Intermediate+

<details>
<summary>📋 Table of Contents</summary>

- [Days 51–60: Web Automation & Web Development - Intermediate+](#days-5160-web-automation--web-development---intermediate)
  - [Day 51: Internet Speed Twitter Bot 🌐](#day-51-internet-speed-twitter-bot-)
  - [Day 52: Instagram Follower Bot 📸](#day-52-instagram-follower-bot-)
  - [Day 53: Automated Data Entry with Web Scraping 📊](#day-53-automated-data-entry-with-web-scraping-)

</details>

---

## 📅 Day 51–60 Projects [3/10 Completed]

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

<a name="day-52-instagram-follower-bot"></a>

## Day 52: Instagram Follower Bot 📸

- **Description**: An automated bot that uses Selenium to log into Instagram, search for a specific account (mad_about_food), navigate to their followers list, and automatically follow multiple users. The bot includes proper delay mechanisms and error handling to avoid detection.
- **What I Learned**:
  - **Advanced Selenium Automation** – Complex Instagram web interface navigation and interaction
  - **Social Media Bot Development** – Building bots for follower growth and engagement
  - **Dynamic Element Handling** – Working with Instagram's dynamic and frequently changing web elements
  - **Random Delays** – Implementing human-like behavior patterns to avoid bot detection
  - **Popup Management** – Handling Instagram's "Save Login Info" and notification popups
  - **Scrolling Automation** – Programmatically scrolling through follower lists to load more content
- **How to Use**:
  1. Install required packages: `pip install selenium webdriver-manager python-dotenv`.
  2. Create a `.env` file with your Instagram credentials (`INSTA_EMAIL`, `INSTA_USER`, `INSTA_PASS`).
  3. Run `main.py` in the `Day52` folder.
  4. The bot will login, search for the target account, and follow 10 users from their followers list.
  5. Browser will remain open until you press Enter to close it.
- **Prerequisites**:
  - Python 3.x
  - `selenium`, `webdriver-manager`, `python-dotenv` libraries
  - Chrome browser and ChromeDriver (automatically managed)
  - Instagram account with login credentials

### Features
- Automated Instagram login with popup handling
- Search functionality for target accounts
- Followers list navigation and interaction
- Automated following with human-like delays
- Scroll automation to load more followers
- Comprehensive error handling and logging
- Browser session management with manual close option

### Link to Code

[View Code →](Day52/main.py)

---

<a name="day-53-automated-data-entry-with-web-scraping"></a>

## Day 53: Automated Data Entry with Web Scraping 📊

- **Description**: A project that automates the process of logging into a website and entering data into a form using information scraped from another website. This project demonstrates the integration of web scraping and web automation to automate repetitive data entry tasks.
- **What I Learned**:
  - **Data Scraping** – Extracting data from websites using BeautifulSoup and Requests
  - **Form Automation** – Automating form filling and submission on websites
  - **Session Management** – Managing user sessions and cookies for authenticated requests
  - **Error Handling** – Implementing robust error handling for network requests and form submissions
  - **Data Parsing** – Parsing and processing scraped data for automated input
- **How to Use**:
  1. Install required packages: `pip install requests beautifulsoup4 selenium webdriver-manager python-dotenv`.
  2. Create a `.env` file with your website login credentials (`SITE_EMAIL`, `SITE_USER`, `SITE_PASS`).
  3. Set the target URL and form data in the script.
  4. Run `main.py` in the `Day53` folder.
  5. The script will scrape data from the source website and submit it to the target website.
- **Prerequisites**:
  - Python 3.x
  - `requests`, `beautifulsoup4`, `selenium`, `webdriver-manager`, `python-dotenv` libraries
  - Chrome browser and ChromeDriver (automatically managed)
  - Accounts on the source and target websites

### Features
- Automated data scraping and parsing
- Form filling and submission automation
- Session and cookie management
- Comprehensive error handling and logging
- Configurable target URL and form data

### Link to Code

[View Code →](Day53/main.py)

---

*More days coming soon...*
