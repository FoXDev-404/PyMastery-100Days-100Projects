<a name="day-21-30"></a>

# Days 21–30: Intermediate Python

<details>
<summary>📋 Table of Contents</summary>

- [Day 21: Snake Game](#day-21-snake-game)
- [Day 22: Pong Game](#day-22-pong-game)
- [Day 23: Turtle Crossing Game](#day-23-turtle-crossing-game)
- [Day 24: Mail Merge Project](#day-24-mail-merge-project)
- [Day 25: Pandas Data Analysis](#day-25-pandas-data-analysis)
- [Day 26: NATO Alphabet Project](#day-26-nato-alphabet-project)
- [Day 27: Tkinter GUI](#day-27-tkinter-gui)
- [Day 28: Pomodoro Timer](#day-28-pomodoro-timer)
- [Day 29: Password Manager](#day-29-password-manager)

</details>

## 📅 Day 21–30 Projects [🚧 In Progress]

---

<a name="day-21-snake-game"></a>

## Day 21: Snake Game 🐍

- **Description**: A classic Snake game built using Python's Turtle module.
- **What I Learned**:
  - **Object-Oriented Programming (OOP)** – Designing modular and reusable code
  - **Keyboard Event Handling** – Using `onkey()` for responsive controls
  - **Game State Management** – Implementing pause, resume, and level progression
  - **File Handling** – Saving and loading high scores

### Features

- Smooth snake movement with direction controls
- High score tracking with auto-save functionality
- Pause and resume functionality
- Level system with increasing difficulty
- Special food items with higher points

### How to Play

1. Run the script using `python main.py` in the `Day21` directory.
2. Use the arrow keys to control the snake's movement.
3. Avoid colliding with the walls or the snake's own tail.
4. Collect food to grow the snake and increase your score.
5. Try to beat your high score!

### Prerequisites

- Python 3.8 or higher
- Turtle module (pre-installed with Python)

### Link to Code

[View Code →](Day21/main.py)

---

<a name="day-22-pong-game"></a>

## Day 22: Pong Game 🏓

- **Description**: A recreation of the classic Pong arcade game using Python's Turtle module.
- **What I Learned**:
  - **Advanced OOP Concepts** – Implementing multiple classes with inheritance
  - **Game Physics** – Creating realistic ball movement and paddle collisions
  - **Two-player Controls** – Managing simultaneous input for different players
  - **Speed Mechanics** – Progressive difficulty with increasing ball speed

### Features

- Two-player gameplay with separate controls
- Dynamic ball physics with increasing speed after each hit
- Score tracking system with winning condition
- Boundary detection for paddles and ball
- Visual elements like center court line

### How to Play

1. Run the script using `python main.py` in the `Day22` directory.
2. Player 1 (left): Use 'W' and 'S' keys to move paddle up and down.
3. Player 2 (right): Use 'Up' and 'Down' arrow keys to control paddle.
4. The ball speeds up each time it hits a paddle.
5. First player to reach 5 points wins the game!

### Prerequisites

- Python 3.8 or higher
- Turtle module (pre-installed with Python)

### Link to Code

[View Code →](Day22/main.py)

---

<a name="day-23-turtle-crossing-game"></a>

## Day 23: Turtle Crossing Game 🐢

- **Description**: A road crossing game where the player controls a turtle to safely cross a busy road.
- **What I Learned**:
  - **State Management** – Implementing different game states (menu, playing, paused, game over)
  - **Collision Detection** – Detecting collisions between turtle and cars
  - **Dynamic Difficulty** – Increasing game difficulty as levels progress
  - **Lives System** – Managing player lives and reset mechanics
  - **Persistent Data** – Saving and loading high scores between game sessions

### Features

- Intuitive controls for turtle movement (up, left, right)
- Progressive difficulty with faster traffic at higher levels
- Multiple lives system with visual feedback
- High score tracking across game sessions
- Pause functionality during gameplay
- Visual road markings and varied car sizes

### How to Play

1. Run the script using `python main.py` in the `Day23` directory.
2. Press SPACE to start the game from the menu.
3. Use the UP arrow key to move forward.
4. Use LEFT and RIGHT arrow keys to dodge traffic.
5. Press P to pause/resume the game.
6. Reach the other side to advance to the next level.
7. Avoid collisions with cars - you have 3 lives!

### Prerequisites

- Python 3.8 or higher
- Turtle module (pre-installed with Python)

### Link to Code

[View Code →](Day23/main.py)

---

<a name="day-24-mail-merge-project"></a>

## Day 24: Mail Merge Project 📧

- **Description**: An automated mail merge system that generates personalized invitation letters from a template.
- **What I Learned**:
  - **File I/O Operations** – Reading from and writing to files with context managers
  - **String Manipulation** – Replacing placeholder text with actual content
  - **Path Handling** – Working with relative and absolute file paths
  - **Batch Processing** – Automating the creation of multiple documents

### Features

- Reads names from a list of invited guests
- Uses a template letter with placeholder for personalization
- Generates individual invitation letters for each person
- Demonstrates both relative and absolute path handling
- Implements efficient file handling with context managers
- Maintains original formatting while replacing placeholders

### How It Works

1. The program reads a list of names from `./Input/Names/invited_names.txt`
2. It loads a letter template from `./Input/Letters/starting_letter.txt`
3. For each name, it replaces the `[name]` placeholder in the template
4. Individual personalized letters are saved to the output directory
5. Files are properly closed using context managers for best practice

### Prerequisites

- Python 3.8 or higher
- No additional packages required

### Link to Code

[View Code →](Day24/mail_merge_project/main.py)

---

<a name="day-25-pandas-data-analysis"></a>

## Day 25: Pandas Data Analysis 📊

- **Description**: Data analysis project using the Pandas library to analyze squirrel census data from Central Park.
- **What I Learned**:
  - **Pandas Library** – Working with DataFrame objects for data manipulation
  - **CSV Handling** – Reading from and writing to CSV files with Pandas
  - **Data Filtering** – Using conditions to filter data from DataFrames
  - **Data Aggregation** – Counting and summarizing data based on categories
  - **Data Export** – Converting processed data back to CSV format

### Features

- Reads and processes large CSV datasets
- Filters data based on specific conditions
- Performs count operations on categorical data
- Creates new DataFrames from analysis results
- Exports processed data to CSV files
- Demonstrates pandas syntax for data selection and manipulation

### How It Works

1. The program reads squirrel census data from a CSV file
2. It counts squirrels by their primary fur color (Gray, Cinnamon, Black)
3. The counts are stored in a new DataFrame with appropriate column names
4. The summarized data is exported to a new CSV file for easy viewing
5. Shows multiple ways to access, filter, and analyze data with pandas

### Prerequisites

- Python 3.8 or higher
- Pandas library (`pip install pandas`)

### Link to Code

[View Code →](Day25/main.py)

---

<a name="day-26-nato-alphabet-project"></a>

## Day 26: NATO Alphabet Project 🔤

- **Description**: A program that converts words into their NATO phonetic alphabet equivalents using Python and pandas.
- **What I Learned**:
  - **Dictionary Comprehensions** – Creating dictionaries efficiently from DataFrames
  - **User Input Validation** – Handling invalid input gracefully
  - **Data Mapping** – Mapping user input to corresponding phonetic code words
  - **Error Handling** – Using try/except for robust user experience

### Features

- Converts any word into a list of NATO phonetic code words
- Handles both uppercase and lowercase input
- Provides clear error messages for invalid characters
- Reads the NATO alphabet from a CSV file using pandas

### How It Works

1. The program loads a CSV file containing the NATO alphabet.
2. It creates a dictionary mapping each letter to its code word.
3. The user enters a word; the program outputs the phonetic code words.
4. If the input contains non-alphabetic characters, the user is prompted again.

### Prerequisites

- Python 3.8 or higher
- Pandas library (`pip install pandas`)
- `nato_phonetic_alphabet.csv` file in the project directory

### Link to Code

[View Code →](Day26/NATO-alphabet/main.py)

---

<a name="day-27-tkinter-gui"></a>

## Day 27: Tkinter GUI 🖥️

- **Description**: An introduction to GUI programming in Python using Tkinter, culminating in a miles-to-kilometers converter application.
- **What I Learned**:
  - **Tkinter Basics** – Creating windows, labels, buttons, and entry fields
  - **Layout Management** – Using grid layout system for precise widget positioning
  - **Event Handling** – Connecting buttons to functions and keyboard events
  - **Input Validation** – Handling user input with error checking
  - **Variable Classes** – Using StringVar, IntVar for dynamic widget content
  - **Advanced Args/Kwargs** – Using \*args and \*\*kwargs for flexible function parameters

### Features of Miles-to-Kilometers Converter

- Convert between miles and kilometers in both directions
- Clean, user-friendly interface with proper spacing and alignment
- Real-time formula display showing the calculation performed
- History tracking of recent conversions
- Input validation with error handling
- Keyboard shortcuts (Enter to convert, Escape to reset)
- Responsive design with proper padding and margins

### How It Works

1. Select the direction of conversion (miles to km or km to miles)
2. Enter a numeric value in the input field
3. Press "Calculate" button or hit Enter to perform the conversion
4. View the result and the formula used for calculation
5. Previous conversions are stored in the history box
6. Press "Reset" button or hit Escape to clear the input

### Prerequisites

- Python 3.8 or higher
- Tkinter (included with standard Python installation)

### Link to Code

[View Code →](Day27/mile_to_kilo_converter.py)

---

<a name="day-28-pomodoro-timer"></a>

## Day 28: Pomodoro Timer ⏱️

- **Description**: A productivity timer application based on the Pomodoro Technique, built with Tkinter.
- **What I Learned**:
  - **Tkinter Canvas Widget** – Creating complex UI elements with canvas
  - **Timer Mechanisms** – Implementing countdown timers with `after()` method
  - **State Management** – Tracking timer states and session types
  - **Dynamic UI Updates** – Changing UI elements based on timer states
  - **Math Module** – Using mathematical functions for time calculations

### Features

- Alternating work and break sessions following the Pomodoro technique
- Visual indication of current session type with color coding
- Automatic transitions between work and break periods
- Visual tracking of completed work sessions with checkmarks
- Start and reset functionality with proper state management
- Clean, minimalist UI with a tomato timer visual

### How to Use

1. Run the script using `python main.py` in the `Day28` directory
2. Click "Start" to begin a 25-minute work session
3. After each work session, the timer automatically switches to a break
4. Short 5-minute breaks follow regular work sessions
5. Every fourth work session is followed by a longer 20-minute break
6. Completed work sessions are tracked with checkmarks
7. Click "Reset" at any time to clear the timer and start over

### Prerequisites

- Python 3.8 or higher
- Tkinter (included with standard Python installation)
- "tomato.png" image file in the project directory

### Link to Code

[View Code →](Day28/main.py)

---

<a name="day-29-password-manager"></a>

## Day 29: Password Manager 🔐

- **Description**: A secure password manager application built with Tkinter that helps generate, store, and retrieve website login credentials.
- **What I Learned**:
  - **Secure Password Generation** - Creating strong random passwords with Python
  - **Formatted Text File Storage** - Reading from and writing to beautifully formatted JSON files
  - **Tkinter UI Design** - Building an attractive user interface with custom color palette
  - **Clipboard Integration** - Copying generated passwords to the clipboard
  - **Data Structure Design** - Organizing and storing credentials efficiently
  - **Error Handling** - Implementing robust error handling for file operations

### Features

- Generate strong random passwords with letters, numbers, and symbols
- Store website credentials (website, email, password) in a beautifully formatted JSON file
- Search for saved credentials by website name
- Elegant UI with a soft pastel color palette (Mauve, Pink, Peach, and Light background)
- High contrast text for better readability
- Automatic copying of generated passwords to clipboard
- Input validation to prevent saving incomplete credentials
- Confirmation dialog before saving new credentials
- Error handling for file operations and data retrieval

### How to Use

1. Run the script using `python main.py` in the `Day29` directory
2. Enter the website name in the "Website" field
3. Enter or use the pre-filled email in the "Email/Username" field
4. Either enter a password manually or click "Generate Password"
5. Click "Add" to save the credentials
6. To retrieve credentials, enter a website name and click "Search"
7. Generated passwords are automatically copied to your clipboard
  
### Prerequisites

- Python 3.8 or higher
- Tkinter (included with standard Python installation)
- "logo.png" image file in the project directory

### Link to Code

[View Code →](Day29/main.py)

---

<!-- Additional sections for Day 30 can follow this structure -->
