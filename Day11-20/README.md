<a name="day-11-20"></a>

# Days 11–20: Intermediate Python

<details>
<summary>📋 Table of Contents</summary>

- [Day 11: Blackjack Game](#day-11)
- [Day 12: Number Guessing Game](#day-12)
- [Day 13: Debugging Exercises](#day-13)
- [Day 14: Higher/Lower Game](#day-14)
- [Day 15: Coffee Machine](#day-15)
- [Day 16: Coffee Machine Using OOP](#day-16)
- [Day 17: Quiz Game](#day-17)
- [Day 18: Hirst Painting Project](#day-18)
- [Day 19: Turtle Race](#day-19)
- [Day 20: Snake Game](#day-20)

</details>

## 📅 Day 11–20 Projects [10/10 Completed]

---

<a id="day-11"></a>

### Day 11: **Blackjack Game** 🎮

- **Description**: A text-based implementation of the classic Blackjack card game (also known as 21).
- **Key Learnings**:
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
- **Key Learnings**:
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
- **Key Learnings**:
  - **Debugging Techniques** – Identifying and resolving common coding errors
  - **Print Debugging** – Using strategic print statements to track code execution
  - **Error Types** – Understanding syntax, logical, and runtime errors
  - **Problem-Solving** – Developing a methodical approach to troubleshooting
- **Link to Code**: [Code](./Day13/)

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
- **Key Learnings**:
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
- **Key Learnings**:
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

---

<a id="day-16"></a>

### Day 16: **Coffee Machine Using OOP** ☕

- **Description**: An enhanced coffee machine simulation using Object-Oriented Programming principles, adapted for Indian currency and coin denominations.
- **Key Learnings**:
  - **OOP Concepts** – Implementing classes and objects for modular code
  - **Class Collaboration** – Interaction between Menu, CoffeeMaker, and MoneyMachine classes
  - **Custom Currency Handling** – Accepting Indian coins (₹1, ₹2, ₹5, ₹10, ₹20)
  - **Code Reusability** – Extending and modifying existing code for new requirements
- **Link to Code**: [Project Code](./Day16/Coffee_Machine_Using_OOP/main.py)

### Features

- Multiple coffee options (espresso, latte, cappuccino) with Indian prices
- Accepts Indian coins: ₹1, ₹2, ₹5, ₹10, ₹20
- Resource tracking for water, milk, and coffee beans
- Maintenance mode to check current resource levels
- Change calculation and return system in ₹
- Error handling for insufficient resources or funds
- Clean, modular code using OOP principles

### How to Play

- Run the script using `python main.py` inside the `Day16/Coffee_Machine_Using_OOP` directory
- Choose from menu options: "espresso", "latte", "cappuccino", "report", or "off"
- Insert coins when prompted (₹1, ₹2, ₹5, ₹10, ₹20)
- Receive your virtual coffee if resources are sufficient and payment is adequate
- Get change back if you inserted more than required
- Type "report" to view current resource levels
- Type "off" to exit the program

### Resource Management

- Each coffee type requires specific amounts of water, milk, and coffee
- The machine checks if enough resources are available before making coffee
- Resources are deducted automatically when a drink is successfully made
- Money collected from sales is tracked and can be viewed in the report

---

<a id="day-17"></a>

### Day 17: **Quiz Game** 🧠

- **Description**: An interactive quiz application that tests users' knowledge with True/False questions while keeping score.
- **Key Learnings**:
  - **OOP Implementation** – Creating classes for Question and QuizBrain
  - **Encapsulation** – Separating concerns between data storage and logic
  - **Attribute Management** – Tracking question number, score, and progress
  - **Class Methods** – Implementing functionality like checking answers and progressing through questions
- **Link to Code**: [Project Code](./Day17/Quiz_Game/)

### Features

- True/False question format with automatic scoring
- Progress tracking showing current question number
- Immediate feedback on answer correctness
- Final score display upon completion
- Modular design using Object-Oriented Programming
- Extendable question bank that can be easily modified

### How to Play

- Run the script using `python main.py` in the `Day17/Quiz_Game` directory
- Read each question carefully and type "True" or "False"
- Get immediate feedback on whether your answer was correct
- See your running score after each question
- Complete all questions to view your final score

---

<a id="day-18"></a>

### Day 18: **Hirst Painting Project** 🎨

- **Description**: A Python program that recreates Damien Hirst's famous spot paintings using the Turtle graphics module.
- **Key Learnings**:
  - **Turtle Graphics** – Using Python's built-in drawing module for visual outputs
  - **RGB Color System** – Working with RGB tuples to generate colorful patterns
  - **Algorithmic Drawing** – Creating structured patterns with nested loops
  - **Color Extraction** – Using the colorgram package to extract colors from images
- **Link to Code**: [Project Code](./Day18/Penting_Project/project.py)

### Features

- Creates a 10×10 grid of colored dots resembling Hirst's spot paintings
- Uses a palette of extracted colors from real artwork
- Implements optimized drawing with hidden turtle and maximum speed
- Precise dot positioning with mathematical calculations
- Randomly selects colors for each dot to create visual interest
- Clean, well-structured code with clear comments

### How It Works

- The program positions the turtle at the starting point (bottom left corner)
- It methodically draws dots in a grid pattern, moving right across each row
- After completing a row, the turtle moves up to begin the next row
- Each dot is assigned a random color from the extracted palette
- The drawing continues until the entire 10×10 grid is filled
- The result is a colorful dot pattern similar to Hirst's famous artwork

### Technical Implementation

- Sets up turtle with penup() to avoid drawing lines between dots
- Uses dot() method for consistent circle shapes
- Leverages turtle.colormode(255) to enable RGB color tuples
- Implements efficient path planning to minimize unnecessary movement
- Creates reusable color extraction functionality for future projects

---

<a id="day-19"></a>

### Day 19: **Turtle Race** 🏁

- **Description**: An interactive turtle racing game using event listeners and higher-order functions in Python.
- **Key Learnings**:
  - **Event Listeners** – Using functions like `listen()` and `onkey()` to detect user input
  - **Higher-Order Functions** – Working with functions that take other functions as parameters
  - **Multiple Objects** – Creating and managing several turtle instances simultaneously
  - **Game States** – Tracking race positions, winners, and betting outcomes
- **Link to Code**: [Project Code](./Day19/turtle_race.py)

### Features

- Colorful racing game with multiple turtles competing simultaneously
- Keyboard-controlled Etch-A-Sketch application for creative drawing
- Betting system that allows users to predict the winner
- Random movement algorithm for unpredictable race outcomes
- Visual finish line and race announcements
- Clean UI with clear color differentiation between racers

### How to Play

- Run the script using `python turtle_race.py` in the `Day19` directory
- Place your bet on which colored turtle you think will win
- Watch as the turtles race across the screen at random speeds
- See whether your chosen turtle wins or loses
- For the Etch-A-Sketch game, use W (forward), S (backward), A (counter-clockwise), D (clockwise), and C (clear)

### Technical Implementation

- Uses `screen.listen()` to enable keyboard event detection
- Implements `screen.onkey(function, key)` to create keyboard controls
- Creates multiple turtle objects with different colors and starting positions
- Uses `random.randint()` to generate varying movement speeds
- Implements win condition detection when a turtle crosses the finish line
- Applies coordinate tracking with `xcor()` and `ycor()` methods
- Demonstrates both procedural and event-driven programming approaches

---

<a id="day-20"></a>

### Day 20: **Snake Game** 🐍

- **Description**: A classic Snake game implementation using Python's Turtle graphics module.
- **Key Learnings**:
  - **OOP Design** – Building a game using object-oriented principles
  - **Coordinate Systems** – Managing positions and movements on a 2D plane
  - **Game Loop** – Creating a continuous game loop for smooth gameplay
  - **Event Handling** – Detecting keyboard input to control the snake
- **Link to Code**: [Project Code](./Day20/main.py)

### Features

- Snake movement in four directions (up, down, left, right)
- Direction control prevention to avoid snake reversing into itself
- Segmented snake body that follows the head
- Smooth movement animation using Turtle graphics
- Clean class-based implementation for maintainability
- Responsive controls with immediate direction changes

### How to Play

- Run the script using `python main.py` in the `Day20` directory
- Control the snake using the arrow keys
- Guide the snake around the screen without hitting the walls or itself
- Try to collect food to grow the snake and increase your score
- The game ends when the snake collides with the wall or its own tail

### Technical Implementation

- Uses object-oriented programming with a dedicated Snake class
- Implements segment-based movement where each body part follows the one ahead
- Uses `setheading()` to control snake direction
- Prevents illegal moves (like reversing) with directional constraints
- Manages snake body as a list of turtle objects with coordinated movement
- Implements efficient movement algorithm to ensure smooth gameplay
