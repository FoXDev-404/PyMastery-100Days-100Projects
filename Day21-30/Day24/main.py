# Read a file and print its contents
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write to a file
# with open("new_file.txt", "w") as file:
#     file.write("New line added to the file\n")
#     file.write("Another line added to the file\n")


# Relative path vs Absolute path
# Relative path: relative to the current working directory
# Example:
with open("new_file.txt") as file:
    contents = file.read()
    print(contents)


# Absolute path: full path to the file
# Example:
with open(r"C:\Users\rajpa\Desktop\PyMastery-100Days-100Projects\Day21-30\Day24\my_file.txt") as file:
    contents = file.read()
    print(contents)