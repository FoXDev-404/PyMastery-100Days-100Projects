# def greet():
#     print("Namaste")
#     print("Hello")
#     print("Good Morning")

# greet()

# # function with name 
# def greet_with_name(name):
#     print(f"Namaste {name}")
#     print(f"Hello {name}")
#     print(f"Good Morning {name}")
    
# greet_with_name("Raj")

# Function with more then 1 input
def greet_with(name,location):
    print(f"Good morning {name} from {location}")
    
greet_with("Raj", "India")
greet_with("India", "Raj") # Positional argument
greet_with(location="India", name="Raj") # Keyword argument