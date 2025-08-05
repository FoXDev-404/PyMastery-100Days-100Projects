<a name="day-51-60"></a>

# Days 51–60: Web Automation & Web Development - Intermediate+

<details>
<summary>📋 Table of Contents</summary>

- [Days 51–60: Web Automation & Web Development - Intermediate+](#days-5160-web-automation--web-development---intermediate)
  - [Day 51: Internet Speed Twitter Bot 🌐](#day-51-internet-speed-twitter-bot-)
  - [Day 52: Instagram Follower Bot 📸](#day-52-instagram-follower-bot-)
  - [Day 53: Automated Data Entry with Web Scraping 📊](#day-53-automated-data-entry-with-web-scraping-)
  - [Day 54: Flask Hello World Web App 🌐](#day-54-flask-hello-world-web-app-)
  - [Day 55: Higher-Lower Server Game 🕹️](#day-55-higher-lower-server-)
  - [Day 56: Personal Portfolio Website Using Flask Server 🎨](#day-56-personal-portfolio-website-using-flask-server-)
  - [Day 57: Flask Blog Templating 📝](#day-57-flask-blog-templating-)
  - [Day 58: Bootstrap & TinDog Website 🎨](#day-58-bootstrap--tindog-website-)
  - [Day 59: Advanced Flask Blog with API Integration 🚀](#day-59-advanced-flask-blog-with-api-integration-)

</details>

---

## 📅 Day 51–60 Projects [9/10 Completed]

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

<a name="day-54-flask-hello-world-web-app"></a>

## Day 54: Flask Hello World Web App 🌐

- **Description**: A simple web application built using Flask, demonstrating the basics of web development with Python. The app displays a "Hello, World!" message and introduces routing and running a local development server.
- **What I Learned**:
  - **Flask Basics** – Setting up a Flask project and running a local server
  - **Routing** – Creating routes and handling HTTP requests
  - **Templates** – Rendering simple responses
  - **Development Server** – Running and testing a Flask app locally
- **How to Use**:
  1. Install Flask: `pip install flask`.
  2. Run `main.py` in the `Day54` folder.
  3. Open your browser and go to `http://127.0.0.1:5000/` to see the app in action.
- **Prerequisites**:
  - Python 3.x
  - `flask` library

### Features
- Simple Flask web server
- Basic route handling
- "Hello, World!" web page
- Easy to extend for more features

### Link to Code

[View Code →](Day54/main.py)

---

<a name="day-55-higher-lower-server"></a>

## Day 55: Higher-Lower Server Game 🕹️

- **Description**: A web-based version of the classic Higher-Lower game, implemented using Python and Flask. The server hosts the game logic, allowing users to guess whether the next number will be higher or lower. The project demonstrates server-side state management and basic web interaction.
- **What I Learned**:
  - **Flask Routing** – Handling multiple routes and user input
  - **Server State** – Managing game state between requests
  - **Web Forms** – Accepting and processing user guesses
  - **Basic Game Logic** – Implementing the Higher-Lower rules
- **How to Use**:
  1. Install Flask: `pip install flask`.
  2. Run `server.py` in the `Day55/higher-lower` folder.
  3. Open your browser and go to `http://127.0.0.1:5000/` to play the game.
- **Prerequisites**:
  - Python 3.x
  - `flask` library

### Features
- Interactive Higher-Lower game in the browser
- Server-side game logic and state
- Simple web interface for user input
- Easy to extend for more features

### Link to Code

[View Code →](Day55/higher-lower/server.py)

---

<a name="day-56-personal-portfolio-website"></a>

## Day 56: Personal Portfolio Website Using Flask Server 🎨

- **Description**: A personal portfolio website to showcase projects, skills, and experiences. The website is built using HTML, CSS, and JavaScript, and is hosted on GitHub Pages. This project demonstrates the fundamentals of web development and deployment.
- **What I Learned**:
  - **HTML Basics** – Structuring web content with HTML
  - **CSS Styling** – Applying styles and layouts with CSS
  - **JavaScript Basics** – Adding interactivity with JavaScript
  - **Responsive Design** – Making the website mobile-friendly
  - **GitHub Pages** – Hosting websites directly from a GitHub repository
  - **Flask Web Server** – Serving dynamic content using Python and Flask
- **How to Use**:
  1. Install Flask: `pip install flask`.
  2. Run `server.py` in the `Day56` or `Day56/name-card` folder.
  3. Open your browser and go to `http://127.0.0.1:5000/` to view your portfolio website.
  4. Customize the content in the `templates/index.html` file and update images or styles in the `static/` folder as needed.
- **Prerequisites**:
  - Python 3.x
  - Flask library (`pip install flask`)
  - Basic knowledge of HTML and CSS (for customization)

### Features
- Personal project showcase powered by Flask
- Skills and experience highlights
- Contact information section
- Responsive and mobile-friendly design
- Easy to extend with new routes or pages

### Link to Code

[View Code →](Day56/name-card/server.py)

---

<a name="day-57-flask-blog-templating"></a>

## Day 57: Flask Blog Templating 📝

- **Description**: A simple blog website built with Flask that demonstrates dynamic page rendering using Jinja templating. Blog post data is fetched from an external API and displayed on the homepage. Each post can be viewed individually by clicking the "Read" button, which uses dynamic routing to show the full content of the selected post.
- **What I Learned**:
  - **Flask Routing** – Creating dynamic routes with URL parameters
  - **Jinja Templating** – Rendering HTML templates with variables and control structures
  - **API Integration** – Fetching and parsing JSON data from an external API
  - **Separation of Concerns** – Organizing code and templates for maintainability
- **How to Use**:
  1. Install Flask and Requests: `pip install flask requests`.
  2. Run `main.py` in the `Day57/blog-templating-v1` folder.
  3. Open your browser and go to `http://127.0.0.1:5000/` to view the blog homepage.
  4. Click the "Read" button on any post to view its full content.
- **Prerequisites**:
  - Python 3.x
  - `flask`, `requests` libraries
- **Features**
  - Blog homepage with a list of posts
  - Individual post pages using dynamic routing
  - Jinja2 template rendering
  - Data fetched from an external API

### Link to Code

[View Code →](Day57/blog-templating-v1/main.py)

---

<a name="day-58-bootstrap--tindog-website"></a>

## Day 58: Bootstrap & TinDog Website 🎨

- **Description**: A responsive website for a fictional dog adoption agency, built using Bootstrap. The website showcases the use of Bootstrap components, grid system, and utilities to create a modern, mobile-first website.
- **What I Learned**:
  - **Bootstrap Framework** – Utilizing Bootstrap for responsive web design
  - **Grid System** – Implementing responsive layouts with Bootstrap's grid system
  - **Components** – Using pre-built components like navbars, cards, and modals
  - **Utilities** – Leveraging Bootstrap utilities for spacing, alignment, and visibility
  - **Custom CSS** – Overriding Bootstrap styles and adding custom styles
- **How to Use**:
  1. Download or clone the repository.
  2. Open `index.html` in your web browser to view the website.
  3. Customize content and styles as desired.
- **Prerequisites**:
  - None

### Features
- Fully responsive website design
- Bootstrap 5 components and grid system
- Customizable content and styles
- Modern and clean design

### Link to Code

[View Code →](Day58/TinDog%20Project/index.html)

---

<a name="day-59-advanced-flask-blog-with-api-integration"></a>

## Day 59: Advanced Flask Blog with API Integration 🚀

- **Description**: An advanced Flask blog application featuring dynamic content from JSON API, pagination, individual post pages with custom backgrounds, and a fully customized design branded as "Psyko Ind Blog". The project demonstrates advanced Flask concepts including template inheritance, url_for routing, and dynamic image backgrounds from Unsplash.
- **What I Learned**:
  - **Advanced Flask Templating** – Template inheritance with includes for header and footer
  - **API Integration** – Fetching blog data from npoint.io JSON API endpoints
  - **Pagination Logic** – Implementing "Older Posts" functionality with page-based navigation
  - **Dynamic Routing** – Creating individual post pages with URL parameters
  - **Jinja2 Advanced Features** – Using dot notation, for loops, and conditional rendering
  - **Custom Branding** – Personalizing templates and styling for consistent brand identity
  - **Dynamic Backgrounds** – Implementing post-specific background images from Unsplash
- **How to Use**:
  1. Install required packages: `pip install flask requests`.
  2. Create your own JSON blog data at npoint.io and update the API URL in `main.py`.
  3. Run `main.py` in the `Day59/upgraded blog` folder.
  4. Open your browser and go to `http://127.0.0.1:5000/` to view the blog.
  5. Navigate through posts using pagination and click on individual posts to view them.
- **Prerequisites**:
  - Python 3.x
  - `flask`, `requests` libraries
  - JSON API endpoint (npoint.io or similar)

### Features
- Dynamic blog content from JSON API
- Pagination with "Older Posts" functionality (4 posts per page)
- Individual post pages with custom Unsplash backgrounds
- Template inheritance with reusable header and footer
- Fully branded "Psyko Ind" design
- About and Contact pages with personalized content
- GitHub profile link in footer
- Responsive Bootstrap-based design
- Clean, organized code structure

### Link to Code

[View Code →](Day59/upgraded%20blog/main.py)

---

*More days coming soon...*
