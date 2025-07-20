<a name="day-41-50"></a>

# Days 41–50: Web Foundation - Intermediate

<details>
<summary>📋 Table of Contents</summary>

- [Days 41–50: Web Foundation - Intermediate](#days-4150-web-foundation---intermediate)
  - [Day 41: HTML Anime Ranking Project 🌸](#day-41-html-anime-ranking-project-)
  - [Day 42: HTML Birthday Invite Project 🎂](#day-42-html-birthday-invite-project-)
  - [Day 43: CSS Selectors \& Color Vocabulary 🎨](#day-43-css-selectors--color-vocabulary-)
  - [Day 44: HTML Movie Ranking Project 🎬](#day-44-html-movie-ranking-project-)
  - [Day 45: 100 Movies to Watch Web Scraper 🎥](#day-45-100-movies-to-watch-web-scraper-)
  - [Day 46: Spotify Playlist from Billboard Hot 100 Scraper 🎵](#day-46-spotify-playlist-from-billboard-hot-100-scraper-)
  - [Day 47: Amazon Price Tracker 📉](#day-47-amazon-price-tracker-)
  - [Day 48: Cookie Clicker Automation Bot 🍪](#day-48-cookie-clicker-automation-bot-)
  - [Day 49: LinkedIn Job Application Bot 🤖](#day-49-linkedin-job-application-bot-)
  - [Day 50: Tinder Auto Swipe Bot 💕](#day-50-tinder-auto-swipe-bot-)

</details>

---

## 📅 Day 41–50 Projects [10/10 Completed]

<a name="day-41-html-anime-ranking-project"></a>

## Day 41: HTML Anime Ranking Project 🌸

- **Description**: A simple HTML project that displays a personal ranking of favorite anime series. This project demonstrates the use of HTML headings, lists, and basic structure to present information in a clear and visually appealing way.
- **What I Learned**:
  - **HTML Structure** – Using headings, paragraphs, and lists for semantic content
  - **Address Formatting** – Presenting addresses with line breaks and proper tags
  - **Horizontal Rules** – Separating content visually with `<hr>`
  - **Self-Closing Tags** – Using `<br />` and others for formatting
  - **Basic Page Layout** – Organizing information for readability

### How to Use

1. Open the `index.html` file in your browser to view the anime ranking and biography content.
2. Review the HTML structure in a code editor to learn about headings, paragraphs, and formatting tags.

### Prerequisites

- Any modern web browser (Chrome, Firefox, Edge, etc.)
- No additional dependencies required

### Link to Code

[View Code →](Day41/Anime%20Ranking%20Project/index.html)

---

<a name="day-42-html-birthday-invite-project"></a>

## Day 42: HTML Birthday Invite Project 🎂

- **Description**: A fun HTML project that creates a birthday invitation web page. This project demonstrates the use of images, links, lists, and semantic HTML to present event information.
- **What I Learned**:
  - **Image Elements** – Using `<img>` with `src` and `alt` attributes
  - **Anchor Tags** – Creating clickable links with `<a>` and `href`
  - **Lists** – Organizing items with `<ul>` and `<li>`
  - **Semantic Structure** – Structuring event details for clarity
- **How to Use**:
  1. Open the `index.html` file in the `Day42/Birthday Invite Project` folder to view the invitation.
  2. Explore the code to see how images and links are used in HTML.
- **Prerequisites**:
  - Any modern web browser
  - No additional dependencies required

### Link to Code

[View Code →](Day42/Birthday%20Invite%20Project/index.html)

---

<a name="day-43-css-selectors--color-vocabulary"></a>

## Day 43: CSS Selectors & Color Vocabulary 🎨

- **Description**: This day covers two projects focused on learning and applying CSS selectors and styling:
  1. **CSS Selectors** – Practice using element, class, id, attribute, and universal selectors to style HTML elements.
  2. **Color Vocabulary** – Style a vocabulary list of Spanish color names, matching each color word to its meaning using CSS.
- **What I Learned**:
  - **Element, Class, and ID Selectors** – Targeting HTML elements in different ways
  - **Attribute Selectors** – Styling elements based on attributes and values
  - **Universal Selector** – Applying styles to all elements
  - **External, Internal, and Inline CSS** – Three ways to add CSS to HTML
  - **Image Styling** – Setting image dimensions with CSS
- **How to Use**:
  1. Open the `index.html` files in the `Day43/CSS Selectors` and `Day43/Color-Vocab-Project` folders to see the styled pages.
  2. Review the corresponding CSS files to understand how selectors are used.
- **Prerequisites**:
  - Any modern web browser
  - No additional dependencies required

### Link to Code

- [Color Vocabulary Project](Day43/Color-Vocab-Project/index.html)

---

<a name="day-44-html-movie-ranking-project"></a>

## Day 44: HTML Movie Ranking Project 🎬

- **Description**: A simple HTML project that displays a personal ranking of favorite movies. This project demonstrates the use of HTML headings, ordered lists, and basic structure to present information clearly.
- **What I Learned**:
  - **Ordered Lists** – Using `<ol>` and `<li>` to create ranked lists
  - **Semantic HTML** – Structuring content for clarity and accessibility
  - **Page Layout** – Organizing sections with headings and paragraphs

### How to Use

1. Open the `index.html` file in your browser to view the movie ranking.
2. Review the HTML code to learn about ordered lists and semantic structure.

### Prerequisites

- Any modern web browser
- No additional dependencies required

### Link to Code

[View Code →](./Day44/Motivation%20Meme%20Project/index.html)

---

<a name="day-45-100-movies-to-watch-web-scraper"></a>

## Day 45: 100 Movies to Watch Web Scraper 🎥

- **Description**: Scrape the top 100 movies of all time from a preserved web page using BeautifulSoup and Requests. The script extracts movie titles and writes them in ascending order to a text file.
- **What I Learned**:
  - **Web Scraping** – Using Requests to fetch web content and BeautifulSoup to parse HTML
  - **HTML Parsing** – Locating elements by tag and class
  - **Data Extraction** – Collecting and reversing lists to match required order
  - **File Writing** – Outputting results to a `.txt` file with proper encoding
- **How to Use**:
  1. Run `main.py` in the `Day45/100 movies to watch start` folder.
  2. Check the generated `movies.txt` file for the list of movies.
- **Prerequisites**:
  - Python 3.x
  - `requests` and `beautifulsoup4` libraries

### Link to Code

[View Code →](./Day45/100%20movies%20to%20watch%20start/main.py)

---

<a name="day-46-spotify-playlist-from-billboard-hot-100-scraper-"></a>

## Day 46: Spotify Playlist from Billboard Hot 100 Scraper 🎵

- **Description**: Scrape the Billboard Hot 100 chart for a given date and automatically create a Spotify playlist with the top 100 songs. Includes a variant for the Billboard India chart.
- **What I Learned**:
  - **Web Scraping** – Extracting song titles from Billboard using BeautifulSoup and Requests
  - **Spotify API** – Authenticating and interacting with Spotify using Spotipy
  - **OAuth2 Authentication** – Handling user login and permissions for playlist creation
  - **Error Handling** – Managing missing songs and API search failures
  - **Environment Variables** – Securing API credentials with dotenv
- **How to Use**:
  1. Set up a `.env` file with your Spotify API credentials.
  2. Run `main.py` to create a playlist from the US Billboard Hot 100 for any date.
  3. Run `hot_hindi.py` to create a playlist from the Billboard India chart for any date.
  4. Check your Spotify account for the new playlist.
- **Prerequisites**:
  - Python 3.x
  - `requests`, `beautifulsoup4`, `spotipy`, `python-dotenv`
  - Spotify Developer account and app credentials

### Link to Code

- [US Billboard Hot 100 Scraper](Day46/main.py)
- [Billboard India Scraper](Day46/hot_hindi.py)

---

<a name="day-47-amazon-price-tracker-"></a>

## Day 47: Amazon Price Tracker 📉

- **Description**: Track the price of a product on Amazon and receive an email notification when the price drops below a target value. Includes a demo for a sample site and a script for Amazon India.
- **What I Learned**:
  - **Web Scraping** – Extracting product prices from Amazon and demo sites using BeautifulSoup and Requests
  - **Email Automation** – Sending email alerts with SMTP when price conditions are met
  - **Environment Variables** – Managing sensitive credentials with dotenv
  - **Error Handling** – Handling missing elements and connection issues gracefully
- **How to Use**:
  1. Set up a `.env` file with your email credentials and recipient.
  2. Adjust the target price and product URL as needed in the scripts.
  3. Run `main.py` for the demo site or `amazon.py` for Amazon India.
  4. Receive an email alert if the price drops below your target.
- **Prerequisites**:
  - Python 3.x
  - `requests`, `beautifulsoup4`, `python-dotenv`
  - Gmail or compatible SMTP email account

### Link to Code

- [Demo Price Tracker](Day47/main.py)
- [Amazon India Price Tracker](Day47/amazon.py)

---

<a name="day-48-cookie-clicker-automation-bot-"></a>

## Day 48: Cookie Clicker Automation Bot 🍪

- **Description**: A Selenium-based automation bot that plays the Cookie Clicker game autonomously, maximizing cookies per second (CPS) by implementing intelligent clicking and purchasing strategies.
- **What I Learned**:
  - **Browser Automation** – Using Selenium WebDriver to control Chrome browser interactions
  - **Dynamic Element Selection** – Finding and interacting with web elements using various selection methods
  - **Game Strategy Algorithms** – Implementing logic to buy the most expensive affordable item
  - **Error Handling** – Managing exceptions and browser issues in automation scripts
- **How to Use**:
  1. Run `main.py` in the `Day48/Cookie Clicker Project` folder to start the bot.
  2. The bot will automatically click the cookie and purchase upgrades for 5 minutes.
  3. Final cookie count is displayed at the end.
- **Prerequisites**:
  - Python 3.x
  - `selenium` for web automation
  - Chrome browser and ChromeDriver

### Link to Code

- [Cookie Clicker Bot](Day48/Cookie%20Clicker%20Project/main.py)

---

<a name="day-49-linkedin-job-application-bot"></a>

## Day 49: LinkedIn Job Application Bot 🤖

- **Description**: An automation bot built with Selenium that logs into LinkedIn, navigates to job listings, and can automate the application process for jobs matching specific criteria. The script demonstrates browser automation, form filling, and handling pop-ups for a real-world job search scenario.
- **What I Learned**:
  - **Selenium WebDriver** – Automating browser actions and navigation
  - **Element Selection** – Using CSS selectors, class names, and IDs to interact with web elements
  - **Form Automation** – Filling out login and application forms programmatically
  - **Error Handling** – Managing exceptions and modal dialogs during automation
  - **User Interaction** – Pausing for manual CAPTCHA solving
- **How to Use**:
  1. Install required packages: `pip install selenium webdriver-manager`.
  2. Set your LinkedIn credentials and ChromeDriver path in `main.py`.
  3. Run `main.py` in the `Day49` folder.
  4. Manually solve any CAPTCHA if prompted, then let the bot proceed with job applications.
- **Prerequisites**:
  - Python 3.x
  - `selenium`, `webdriver-manager` libraries
  - Chrome browser and ChromeDriver
  - LinkedIn account

### Link to Code

- [LinkedIn Job Application Bot](Day49/main.py)

---

<a name="day-50-tinder-auto-swipe-bot-"></a>

## Day 50: Tinder Auto Swipe Bot 💕

- **Description**: A Selenium-based bot that automates swiping on Tinder profiles. The bot can be configured to swipe right (like) or left (pass) based on user preferences and profile information.
- **What I Learned**:
  - **Selenium WebDriver** – Advanced browser automation techniques
  - **XPath and CSS Selectors** – Locating elements with precision
  - **Randomization in Automation** – Introducing variability in swipe patterns
  - **Handling Dynamic Content** – Dealing with AJAX-loaded elements and infinite scrolling
  - **Ethical Considerations** – Understanding the implications of automating interactions on dating platforms
- **How to Use**:
  1. Install required packages: `pip install selenium webdriver-manager`.
  2. Set your Tinder login credentials and ChromeDriver path in `main.py`.
  3. Configure swipe preferences (right/left) and profile filters in the script.
  4. Run `main.py` in the `Day50` folder to start the bot.
  5. Monitor the bot's activity and intervene if necessary (e.g., to solve CAPTCHAs).
- **Prerequisites**:
  - Python 3.x
  - `selenium`, `webdriver-manager` libraries
  - Chrome browser and ChromeDriver
  - Tinder account

### Link to Code

- [Tinder Auto Swipe Bot](Day50/main.py)

---

