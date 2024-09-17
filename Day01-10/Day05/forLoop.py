# for loop in python list

# Define a list of fruits
fruits = ["Apple", "Peach", "Pear"]

# For loop to iterate through each fruit in the list
for fruit in fruits:
    # Print the name of the fruit
    print(fruit)
    # Print the fruit name followed by 'pie'
    print(fruit + " pie")

# Example of code outside the loop
print("This line is outside the for loop.")

# Another example showing the importance of indentation
for fruit in fruits:
    print(fruit)
    # Printing the list inside the loop will print it multiple times
    print(fruits)

# Printing the list outside the loop will print it only once
print(fruits)

# Example of using the range function with a for loop
for number in range(1, 11):
    print(number)

# Example of using the range function with a for loop and a step
for number in range(1, 11, 2):
    print(number)
    
# Example of using the range function with a for loop and a step
for number in range(10, 1, -2):
    print(number)

# Example of using the range function with a for loop and a step
for number in range(10, 0, -1):
    print(number)

# Nested for loop example
for number in range(3):
    for num in range(3):
        print(f"({number}, {num})")
