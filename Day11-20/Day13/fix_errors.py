"""
age = int(input("How old are you?"))
'''
What is the user enters: "Twelve",
it will show an "ValueError" error in terminal
'''
if age > 18:
    print("You can drive at age {age}")
"""
 
# To solve this problem we can use try:, except
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print("Sorry, you're not old enough to drive yet.")
