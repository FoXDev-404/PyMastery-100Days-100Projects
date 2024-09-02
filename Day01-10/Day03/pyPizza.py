# 3 Day of Code -
#* Pizza Order System.

print("Hey there! Welcome to InPizza Delivery!")
print("Which size pizza would you like to order today?")
size = input("Choose: S for Small, M for Medium, or L for Large: ").lower()  # Converts input to lowercase

print("Would you like to add some Pepperoni to your pizza?")
pepperoni = input("Press Y for Yes or N for No: ").lower()

print("How about some extra cheese to make it more cheesy?")
cheese = input("Press Y for Yes or N for No: ").lower() 

bill = 0

#* Calculate the total bill based on size and toppings
#* Small: Rs.99, Medium: Rs.199, Large: Rs.299
if size == "s":
    bill += 99
    if pepperoni == "y":
        bill += 20
    if cheese == "y":
        bill += 10
elif size == "m":
    bill += 199
    if pepperoni == "y":
        bill += 30
    if cheese == "y":
        bill += 10
elif size == "l":
    bill += 299
    if pepperoni == "y":
        bill += 40
    if cheese == "y":
        bill += 10
else:
    print("Hmm, that doesn't seem right. Please check your selection and try again!")

print(f"Your total bill is: Rs.{bill}.")
print("Thanks for ordering with InPizza Delivery! We hope you enjoy your meal!")
