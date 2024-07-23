# Conditional operator in Python
# Conditional operator is also known as ternary operator
# if, else, elif are conditional statements in Python
# Syntax: [on_true] if [expression] else [on_false]

'''
# Example 1
a = 10
b = 20
mini = a if a < b else b
print(mini)
'''

# Example 2
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")
else:
    print("You can't vote!")

# Comparison Operators >, <, >=, <=, ==, !=