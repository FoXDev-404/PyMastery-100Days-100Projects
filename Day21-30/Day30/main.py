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
    file.close()
    print("FIle was closed.")

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