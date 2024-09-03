"""
Haunted Mansion Escape

Overview:
A text-based adventure game where the player navigates through a haunted mansion to escape.
Choices lead to different scenarios and outcomes.

Usage:
- Choose 'left' or 'right' at the entrance.
- Make decisions to find the correct path and escape.
- Rewards and dangers vary based on choices.

Variables:
- choice1: Player's choice at the entrance.
- choice2: Choice of interacting with a door.
- choice3: Choice of going upstairs or back.
- choice4: Choice of fighting or fleeing.
- choice5: Choice of exploring or going upstairs.
- choice6: Choice of taking or leaving an amulet.
- reward: Type of reward obtained.

Author: @FoXDev-404 (Rajpal Nishad)
"""



# ASCII Art Title
print(r'''  
                                              ,           ^'^  _
                                              )               (_) ^'^
         _/\_                    .---------. ((        ^'^
         (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\|
         ^^           ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
        _         /_____________\ |")| |  |  |/ |_| \|
       (")         |  __   __  |  '==' '=='  /_______\     _
      (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
       \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
     _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,ldb


 _    _                   _           _   __  __                 _             
| |  | |                 | |         | | |  \/  |               (_)            
| |__| | __ _ _   _ _ __ | |_ ___  __| | | \  / | __ _ _ __  ___ _  ___  _ __  
|  __  |/ _` | | | | '_ \| __/ _ \/ _` | | |\/| |/ _` | '_ \/ __| |/ _ \| '_ \ 
| |  | | (_| | |_| | | | | ||  __/ (_| | | |  | | (_| | | | \__ \ | (_) | | | |
|_|  |_|\__,_|\__,_|_| |_|\__\___|\__,_| |_|  |_|\__,_|_| |_|___/_|\___/|_| |_|
      
''')

print("Welcome to the Haunted Mansion Escape!")
print("You are trapped inside a creepy mansion filled with mysterious rooms. Your goal is to escape alive.")
print("Make smart choices to find your way out. Good luck!")

# Starting the game
print("\nYou find yourself at the mansion entrance.")
choice1 = input("Do you want to go 'left' into the dark corridor or 'right' into the dimly lit hallway? ").lower()

if choice1 == "left":
    print(r'''
    You enter the dark corridor and see a spooky old door.
     .-.
    (o o)
    | O |
    \   /
     `~~~'
    ''')
    choice2 = input("Do you want to 'open' the door or 'peek' through the keyhole? ").lower()
    
    if choice2 == "open":
        print('''
        You find a chest filled with gold coins! 🎉
        🪙🪙🪙🪙🪙
        Congratulations, you found a reward!
        ''')
        reward = "gold coins"
        choice3 = input("You see a staircase. Do you want to go 'upstairs' or go back to the 'entrance'? ").lower()
        
        if choice3 == "upstairs":
            print(r'''
            You climb the stairs and find a window. You see a scary ghost!
            .-.
           (o o)
           | O |
           \   /
            `~~~'
            ''')
            choice4 = input("Do you want to 'fight' the ghost or 'jump' out the window? ").lower()
            if choice4 == "fight":
                print('''
                You bravely face the ghost with a silver sword you found earlier!
                You defeat the ghost and escape through the window with your treasure. You win! 🏆
                ''')
            else:
                print("You jump out the window, escape, but leave your treasure behind. You survive but without the reward. Game over.")
        else:
            print("You get lost in the mansion forever. Game over.")
    else:
        print("A ghost scares you away. You run back to the entrance. Game over.")

elif choice1 == "right":
    print('''
    The hallway is filled with flickering lights and eerie paintings.
      .-.
     (o o)
    (  V  )
      | |
    ''')
    choice5 = input("Do you want to 'explore' the library or go 'upstairs'? ").lower()
    
    if choice5 == "explore":
        print('''
        You find an ancient book that opens a secret door. Behind it, you see the exit!
        🎁 You also find a magical amulet that grants you invincibility.
        ''')
        reward = "magical amulet"
        choice6 = input("Do you want to 'take' the amulet and exit or 'leave' it and exit quickly? ").lower()
        if choice6 == "take":
            print('''
            The amulet glows and protects you from any future danger. You escape successfully with a powerful reward! 🏆
            ''')
        else:
            print("You escape quickly but without the amulet's protection. You survive but missed out on a powerful reward. Game over.")
    else:
        print("The stairs collapse beneath you. You fall and get trapped forever. Game over.")

else:
    print("You stand still in fear. A ghost finds you and you lose. Game over.")
