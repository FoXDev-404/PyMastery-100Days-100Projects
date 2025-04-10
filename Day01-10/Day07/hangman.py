import random

hangman_stages = [
    # Stage 0: Full hangman (game over)
    '''
      +--------+
      |        |
      O        |
     /|\\       |
      |        |
     / \\       |
               |
    ============''',    

    # Stage 1: One leg missing
    '''
      +--------+
      |        |
      O        |
     /|\\       |
      |        |
     /         |
               |
    ============''',    

    # Stage 2: No legs
    '''
      +--------+
      |        |
      O        |
     /|\\       |
      |        |
               |
               |
    ============''',    

    # Stage 3: One arm missing
    '''
      +--------+
      |        |
      O        |
     /|        |
      |        |
               |
               |
    ============''',    

    # Stage 4: No arms
    '''
      +--------+
      |        |
      O        |
      |        |
      |        |
               |
               |
    ============''',    

    # Stage 5: Head only
    '''
      +--------+
      |        |
      O        |
               |
               |
               |
               |
    ============''',    

    # Stage 6: Empty gallows (fully recovered)
    '''
      +--------+
      |        |
               |
               |
               |
               |
               |
    ============'''    
]

word_list = ["python", "elephant", "guitar", "jupiter", "quantum", 
             "mountain", "chocolate", "butterfly", "galaxy", "waterfall",
             "orchestra", "helicopter", "kangaroo", "umbrella", "volcano",
             "adventure", "detective", "lighthouse", "paradox", "zephyr"]

life = 6
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
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display+= letter
            if letter not in correct_letters:
                correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
            
        else:
            display+= "_"

    print(display)
    
    if guess not in chosen_word:
        life-=1        
        if life == 0:
            game_over = True
            print("\n***************Game Over You lost***************\n")

    
    print(f"***************{life}/6 LIVES LEFT***************")
    print(hangman_stages[life])
        
    if "_" not in display:
        game_over = True
        print("\n***************You Win🏆***************\n")
    