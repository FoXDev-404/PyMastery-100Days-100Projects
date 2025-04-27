<a name="day-11-20"></a>

# Days 11–20: Intermediate Python

<details>
<summary>📋 Quick Navigation</summary>

- [Day 11: Blackjack Game](#day-11)
- [Day 12: Number Guessing Game](#day-12)
- [Day 13: Debugging Exercises](#day-13)
- [Day 14: Higher/Lower Game](#day-14)
- [Day 15: Coffee Machine](#day-15)

</details>

## 📅 Day 11–20 Projects [🚧 In Progress]

---

<a id="day-11"></a>

### Day 11: **Blackjack Game** 🎮

- **Description**: A text-based implementation of the classic Blackjack card game (also known as 21).
- **What I Learned**:
  - **Functions with Outputs** – Creating functions that return values
  - **Game Logic** – Implementing complex game rules
  - **Random Module** – Generating random cards
  - **Conditional Logic** – Determining win/loss conditions
- **Link to Code**: [Project Code](./Day11/projectDay11.py)

### Features

- Automatic adjustment of Ace values (11 → 1) when needed
- Dealer follows casino rules (must draw until 17)
- Clean interface with screen clearing between games
- Special handling for Blackjack (natural 21)
- Colorful emojis to indicate game results

### How to Play

- Run the script using `python projectDay11.py`
- Follow the prompts to hit (get another card) or stand
- Aim for a score of 21 without going over
- The dealer will draw cards until reaching at least 17
- Win by having a higher score than the dealer without busting

### Rules Summary

- Cards 2-10 are worth their face value
- Jack, Queen, and King are worth 10 points each
- Ace is worth 11 points unless that would cause a bust, then it's worth 1 point
- Blackjack (Ace + 10-value card) automatically wins unless dealer also has blackjack

---

<a id="day-12"></a>

### Day 12: **Number Guessing Game** 🔢

- **Description**: A fun number guessing game where the computer picks a random number and the player tries to guess it.
- **What I Learned**:
  - **Scope** – Understanding local and global scope in Python
  - **Constants** – Using constants to improve code readability
  - **Difficulty Levels** – Implementing different game difficulties
  - **User Feedback** – Providing helpful hints to users
- **Link to Code**: [Project Code](./Day12/projectDay12.py)

### Features

- Two difficulty levels (easy and hard)
- Limited number of attempts based on difficulty
- Helpful feedback (too high/too low) after each guess
- Keeps track of remaining attempts
- Clean interface with clear instructions

### How to Play

- Run the script using `python projectDay12.py`
- Choose a difficulty level (easy or hard)
- Guess the number between 1 and 100
- Receive feedback after each guess
- Try to find the correct number before running out of attempts

---

<a id="day-13"></a>

### Day 13: **Debugging Exercises** 🐛

- **Description**: A collection of exercises focused on finding and fixing bugs in Python code.
- **What I Learned**:
  - **Debugging Techniques** – Identifying and resolving common coding errors
  - **Print Debugging** – Using strategic print statements to track code execution
  - **Error Types** – Understanding syntax, logical, and runtime errors
  - **Problem-Solving** – Developing a methodical approach to troubleshooting
- **Link to Code**: [Project Code](./Day13/projectDay13.py)

### Features

- Multiple debugging challenges of increasing difficulty
- Examples of common Python programming errors
- Solutions with detailed explanations
- Techniques for identifying and fixing different bug types
- Documentation of debugging best practices

### Debugging Skills Covered

- Describe the problem before trying to solve it
- Reproduce the bug consistently to understand it
- Play computer: trace the code execution manually
- Fix errors one by one and test after each fix
- Use print statements strategically to track variable values
- Take breaks when stuck to gain fresh perspective

---

<a id="day-14"></a>

### Day 14: **Higher/Lower Game** 📊

- **Description**: A fun guessing game where players compare the follower counts of Indian celebrities and decide who has more followers.
- **What I Learned**:
  - **Dictionary Data Handling** – Working with complex data structures
  - **Game State Management** – Managing game progression and score tracking
  - **UI/UX Design** – Creating a clean and engaging text-based interface
  - **Random Selection** – Implementing non-repeating random selection
- **Link to Code**: [Project Code](./Day14/higher_lower.py)

### Features

- Database of Indian celebrities with descriptions and follower counts
- Dynamic comparison between two randomly selected celebrities
- Score tracking system that increases with each correct guess
- Clean interface with screen clearing between rounds
- Visual separation between game elements using ASCII art
- Non-repeating selection to ensure varied comparisons

### How to Play

- Run the script using `python higher_lower.py`
- Compare the two displayed celebrities (A and B)
- Guess which one has more Instagram followers by typing 'A' or 'B'
- Each correct guess earns one point and continues the game
- The game ends when you make an incorrect guess
- Try to achieve the highest score possible!

---

<a id="day-15"></a>

### Day 15: **Coffee Machine** ☕

- **Description**: A virtual coffee machine simulation that manages resources, processes coins, and serves different types of coffee.
- **What I Learned**:
  - **Resource Management** – Tracking and updating available ingredients
  - **Financial Transactions** – Handling money inputs and calculating change
  - **User Interaction** – Creating an interactive command-line interface
  - **Program Structure** – Organizing code into modular functions
- **Link to Code**: [Project Code](./Day15/coffee_machine.py)

### Features

- Multiple coffee options (espresso, latte, cappuccino) with different prices and resource requirements
- Resource tracking for water, milk, and coffee beans
- Coin processing system accepting different coin denominations
- Maintenance mode to check current resource levels
- Change calculation and return system
- Error handling for insufficient resources or funds

### How to Play

- Run the script using `python coffee_machine.py`
- Choose from menu options: "espresso", "latte", "cappuccino", "report", or "off"
- Insert coins when prompted (quarters, dimes, nickels, pennies)
- Receive your virtual coffee if resources are sufficient and payment is adequate
- Get change back if you inserted more than required
- Type "report" to view current resource levels
- Type "off" to exit the program

### Resource Management

- Each coffee type requires specific amounts of water, milk, and coffee
- The machine checks if enough resources are available before making coffee
- Resources are deducted automatically when a drink is successfully made
- Money collected from sales is tracked and can be viewed in the report
