## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Functiins are first-class objects, can be passed around as arguments
# e.g., int/string/float, etc.

def calculate(calc_function, n1,n2):
    return calc_function(n1, n2)

result = calculate(add, 5, 3)
print(result)


# Nested functions

def outer_function():
    print("I am outer function")

    def nested_function():
        print("I am inner function")

    nested_function()

outer_function()


# Function can return functions from other functions
def outer_function():
    print("I am outer function")

    def nested_function():
        print("I am inner function")

    return nested_function

inner_function = outer_function()
