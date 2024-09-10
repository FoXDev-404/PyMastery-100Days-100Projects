# Project: Rock, Paper, Scissors Game
# Description: A simple Rock, Paper, Scissors game where the user plays against the computer.

import random

# Rock ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper ASCII Art
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Scissors ASCII Art
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Rules to win the game
# Rock wins against Scissors
# Scissors wins against Paper
# Paper wins against Rock
# If both players choose the same shape, it's a draw

choices = [rock, paper, scissors]

# User choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_choice == 0:
    print(f"You chose:\n{choices[0]}")
elif user_choice == 1:
    print(f"You chose:\n{choices[1]}")
elif user_choice == 2:
    print(f"You chose:\n{choices[2]}")
else:
    print("Invalid choice, you lose!")
    exit()

# Computer choice
computer_choice = random.randint(0, 2)  # Generate a random index between 0 and 2
print(f"Computer chose:\n{choices[computer_choice]}")

# Game logic
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
else:
    print("It's a draw!")
