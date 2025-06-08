<a name="day-31-40"></a>

# Days 31–40: Advanced Python Projects

<details>
<summary>📋 Table of Contents</summary>

- [Day 31: Flash Card App](#day-31-flash-card-app)
- [Day 32: Birthday Wisher](#day-32-birthday-wisher)
- [Day 33: ISS Tracker](#day-33-iss-tracker)
  <!-- Add more days as they are completed -->
  </details>

## 📅 Day 31–40 Projects [3/10 Completed]

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

<!-- Content for additional days will be added as projects are completed -->
