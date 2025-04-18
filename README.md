# PyMastery-100Days-100Projects

Welcome to **PyMastery-100Days-100Projects**! I'm on a mission to master Python by taking on an exciting 100-day coding challenge. Over the next 100 days, I'll be building 100 unique projects, diving into areas like data science, web development, automation, game development, and app creation. Each day is a fresh chance to sharpen my coding skills, tackle real-world problems, and become a Python pro. Come along and join me on this amazing journey of learning and growth!

---

## Table of Contents

- [Day 1-10](#day-1-10)
- [Resources](#resources)
- [License](#license)

---

<a name="day-1-10"></a>

<details>
<summary>Day 1-10</summary>

### Day 1: Band Name Generator

- **Description**: Built a Python script that combines user inputs to generate a band name.
- **What I Learned**:
  - **Printing to the Console**: Using `print()` to display output.
  - **String Manipulation**: Handling and modifying strings.
  - **Input Function**: Using `input()` to get user input.
  - **Variables**: Declaring and using variables.
  - **Variable Naming**: Rules for naming variables.
  - **Debugging**: Finding and fixing errors.
- **Link to Code**: [Project Code](Day01-10/Day01/projectDay1.py)

### Day 2: Tip Calculator

- **Description**: Built a Python script that calculates the tip amount based on the bill total and desired tip percentage.
- **What I Learned**:
  - **Python Primitive Data Types**: Understanding different data types in Python.
  - **Type Error, Type Checking and Type Conversion**: Handling type errors, checking types, and converting between types.
  - **Mathematical Operations in Python**: Performing basic mathematical operations.
  - **Number Manipulation and F-Strings**: Manipulating numbers and using f-strings for formatted output.
- **Link to Code**: [Project Code](Day01-10/Day02/projectDay2.py)

### Day 3: Haunted Mansion Escape

- **Description**: Developed a text-based adventure game where the player navigates through a haunted mansion, making choices that influence the outcome. This project focuses on applying control flow, user input, and string manipulation skills learned during the course.

- **What I Learned**:

  - **Control Flow with `if / else` and Conditional Operators**: Implemented decision-making in the game using conditional statements.
  - **Introducing the Modulo Operator**: Applied modulo operations in the game’s logic.
  - **Nested `if` Statements and `elif` Statements**: Used nested conditionals to handle complex game scenarios.
  - **Multiple `If` Statements in Succession**: Managed sequential conditions to create branching paths in the game.
  - **Logical Operators**: Utilized logical operators to combine multiple conditions for more dynamic game responses.
  - **String Literals for ASCII Art**: Employed multi-line string literals to include ASCII art in the game’s narrative.

- **Link to Code**: [Project Code](Day01-10/Day03/projectDay3.py)

### Day 4: Rock Paper Scissors

- **Description**: Built a Rock Paper Scissors game using Python, incorporating user inputs and random choices.
- **What I Learned**:
  - **Random Module**: Using random functions to generate choices.
  - **Lists**: Appending items and handling nested lists.
  - **Index Errors**: Managing errors when accessing list elements.
- **Link to Code**: [Project Code](Day01-10/Day04/projectDay4.py)

### Day 5: Password Generator  

- **Description**: Built a Python script that generates strong, random passwords based on user-defined criteria such as length and character types. This project emphasized the use of loops, list manipulation, and randomization techniques.  

- **What I Learned**:  
  - **For Loops with Python Lists**: Practiced iterating through lists to process data efficiently.  
  - **Finding the Highest Score**: Learned to identify the maximum value in a list without using the `max()` function by implementing custom logic.  
  - **The `range()` Function**: Used `range()` for controlled iteration in loops.  
  - **FizzBuzz Exercise**: Strengthened logical thinking by solving the classic **FizzBuzz** coding challenge.  
  - **The `random` Module**: Employed `random` functions to generate secure passwords with letters, numbers, and symbols.  
  - **String Manipulation and List Operations**: Utilized string joining, list shuffling, and slicing to create strong, dynamic passwords.  

- **Link to Code**: [Project Code](Day01-10/Day05/projectDay5.py)

### Day 6: Maze Solver

- **Description**: Developed a robot maze solver algorithm for Reeborg's World using the "right-hand rule" technique. This program guides a robot through complex mazes by consistently following the right wall until it reaches the goal.

- **What I Learned**:
  - **Functions**: Creating and calling custom functions to modularize code.
  - **While Loops**: Using while loops for condition-based iteration.
  - **Conditional Logic**: Implementing if/elif/else statements for decision-making.
  - **Problem-Solving Algorithms**: Applying the right-hand rule for maze navigation.
  - **Debugging Logic**: Testing and refining algorithmic solutions.
  - **Working with External Environments**: Writing code for the Reeborg's World platform.

- **Key Concepts**:
  - **Wall Following Algorithm**: Understanding how the right-hand rule guarantees finding an exit in simply connected mazes.
  - **Priority-Based Decision Making**: Implementing a clear hierarchy of movement choices.
  - **State Management**: Tracking the robot's position and orientation relative to walls.

- **Link to Code**: [Project Code](Day01-10/Day06/projectDay6.py)

### Day 7: Beginner – Hangman

- **Description**: Built a fully functional Hangman game in Python by breaking down the problem into manageable steps like picking a random word, replacing blanks, checking for win conditions, tracking lives, and improving user experience.

- **What I Learned**:
  - **Flow Charting**: How to break a complex problem into logical steps using flow charts.
  - **Random Module**: Using `random.choice()` to pick a word from a list.
  - **List and String Manipulation**: Replacing blanks with guessed letters and updating the display.
  - **Control Flow**: Implementing conditions to check win/loss scenarios.
  - **Life Tracker**: Using variables to represent and decrement player lives.
  - **User Experience Enhancements**: Improving visuals and interactions (like displaying hangman stages, hearts for lives, and guessed letters).

- **Link to Code**: [Project Code](Day01-10/Day07/projectDay7.py)

### Day 8: Caesar Cipher

- **Description**: Developed a Caesar Cipher encryption/decryption tool where each letter in the plaintext is shifted by a certain number of places down the alphabet. Enhanced the project by organizing it into a single function and implementing a loop that allows the user to run the cipher repeatedly.

- **What I Learned**:
  - **Function Parameters**: How to pass and use multiple parameters in functions.
  - **Positional vs Keyword Arguments**: The difference in calling functions using position-based or named arguments.
  - **Loops and User Interaction**: Implemented a loop to allow repeated encoding/decoding based on user choice.
  - **String and List Operations**: Shifted characters through an alphabet list using indexing and modulo operations.
  - **Code Structuring**: Reorganized code to make it more reusable, clean, and modular.
  - **Handling Non-Alphabet Characters**: Ensured non-alphabet characters (like spaces and punctuation) were preserved during ciphering.

- **Link to Code**: [Project Code](Day01-10/Day08/projectDay8.py)

### Day 9: Secret Auction Program

- **Description**: Developed a Secret Auction program using dictionaries and control flow. The script allows multiple users to input their bids, stores them in a dictionary, and then determines the highest bidder using a manual loop (instead of built-in `max()`).

- **What I Learned**:
  - **Python Dictionaries**: Creating, updating, and retrieving data from dictionaries.
  - **Nesting**: Nesting lists and dictionaries to represent more complex data.
  - **Control Flow with Loops**: Using `while` loops to collect user data until a condition is met.
  - **Dictionary Iteration**: Looping through a dictionary to find the highest bidder.
  - **Function Structuring**: Modularizing code using reusable functions.
  - **Flow Charts**: Visualizing the logic flow before coding to plan out decisions and inputs.
  - **User Interaction**: Handling multiple inputs and clearing the screen to simulate an auction environment.

- **Link to Code**: [Project Code](Day01-10/Day09/projectDay9.py)

...

</details>

## Resources

Here are some resources that I'm using to help me along the way:

- **Books**
  - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- **Online Courses**
  - [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
  - [Python for Everybody](https://www.coursera.org/specializations/python)
- **Documentation**
  - [Python Official Documentation](https://docs.python.org/3/)
  - [Django Documentation](https://docs.djangoproject.com/en/stable/)
- **Communities**
  - [Stack Overflow](https://stackoverflow.com/)
  - [Reddit - r/learnpython](https://www.reddit.com/r/learnpython/)

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
