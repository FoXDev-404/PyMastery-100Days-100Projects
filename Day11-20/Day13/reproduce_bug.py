from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # There is a bug(when dice_num =6) IndexError & It starts form 1, the image in list at index 0 well never be printed
dice_num = randint(0, 5)
print(dice_num)
print(dice_images[dice_num])
