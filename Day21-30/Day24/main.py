# Read a file and print its contents
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write to a file
with open("new_file.txt", "w") as file:
    file.write("New line added to the file\n")
    file.write("Another line added to the file\n")