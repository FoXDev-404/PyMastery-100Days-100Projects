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


# Example 5 [Using conditional operator]. Max of 3 numbers
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))

if input1 > input2:
    if input1 > input3:
        print(input1)
    else:
        print(input3)
else:
    if input2 > input3:
        print(input2)
    else:
        print(input3)


# Example 6 [ 4 levels of nested if-else]

a = 10
b = 20
c = 30
d = 40

if a > b:
    if a > c:
        if a > d:
            print(a)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)
else:
    if b > c:
        if b > d:
            print(b)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)


# Example 7 [Using conditional operator]. Age drinking eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You can drink.")
else:
    print("You can't drink.")
'''

# Example 8 [Using conditional operator]. If marks > 40, pass else fail
marks = int(input("Enter your marks: "))
if marks > 90:
    print("Grade A")
elif marks > 80:
    print("Grade B")
elif marks > 70:
    print("Grade C")
elif marks > 60:
    print("Grade D")
else:
    print("Grade F")
    
