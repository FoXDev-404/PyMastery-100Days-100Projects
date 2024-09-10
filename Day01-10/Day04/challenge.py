# This is a coding challenge from Day 4
#* Using list of names, and find the random name from the list and that person will pay the bill
#* Input: List of names
#* Output: Random name from the list

import random

names_list = ["Aman", "Bhavesh", "Chirag", "Dhruv", "Eshaan", "Fenil", "Gaurav", "Hemant", "Ishaan", "Jatin"]
name = random.choice(names_list)

print(f"{name} is going to buy the meal today!")
