import random
import os
import time
from hangman_words import wordlist as word_list
from hangman_art import stages as hangman_stages, logo
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    print(logo)

def play_game():
    clear_screen()
    display_logo()
    print("=" * 50)
    print("WELCOME TO HANGMAN!")
    print("=" * 50)
    print("Try to guess the word one letter at a time.")
    print("*****You have 6 lives. Good luck!*****\n")

    life = 6
    chosen_word = random.choice(word_list)
    
    display = "_" * len(chosen_word)
    
    game_over = False
    correct_letters = []
    guessed_letters = []
    
    while not game_over:
        # Clear and redraw screen for better experience
        clear_screen()
        display_logo()
        
        # Game status section
        print(f"\n{'='*20} GAME STATUS {'='*20}")
        print(f"Word: {' '.join(display)}")  # Add spaces between letters for readability
        print(f"Lives: {'❤️ ' * life}{'🖤 ' * (6-life)}")  # Visual heart display for lives
        print(f"Hangman:\n{hangman_stages[life]}")
        
        if guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")  # Sort for easier scanning
        
        # User input section
        print(f"\n{'='*20} YOUR TURN {'='*20}")
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("❌ Please enter just one letter.")
            elif not guess.isalpha():
                print("❌ Please enter a letter from A-Z.")
            elif guess in guessed_letters:
                print(f"❌ You already guessed '{guess}'. Try another letter.")
            else:
                break
        
        guessed_letters.append(guess)
        
        # Update display
        new_display = ""
        for letter in chosen_word:
            if letter == guess or letter in correct_letters:
                new_display += letter
            else:
                new_display += "_"
        
        # Feedback section
        if guess in chosen_word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            if guess not in correct_letters:
                correct_letters.append(guess)
        else:
            life -= 1
            print(f"❌ Sorry! '{guess}' is not in the word.")
            # Add suspense
            time.sleep(1)
            
        display = new_display
        
        # Check win/lose conditions
        if "_" not in display:
            game_over = True
            clear_screen()
            display_logo()
            print(f"\nWord: {chosen_word}")
            print(hangman_stages[life])
            print("\n🎉 CONGRATULATIONS! YOU WIN! 🏆")
        
        if life == 0:
            game_over = True
            clear_screen()
            display_logo()
            print(f"\nWord: {chosen_word}")
            print(hangman_stages[0])
            print("\n💀 GAME OVER! YOU LOST! 💀")

    # Play again prompt
    print("\n" + "="*50)
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ['y', 'n']:
            break
        print("Please enter 'y' or 'n'")
    
    if play_again == 'y':
        play_game()
        # Prevent creation of __pycache__ folders
        sys.dont_write_bytecode = True
if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        clear_screen()
        print("\nThanks for playing Hangman! Goodbye!")