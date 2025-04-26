# The Hiher/Lower Game. This is a game where you compare the number of followers of two different Indian celebrities.
# The game is played in a loop until the user makes a wrong guess.
# The user is prompted to guess which celebrity has more followers, and the game keeps track of the score.
# The game ends when the user makes a wrong guess, and the final score is displayed.

import random
from higher_lower_art import logo, vs
from data import indian_celebrities


def display_comparison(option_a, option_b):
    """Display the comparison between two options with nice formatting."""
    # Assuming the key format is "Name, Description"
    name_a, desc_a = option_a.split(",", 1)
    name_b, desc_b = option_b.split(",", 1)
    print(f"Compare A: {name_a.strip()}, {desc_a.strip()}")
    print(vs)
    print(f"Compare B: {name_b.strip()}, {desc_b.strip()}")


def clear_screen():
    """Clear the console screen for better visibility."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    print(logo)
    score = 0
    game_over = False
    current_celebrity = random.choice(list(indian_celebrities.keys()))

    while not game_over:
        next_celebrity = current_celebrity
        while next_celebrity == current_celebrity:
            next_celebrity = random.choice(list(indian_celebrities.keys()))

        display_comparison(current_celebrity, next_celebrity)

        current_followers = indian_celebrities[current_celebrity]
        next_followers = indian_celebrities[next_celebrity]

        while True:
            user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if user_guess in ['a', 'b']:
                break
            print("Invalid input. Please type 'A' or 'B'.")

        # Check if user is correct
        correct_answer = 'a' if current_followers > next_followers else 'b'
        is_correct = user_guess == correct_answer

        clear_screen()
        print(logo)

        if is_correct:
            score += 1
            print(f"✓ Correct!")
            print(f"{current_celebrity.split(',')[0]}: {current_followers}M followers")
            print(f"{next_celebrity.split(',')[0]}: {next_followers}M followers")
            print(f"Current score: {score}")

            # The one with more followers becomes the next Option A
            if current_followers > next_followers:
                current_celebrity = current_celebrity
            else:
                current_celebrity = next_celebrity
        else:
            print(f"✗ Sorry, that's wrong!")
            print(f"{current_celebrity.split(',')[0]}: {current_followers}M followers")
            print(f"{next_celebrity.split(',')[0]}: {next_followers}M followers")
            print(f"Final score: {score}")
            game_over = True

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    play_game()