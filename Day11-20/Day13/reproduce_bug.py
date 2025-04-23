"""
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # There is a bug(when dice_num =6) IndexError & It starts form 1, the image in list at index 0 well never be printed
dice_num = randint(0, 5)
print(dice_images[dice_num])
"""

# Play Computer and think what will the computer do when this code will run
year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994: # The year 1980 will not produce any results
if year >= 1980 and year < 1994: # Correct code
    print("You are a millennial.")
# elif year > 1994: # The year 1994 and will not produce any results
elif year >= 1994: # Correct code
    print("You are a Gen Z.")
