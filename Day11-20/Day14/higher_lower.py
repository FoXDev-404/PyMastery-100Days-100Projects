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
        # Select next celebrity (ensuring it's different from current)
        next_celebrity = current_celebrity
        while next_celebrity == current_celebrity:
            next_celebrity = random.choice(list(indian_celebrities.keys()))

        # Display comparison
        display_comparison(current_celebrity, next_celebrity)

        # Get followers
        current_followers = indian_celebrities[current_celebrity]
        next_followers = indian_celebrities[next_celebrity]

        # Debug info (comment out for production)
        # print(f"DEBUG - A: {current_followers}M, B: {next_followers}M")

        # Get user's guess
        while True:
            user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if user_guess in ['a', 'b']:
                break
            print("Invalid input. Please type 'A' or 'B'.")

        # Check if user is correct
        is_correct = (user_guess == 'a' and current_followers > next_followers) or (
                    user_guess == 'b' and next_followers > current_followers)

        clear_screen()
        print(logo)

        # Display results
        if is_correct:
            score += 1
            print(f"✓ Correct! {current_celebrity.split(',')[0]} has {current_followers}M followers.")
            print(f"✓ {next_celebrity.split(',')[0]} has {next_followers}M followers.")
            print(f"Current score: {score}")
            # Winner becomes the new current celebrity for comparison
            current_celebrity = next_celebrity
        else:
            print(f"✗ Sorry, that's wrong!")
            print(f"{current_celebrity.split(',')[0]} has {current_followers}M followers.")
            print(f"{next_celebrity.split(',')[0]} has {next_followers}M followers.")
            print(f"Final score: {score}")
            game_over = True

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    play_game()