<a name="day-11-20"></a>

# Days 11–20: Intermediate Python

<details>
<summary>📋 Quick Navigation</summary>

- [Day 11: Blackjack Game](#day-11)
- [Day 12: Number Guessing Game](#day-12)

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
