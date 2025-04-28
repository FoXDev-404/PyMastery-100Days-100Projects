class MoneyMachine:

    CURRENCY = "₹"

    COIN_VALUES = {
        "₹1": 1,
        "₹2": 2,
        "₹5": 5,
        "₹10": 10,
        "₹20": 20
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        self.money_received = 0
        for coin in self.COIN_VALUES:
            try:
                self.money_received += int(input(f"How many {coin} coins?: ")) * self.COIN_VALUES[coin]
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                return self.process_coins()
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = int(self.money_received - cost)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

