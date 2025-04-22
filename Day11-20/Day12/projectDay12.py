# Number Guessing Game
 
import random


def number_guessing_game():
    actual_num = random.randint(1, 100)

    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    level = input("Choose the Difficulty. Type 'easy', 'medium' or 'hard': ").lower()

    if level == "easy":
        life = 10
    elif level == "medium":
        life = 7
    elif level == "hard":
        life = 5
    else:
        print("Invalid difficulty. Defaulting to 'easy'.")
        life = 10

    while life > 0:
        print(f"\nYou have {life} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if guess < actual_num:
            print("Too low.")
        elif guess > actual_num:
            print("Too high.")
        else:
            print(f"🎉 Correct! You guessed the number {actual_num}!")
            break

        life -= 1

        if life == 0:
            print("💀 Game Over!")
            print(f"The correct number was {actual_num}.")
        else:
            print("Guess again.")


def play():
    while True:
        number_guessing_game()
        play_again = input("\nDo you want to play again? Type 'yes' or 'no': ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye 👋")
            break


play()
