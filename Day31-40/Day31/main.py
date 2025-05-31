from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FRONT = "French"
LANGUAGE_BACK = "English"
DATA_FILE = "data/french_words.csv"
WORDS_TO_LEARN_FILE = "data/words_to_learn.csv"

# Load the data
try:
    # Try to load the words to learn file if it exists
    data = pandas.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    # If not found, load the original data file
    data = pandas.read_csv(DATA_FILE)

to_learn = data.to_dict(orient="records")
current_card = {}
flip_timer = None  # Keep track of the timer

def next_card():
    """Select and display a new random card from the deck"""
    global current_card, flip_timer
    
    # Cancel previous timer if exists
    if flip_timer:
        window.after_cancel(flip_timer)
    
    # Check if we still have cards to learn
    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Congratulations!", fill="black")
        canvas.itemconfig(card_word, text="You've learned all words!", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        return
    
    # Get a random card and show the front side
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text=LANGUAGE_FRONT, fill="black")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE_FRONT], fill="black")
    
    # Set a new timer to flip the card after 3 seconds
    flip_timer = window.after(3000, flip_card)

def flip_card():
    """Flip the card to show the English translation"""
    # Change to the back of the card
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text=LANGUAGE_BACK, fill="white")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE_BACK], fill="white")

def is_known():
    """Mark the current card as known and remove it from the deck"""
    if current_card and len(to_learn) > 0:
        to_learn.remove(current_card)
        
        # Save the updated list to a CSV file
        data_frame = pandas.DataFrame(to_learn)
        # Create the data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        data_frame.to_csv(WORDS_TO_LEARN_FILE, index=False)
        
        # Show the next card
        next_card()

# UI SETUP
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas for displaying the flash card
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Start with the first card
next_card()

window.mainloop()