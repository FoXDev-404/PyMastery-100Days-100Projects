# ## ********Day 54 Start**********
# ## Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# #Functiins are first-class objects, can be passed around as arguments
# # e.g., int/string/float, etc.
#
# def calculate(calc_function, n1,n2):
#     return calc_function(n1, n2)
#
# result = calculate(add, 5, 3)
# print(result)
#
#
# # Nested functions
#
# def outer_function():
#     print("I am outer function")
#
#     def nested_function():
#         print("I am inner function")
#
#     nested_function()
#
# outer_function()
#
#
# # Function can return functions from other functions
# def outer_function():
#     print("I am outer function")
#
#     def nested_function():
#         print("I am inner function")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function


## ******** Python Decorator **********
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()


## ======= Excercise =======
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
