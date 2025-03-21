import random

word_list = ["python", "elephant", "guitar", "jupiter", "quantum", 
             "mountain", "chocolate", "butterfly", "galaxy", "waterfall",
             "orchestra", "helicopter", "kangaroo", "umbrella", "volcano",
             "adventure", "detective", "lighthouse", "paradox", "zephyr"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder+= "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a latter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display+= letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
            
        else:
            display+= "_"

    print(display)
    
    if "_" not in display:
        game_over = True
        print("You Win")