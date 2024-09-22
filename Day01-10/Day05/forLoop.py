# Define a list of fruits
fruits = ["Apple", "Peach", "Pear"]

# Iterate through each fruit in the list and perform actions
for fruit in fruits:
    print(fruit)                   # Print the fruit name
    print(f"{fruit} pie")           # Print the fruit followed by 'pie'

# Demonstrating code outside the loop
print("\nThis line is outside the for loop.")

# Show the effect of printing the entire list inside and outside a loop
for fruit in fruits:
    print(fruit)                   # Print individual fruit
    print(fruits)                  # Print the entire list multiple times (inside the loop)

print(f"\n{fruits}")               # Print the list only once (outside the loop)

# Using range() to print numbers 1 to 10
print("\nNumbers from 1 to 10:")
for number in range(1, 11):
    print(number)

# Using range() to print numbers from 1 to 10 with a step of 2
print("\nNumbers from 1 to 10 (step of 2):")
for number in range(1, 11, 2):
    print(number)

# Using range() to print numbers from 10 to 2 in reverse (step of -2)
print("\nNumbers from 10 to 2 (reverse step of 2):")
for number in range(10, 1, -2):
    print(number)

# Using range() to print numbers from 10 to 1 in reverse
print("\nNumbers from 10 to 1 (step of -1):")
for number in range(10, 0, -1):
    print(number)

# Nested loop example to print combinations of two numbers
print("\nNested loop example:")
for number in range(3):
    for num in range(3):
        print(f"({number}, {num})")

# Nested loop example to print combinations of two numbers with a condition
print("\nNested loop example with condition:")
for number in range(3):
    for num in range(3):
        if number != num:
            print(f"({number}, {num})")

# Nested loop example to print combinations of three numbers with a condition
print("\nNested loop example with condition:")
for number in range(3):
    for num in range(3):
        for n in range(3):
            if number != num and num != n and number != n:
                print(f"({number}, {num}, {n})")
