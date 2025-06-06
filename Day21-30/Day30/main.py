# FileNotFoundError
# with open("a_file.txt", "r") as file:
#     file.read()

# Fix the code to handle the error
try:
    file = open("a_file.txt", "r") # Attempt to open a file that may not exist
    a_dict = {"name": "Alice", "age": 30} # Example dictionary
    print(a_dict["age"]) # Accessing a key that exists
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("This is a new file created because the original was not found.")
except KeyError as error_message:
    print(f"KeyError: {error_message} - The key does not exist in the dictionary.")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("This is a custom KeyError message.") # Raising a custom KeyError

# KeyError
# my_dict = {"name": "Alice"}
# print(my_dict["age"])

# IndexError
# my_list = [1, 2, 3]
# print(my_list[5])

# TypeError
# def add_numbers(a, b):
#     return a + b
# print(add_numbers(5, "10"))



hight = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

if hight > 3:
    raise ValueError("Height cannot be greater than 3 meters.")
if weight < 0:
    raise ValueError("Weight cannot be negative.")

bmi = weight / (hight ** 2)
print(f"Your BMI is: {bmi:.2f}")