print("☕ Welcome to the Coffee Machine! ☕")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,  # ₹100
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,  # ₹150
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,  # ₹150
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def is_resource_sufficient(order_ingredients):
    """Check if machine has enough resources for the drink and return True if sufficient, False otherwise."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}")
            return False
    return True



def process_coins():
    """Prompt user for coin inputs, calculate and return the total monetary value in rupees."""
    print("Please insert coins.")
    total = 0
    try:
        total += int(input("How many ₹1 coins?: ")) * 1
        total += int(input("How many ₹2 coins?: ")) * 2
        total += int(input("How many ₹5 coins?: ")) * 5
        total += int(input("How many ₹10 coins?: ")) * 10
        total += int(input("How many ₹20 coins?: ")) * 20
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return process_coins()
    return total


def is_transaction_successful(money_received, drink_cost):
    """Process payment, handle change, update profit and return True if payment sufficient, False otherwise."""
    if money_received >= drink_cost:
        change = int(money_received - drink_cost)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False
    
    
def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources and deliver the requested drink to the user."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️ Enjoy!")
    print(f"[Resource usage: {order_ingredients}]")
    
        
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Shutting down the coffee machine. Goodbye! ☕")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    elif choice == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Resources have been refilled.")
    elif choice == "menu":
        print("\n=== AVAILABLE DRINKS ===")
        for drink_name, drink_info in MENU.items():
            print(f"{drink_name.capitalize()}: ₹{drink_info['cost']}")
        print("======================\n")
    elif choice == "help":
        print("\n=== AVAILABLE COMMANDS ===")
        print("espresso/latte/cappuccino - Order a drink")
        print("report - Check machine resources")
        print("refill - Refill all resources")
        print("menu - Show available drinks and prices")
        print("off - Turn off the machine")
        print("==========================\n")
    else:
        if choice not in MENU:
            print(f"Sorry, we don't serve {choice}. Please select a valid option.")
            continue
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            # Display drink price before asking for coins
            print(f"The price of {choice} is ₹{drink['cost']}")
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

