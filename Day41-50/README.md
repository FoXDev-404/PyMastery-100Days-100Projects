<a name="day-41-50"></a>

# Days 41–50: Web Foundation - Intermediate

<details>
<summary>📋 Table of Contents</summary>

- [Days 41–50: Web Foundation - Intermediate](#days-4150-web-foundation---intermediate)
  - [📅 Day 41–50 Projects \[5/10 Completed\]](#-day-4150-projects-510-completed)
  - [Day 41: HTML Anime Ranking Project 🌸](#day-41-html-anime-ranking-project-)
    - [How to Use](#how-to-use)
    - [Prerequisites](#prerequisites)
    - [Link to Code](#link-to-code)
  - [Day 42: HTML Birthday Invite Project 🎂](#day-42-html-birthday-invite-project-)
    - [Link to Code](#link-to-code-1)
  - [Day 43: CSS Selectors \& Color Vocabulary 🎨](#day-43-css-selectors--color-vocabulary-)
    - [Link to Code](#link-to-code-2)
  - [Day 44: HTML Movie Ranking Project 🎬](#day-44-html-movie-ranking-project-)
    - [How to Use](#how-to-use-1)
    - [Prerequisites](#prerequisites-1)
    - [Link to Code](#link-to-code-3)
  - [Day 45: 100 Movies to Watch Web Scraper 🎥](#day-45-100-movies-to-watch-web-scraper-)
    - [Link to Code](#link-to-code-4)
  - [Day 46: Spotify Playlist from Billboard Hot 100 Scraper 🎵](#day-46-spotify-playlist-from-billboard-hot-100-scraper-)
    - [Link to Code](#link-to-code-5)

</details>

---

## 📅 Day 41–50 Projects [5/10 Completed]

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


