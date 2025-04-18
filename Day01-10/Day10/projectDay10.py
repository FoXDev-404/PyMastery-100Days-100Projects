"""
Calculator App

A simple command-line calculator that can perform basic arithmetic operations:
- Addition
- Subtraction  
- Multiplication
- Division

The calculator supports operation chaining by continuing with the previous result.
"""

from calculator_art import logo

def add(n1, n2):
    """Add two numbers and return the result."""
    return n1 + n2

def subtract(n1, n2):
    """Subtract n2 from n1 and return the result."""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers and return the result."""
    return n1 * n2

def divide(n1, n2):
    """
    Divide n1 by n2 and return the result.
    Prints an error and returns None if division by zero is attempted.
    """
    if n2 == 0:
        print("❌ Error: Cannot divide by zero.")
        return None
    return n1 / n2

# Dictionary mapping symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """Run the calculator program with chaining support."""
    print(logo)
    print("🔢 Welcome to the Calculator App!")

    num1 = float(input("What's the first number?: "))

    while True:
        # Display available operations
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("⚠️ Invalid operation. Please choose from the list.")
            continue

        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        if answer is None:
            print("⚠️ Calculation failed. Starting over...\n")
            return calculator()

        print(f"✅ {num1} {operation_symbol} {num2} = {answer}")

        next_step = input(f"Type 'y' to continue calculating with {answer}, 'n' to start new, or 'exit' to quit: ").lower()

        if next_step == 'y':
            num1 = answer
        elif next_step == 'n':
            print("\n🔄 Starting a new calculation...\n")
            return calculator()
        elif next_step == 'exit':
            print("👋 Thanks for using the Calculator App. Goodbye!")
            break
        else:
            print("⚠️ Invalid input. Exiting...")
            break

# Start the calculator
if __name__ == "__main__":
    calculator()
