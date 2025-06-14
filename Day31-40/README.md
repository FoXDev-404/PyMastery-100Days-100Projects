<a name="day-31-40"></a>

# Days 31–40: Advanced Python Projects

<details>
<summary>📋 Table of Contents</summary>

- [Day 31: Flash Card App](#day-31-flash-card-app)
- [Day 32: Birthday Wisher](#day-32-birthday-wisher)
- [Day 33: ISS Tracker](#day-33-iss-tracker)
- [Day 34: Quiz App](#day-34-quiz-app)
- [Day 35: Weather Alert System](#day-35-weather-alert-system)
- [Day 36: Stock News SMS Alert](#day-36-stock-news-sms-alert)
- [Day 37: Habit Tracker](#day-37-habit-tracker)
- [Day 38: Workout Tracker](#day-38-workout-tracker)
- [Day 39: Flight Deals Project](#day-39-flight-deals-project)
  <!-- Add more days as they are completed -->
  </details>

## 📅 Day 31–40 Projects [9/10 Completed]

---

<a name="day-31-flash-card-app"></a>

## Day 31: Flash Card App 🗣️

- **Description**: A language learning application that uses digital flash cards to help users memorize French vocabulary.
- **What I Learned**:
  - **Tkinter UI Development** – Creating a polished user interface with Canvas and images
  - **Timer Management** – Using window.after() to schedule operations and handle timeouts
  - **State Tracking** – Managing card flipping and word learning states
  - **Data Persistence** – Saving progress to files to continue learning across sessions
  - **Error Handling** – Gracefully handling file operations and potential errors

### Features

- Digital flash cards showing French words and their English translations
- Automatic card flipping after 3 seconds to reveal translations
- Progress tracking to focus on unlearned words
- Visual feedback with different card designs for front/back
- Intuitive buttons for marking words as known/unknown
- Persistent storage of learning progress

### How to Use

1. Run the script using `python main.py` in the `Day31` directory.
2. A French word will appear on the screen.
3. Try to recall the English translation before the card flips automatically.
4. After the card flips (or you've made your guess), either:
   - Click the ✓ button if you knew the word (removes it from your learning pile)
   - Click the ✗ button if you didn't know it (keeps it for future review)
5. Your progress is automatically saved between sessions.

### Prerequisites

- Python 3.8 or higher
- Tkinter (included with Python)
- Pandas library (`pip install pandas`)
- Flash card images in the "images" directory
- French words data file in the "data" directory

### Link to Code

[View Code →](Day31/main.py)

---

<a name="day-32-birthday-wisher"></a>

## Day 32: Birthday Wisher 📧

- **Description**: An automated email system that sends birthday wishes to contacts on their special day.
- **What I Learned**:
  - **Email Automation** – Using SMTP protocol to programmatically send emails
  - **Environment Variables** – Securing sensitive information like passwords
  - **Date & Time Handling** – Working with datetime to check for birthdays
  - **String Templates** – Creating personalized email content with dynamic data
  - **CSV Data Processing** – Reading and filtering data from structured files

### Features

- Automatic birthday checks against the current date
- Personalized email messages using letter templates
- Secure credential handling via environment variables
- CSV-based contact management system
- Support for multiple email templates for variety

### How to Use

1. Run the script using `python main.py` in the `Day32` directory.
2. The app will automatically check if anyone in your contacts has a birthday today.
3. If there's a match, it will send a personalized birthday email from your account.
4. Add new contacts to the birthdays.csv file to include them in future checks.

### Prerequisites

- Python 3.8 or higher
- smtp library (included with Python)
- python-dotenv for environment variable management (`pip install python-dotenv`)
- Gmail account (or other email provider) with app password configured
- CSV file with birthday information

### Link to Code

[View Code →](Day32/birthday-wisher/main.py)

---

<a name="day-33-iss-tracker"></a>

## Day 33: ISS Tracker 🛰️

- **Description**: An application that tracks the real-time location of the International Space Station using public APIs.
- **What I Learned**:
  - **API Integration** – Making HTTP requests to external APIs to fetch real-time data
  - **JSON Parsing** – Processing and extracting information from JSON responses
  - **Error Handling** – Implementing robust exception handling for network requests
  - **HTTP Status Codes** – Understanding and properly handling different response codes
  - **Alternative Solutions** – Finding and implementing fallback options when primary APIs fail

### Features

- Real-time tracking of the ISS's current latitude and longitude
- Proper error handling for connection issues
- Clean display of tracking data including timestamps
- Implementation of robust API request patterns
- Fallback to alternative data sources when needed

### How to Use

1. Run the script using `python main.py` in the `Day33` directory.
2. The application will connect to the ISS tracking API and retrieve the current location.
3. The latitude, longitude, and timestamp will be displayed in the console.
4. The data refreshes each time you run the script, giving you the latest position.

### Prerequisites

- Python 3.8 or higher
- Requests library (`pip install requests`)
- Internet connection to access the API

### Link to Code

[View Code →](Day33/main.py)

---

<a name="day-34-quiz-app"></a>

## Day 34: Quiz App 🧠

- **Description**: A Trivia Quiz application that fetches questions from an API and tests the user's knowledge through a GUI interface.
- **What I Learned**:
  - **API Integration with UI** – Combining API requests with Tkinter for a complete application
  - **Object-Oriented Design** – Creating a well-structured multi-class application
  - **Quiz Logic** – Implementing scoring, question progression, and feedback systems
  - **UI/UX Design** – Building an intuitive and responsive quiz interface
  - **State Management** – Tracking quiz progress and user performance

### Features

- Dynamic quiz questions pulled from a trivia question API
- Multiple-choice answer interface with immediate feedback
- Score tracking throughout the quiz session
- Visual feedback for correct and incorrect answers
- Progress tracking to show completion percentage
- Final score display with performance summary

### How to Use

1. Run the script using `python main.py` in the `Day34` directory.
2. The app will load quiz questions from the Open Trivia Database API.
3. Answer each question by clicking "True" or "False" buttons.
4. Receive immediate feedback on your answers.
5. View your final score at the end of the quiz.
6. Option to restart the quiz with new questions.

### Prerequisites

- Python 3.8 or higher
- Tkinter (included with Python)
- Requests library (`pip install requests`)
- Internet connection to access the quiz API

### Link to Code

[View Code →](Day34/main.py)

---

<a name="day-35-weather-alert-system"></a>

## Day 35: Weather Alert System ☔

- **Description**: A weather monitoring application that sends SMS alerts when rain is forecasted in your area using OpenWeatherMap API and Twilio.
- **What I Learned**:
  - **Weather API Integration** – Fetching and processing forecast data from OpenWeatherMap
  - **SMS Notification System** – Using Twilio API to send automated text messages
  - **Environment Variables** – Securing API keys and sensitive credentials
  - **Error Handling** – Implementing robust exception handling for API requests
  - **Weather Data Analysis** – Interpreting weather condition codes to determine rain probability

### Features

- Real-time weather forecast retrieval for New Delhi, India
- Automated SMS notifications when rain is expected
- Secure credential management using environment variables
- Robust error handling for API failures
- Weather condition analysis using OpenWeatherMap condition codes
- Customizable alert messages with emojis

### How to Use

1. Set up environment variables in a `.env` file:
   - `OWM_API_KEY` (OpenWeatherMap API key)
   - `TWILIO_ACCOUNT_SID` (Twilio account SID)
   - `TWILIO_AUTH_TOKEN` (Twilio auth token)
   - `TWILIO_MESSAGING_SERVICE_SID` (Twilio messaging service)
   - `PHONE_NUMBER` (Your phone number for alerts)
2. Run the script using `python main.py` in the `Day35` directory.
3. The app will check the weather forecast for the next 12 hours.
4. If rain is detected, you'll receive an SMS alert automatically.

### Prerequisites

- Python 3.8 or higher
- Requests library (`pip install requests`)
- Twilio library (`pip install twilio`)
- python-dotenv (`pip install python-dotenv`)
- OpenWeatherMap API account
- Twilio account with SMS credits

### Link to Code

[View Code →](Day35/main.py)

---

<a name="day-36-stock-news-sms-alert"></a>

## Day 36: Stock News SMS Alert 📈

- **Description**: A stock monitoring application that sends SMS alerts with the latest news headlines when a significant price change is detected for a given stock (e.g., Tesla Inc).
- **What I Learned**:
  - **Stock API Integration** – Fetching and analyzing intraday stock data from Alpha Vantage
  - **News API Integration** – Retrieving relevant news articles using NewsAPI
  - **SMS Notification System** – Sending formatted news alerts via Twilio SMS
  - **Environment Variables** – Managing sensitive API keys and credentials securely
  - **Data Analysis** – Calculating percentage changes and filtering news
  - **Error Handling** – Managing API errors and missing data gracefully

### Features

- Monitors stock price changes using Alpha Vantage intraday data
- Fetches top 3 relevant news headlines if a significant price change is detected
- Sends each news headline as a separate SMS using Twilio
- Secure credential management with environment variables
- Clear and concise SMS formatting with stock movement indicators

### How to Use

1. Set up environment variables in a `.env` file:
   - `STOCK_API_KEY` (Alpha Vantage API key)
   - `NEWS_API_KEY` (NewsAPI key)
   - `TWILIO_ACCOUNT_SID` (Twilio account SID)
   - `TWILIO_AUTH_TOKEN` (Twilio auth token)
   - `TWILIO_MESSAGING_SERVICE_SID` (Twilio messaging service SID)
   - `PHONE_NUMBER` (Your phone number for alerts)
2. Run the script using `python main.py` in the `Day36` directory.
3. The app will check the latest stock price and send SMS news alerts if a significant change is detected.

### Prerequisites

- Python 3.8 or higher
- Requests library (`pip install requests`)
- Twilio library (`pip install twilio`)
- python-dotenv (`pip install python-dotenv`)
- Alpha Vantage and NewsAPI accounts
- Twilio account with SMS credits

### Link to Code

[View Code →](Day36/main.py)

---

<a name="day-37-habit-tracker"></a>

## Day 37: Habit Tracker 📊

- **Description**: A habit tracking application that visualizes daily coding hours using the Pixela API to create a GitHub-like contribution graph.
- **What I Learned**:
  - **HTTP Methods** – Using GET, POST, PUT, and DELETE methods for API interaction
  - **Request Headers** – Adding authentication tokens to secure API requests
  - **Date Handling** – Converting and formatting dates for API compatibility
  - **User Input Processing** – Taking and validating user input for data entry
  - **API Documentation** – Reading and implementing features from API documentation

### Features

- Pixel-based visual habit tracking similar to GitHub's contribution graph
- Create, update, and delete tracking entries
- Record daily coding hours with precision (floating point values)
- Automatic date handling with option for manual date entry
- Secure API authentication using token-based headers
- Web-based visualization through Pixela's hosted graphs

### How to Use

1. Run the script using `python main.py` in the `Day37` directory.
2. Choose whether to use today's date or specify a different date.
3. Enter the number of hours you've coded for the selected date.
4. The application will create or update the data point on your habit graph.
5. View your progress visually by visiting your Pixela graph URL.
6. Uncomment different sections of the code to create a new user, graph, or delete entries.

### Prerequisites

- Python 3.8 or higher
- Requests library (`pip install requests`)
- Internet connection to access the Pixela API
- A Pixela account (or create one using the script)

### Link to Code

[View Code →](Day37/main.py)

---

<a name="day-38-workout-tracker"></a>

## Day 38: Workout Tracker 🏋️‍♂️

- **Description**: An automated workout tracker that logs exercise stats from natural language input and saves them to Google Sheets using Nutritionix and Sheety APIs.
- **What I Learned**:
  - **API Integration** – Making authenticated POST requests to Nutritionix and Sheety
  - **Natural Language Processing** – Using plain text to extract exercise data
  - **Environment Variables** – Securing API keys and endpoints
  - **Datetime Handling** – Formatting and logging timestamps
  - **Google Sheets Automation** – Using Sheety to update spreadsheets programmatically

### Features

- Accepts natural language exercise descriptions (e.g., "Ran 3km and cycled 20 minutes")
- Fetches exercise stats (duration, calories, etc.) from Nutritionix
- Logs each exercise with date and time to a Google Sheet via Sheety
- Secures sensitive data using environment variables
- Supports both Basic and Bearer authentication for Sheety

### How to Use

1. Set up environment variables for all API keys, endpoints, and authentication tokens.
2. Run the script using `python main.py` in the `Day38` directory.
3. Enter your exercise details in plain English when prompted.
4. Check your Google Sheet for the new workout entries.

### Prerequisites

- Python 3.8 or higher
- Requests library (`pip install requests`)
- Nutritionix and Sheety accounts
- Google Sheet set up with Sheety

### Link to Code

[View Code →](Day38/main.py)

---

<a name="day-39-flight-deals-project"></a>

## Day 39: Flight Deals Project ✈️

- **Description**: Automates searching for the cheapest flights from a specified origin to multiple destinations and notifies you via SMS or WhatsApp when a lower price is found. Uses the Amadeus API for flight data, Google Sheets (via Sheety API) for storing destination and price data, and Twilio for notifications.
- **What I Learned**:
  - **API Chaining** – Integrating multiple APIs (Amadeus, Sheety, Twilio) in a workflow
  - **Flight Data Parsing** – Extracting and comparing flight offers for best deals
  - **Automated Notifications** – Sending SMS/WhatsApp alerts for price drops
  - **Google Sheets Automation** – Updating and reading data programmatically
  - **Error Handling & Rate Limiting** – Managing API rate limits and fallback logic

### Features

- Automatically fetches and updates IATA codes for destinations
- Searches for the cheapest round-trip flights within a 6-month window
- Notifies you via SMS or WhatsApp if a cheaper flight is found
- Updates the lowest price in your Google Sheet

### How to Use

1. Set up environment variables for Sheety, Amadeus, and Twilio credentials in a `.env` file.
2. Prepare your Google Sheet with columns: `city`, `iataCode`, `lowestPrice`, and `id`.
3. Run the script using `python main.py` in the `Day39` directory.
4. The script will update IATA codes, search for flights, and send notifications if cheaper flights are found.

### Prerequisites

- Python 3.8 or higher
- Requests, python-dotenv, and Twilio libraries (`pip install requests python-dotenv twilio`)
- Accounts for Amadeus, Twilio, and Sheety (Google Sheets API)

### Link to Code

[View Code →](Day39/main.py)

---

<!-- Content for additional days will be added as projects are completed -->
