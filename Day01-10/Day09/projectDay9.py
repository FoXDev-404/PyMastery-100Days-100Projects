import os
from art import logo

def clear_screen():
    # Cross-platform screen clear
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bidder_info():
    name = input("Enter your name: ")
    while True:
        try:
            bid = int(input("Enter your bid amount: $"))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    return name, bid

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    return winner, highest_bid

def secret_auction():
    print(logo)
    print("Welcome to the Secret Auction Program!")
    bids = {}
    while True:
        name, bid = get_bidder_info()
        bids[name] = bid

        more = input("Is there anyone else who wants to bid? Type 'yes' or 'no': ").strip().lower()
        if more == 'no':
            break
        clear_screen()

    clear_screen()
    winner, amount = find_highest_bidder(bids)
    print(f"🏆 The winner is '{winner}' with a bid of ${amount}!")

secret_auction()

