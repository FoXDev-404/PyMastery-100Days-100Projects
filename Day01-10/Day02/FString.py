# F-String 

# print(round(8/3, 2)) # 2.67
# print(8 // 3) # 2 The floor division // rounds the result down to the nearest whole number
# print(type(8 // 3)) # <class 'int'>

'''
name = "Raj"
age = 24
height = 1.75
print("Your name is " + name + ", your age is " + (age) + ", your height is " + (height) + " m.")
## TypeError: can only concatenate str (not "int") to str
## Solution: Convert int to str
## print("Your name is " + name + ", your age is " + str(age) + ", your height is " + str(height) + " m.")
## To avoid this, we can use f-string to format the string
'''


# f-string 
Name = "Raj"
Age = 24
Height = 1.75

print(f"Your name is {Name}, your age is {Age}, your height is {Height} m.") # Your name is Raj, your age is 24, your height is 1.75 m.
