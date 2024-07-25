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

# Example 2
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")
else:
    print("You can't vote!")

# Comparison Operators >, <, >=, <=, ==, !=

# Example 3 [Nested if-else, elif]
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
    if age >= 60:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a kid.")
'''

# Example 4 [Multiple if statement in succession]
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
if marks >= 80:
    print("Grade B")
if marks >= 70:
    print("Grade C")
if marks >= 60:
    print("Grade D")
if marks < 60:
    print("Grade F")
