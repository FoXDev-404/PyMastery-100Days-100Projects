# Logical operators in Python are used to combine conditional statements: and, or, not
# and: Returns True if both statements are true
# or: Returns True if one of the statements is true
# not: Reverse the result, returns False if the result is true

#* Example program using normal if-else statements
'''
def calculate_cost():
    # Ask for the user's height in centimeters
    height = int(input("Enter your height in centimeters: "))

    # Check if the user is tall enough to ride
    if height <= 120:
        print("You are not tall enough to ride. Sorry!")
        return
    
    print("Great! You can ride.")

    # Ask for the user's age
    age = int(input("Enter your age: "))

    # Determine the ticket price based on the user's age
    if age < 12:
        ticket_price = 100  #* Price for children under 12 years
    elif 12 <= age < 18:
        ticket_price = 200  #* Price for teens between 12 and 18 years
    elif 45 <= age <= 55:
        ticket_price = 50   #* Discounted price for people aged 45 to 55
    else:
        ticket_price = 500  #* Standard price for adults (18 and above)

    # Ask if the user wants photos
    wants_photos = input("Would you like to add photos for an extra ₹50? (Y/N): ").strip().lower()

    # Add the cost of photos if the user wants them
    if wants_photos == 'y':
        ticket_price += 50

    # Display the total cost to the user
    print(f"Your total cost is ₹{ticket_price}.")


# Start the process
calculate_cost()
'''

#* Example program using logical operators
def family_gathering():
    # Ask if it's a weekend
    is_weekend = input("Is it a weekend? (Y/N): ").strip().lower() == 'y'

    # Ask if the user has finished their work
    finished_work = input("Have you finished your work? (Y/N): ").strip().lower() == 'y'

    # Ask if the user has received a special invite
    received_invite = input("Did you receive a special invite? (Y/N): ").strip().lower() == 'y'

    # Determine if the user can attend the family gathering
    # Conditions:
    # - It must be a weekend (is_weekend is True)
    # - User must have finished their work (finished_work is True)
    # - User must have received a special invite (received_invite is True)
    if is_weekend and finished_work and (received_invite or not received_invite):
        print("Awesome! You can attend the family gathering.")
    else:
        print("Oh no, you can't attend the family gathering today.")

# Start the process
family_gathering()
