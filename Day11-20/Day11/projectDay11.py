# Blackjack Project
# This is a simple implementation of the Blackjack card game.

import random
import os
from art import logo

def deal_card():
    """
    Returns a random card from the deck.
    Deck consists of numbers 2-10, four 10s (for J, Q, K), and 11 (Ace).
    """
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    """
    Takes a list of cards and returns the total score.
    
    Returns:
        0 if the hand is a blackjack (sum is 21 with 2 cards).
        Adjusts Ace (11) to 1 if score goes over 21.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """
    Compares user and computer scores and returns the result.
    
    Returns:
        A string indicating whether the user won, lost, or drew the game.
    """
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose 😱 Opponent has Blackjack!"
    elif user_score == 0:
        return "Win 😎 with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😄"
    else:
        return "You lose 😤"

def play_game():
    """
    Manages the flow of a single game of Blackjack.
    Deals cards, handles player input, and evaluates game outcome.
    """
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game loop
while input("\nDo you want to play a game of Blackjack? (y/n): ").lower() == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()
