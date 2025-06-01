<a name="day-31-40"></a>

# Days 31–40: Advanced Python Projects

<details>
<summary>📋 Table of Contents</summary>

- [Day 31: Flash Card App](#day-31-flash-card-app)
<!-- Add more days as they are completed -->
</details>

## 📅 Day 31–40 Projects [1/10 Completed]

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

<!-- Content for additional days will be added as projects are completed -->
