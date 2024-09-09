# List data structure in Python is a mutable, ordered sequence of elements.
# List is defined by square brackets [].
# List elements are separated by commas.

# #* List creation
# # Empty list
# empty_list = []
# print(empty_list)  # []

# #* List with elements
# fruits = ['apple', 'banana', 'cherry']
# print(fruits)  # ['apple', 'banana', 'cherry']

# #* List with mixed data types
# mixed_list = [1, 'apple', 2.5, True]
# print(mixed_list)  # [1, 'apple', 2.5, True]

# #* List with nested lists
# nested_list = [1, [2, 3], [4, 5, 6]]
# print(nested_list)  # [1, [2, 3], [4, 5, 6]]

# #* List with list comprehension
# squares = [x**2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]


# #* Accessing List Items Using Indexing
# # Index starts from 0.
# # Negative index starts from -1.
# # List items can be accessed using slicing.

# #* Accessing list items
# fruits = ['apple', 'banana', 'cherry']
# print(fruits[0])  # apple # Positive index
# print(fruits[-1])  # cherry # Negative index

# #* Slicing list
# # Start index is inclusive, end index is exclusive
# print(fruits[1:])  # ['banana', 'cherry']
# print(fruits[:2])  # ['apple', 'banana']
# print(fruits[1:2])  # ['banana']
# print(fruits[-2:])  # ['banana', 'cherry']
# print(fruits[:-1])  # ['apple', 'banana']

# #* Modifying List Items
# # List is mutable, so its elements can be modified.

# # Using index
# fruits = ['apple', 'banana', 'cherry']
# fruits[1] = 'blueberry'
# print(fruits)  # ['apple', 'blueberry', 'cherry']

# # Using slicing
# fruits[1:] = ['blueberry', 'cherry']
# print(fruits)  # ['apple', 'blueberry', 'cherry']

# # Using append() method
# fruits.append('dates')
# print(fruits)  # ['apple', 'blueberry', 'cherry', 'dates']

# # Using insert() method
# fruits.insert(1, 'banana')
# print(fruits)  # ['apple', 'banana', 'blueberry', 'cherry', 'dates']

# # Using extend() method
# fruits.extend(['fig', 'grape'])
# print(fruits)  # ['apple', 'banana', 'blueberry', 'cherry', 'dates', 'fig', 'grape']

# #* Removing List Items
# # List elements can be removed using remove(), pop(), and del.

# # Using remove() method
# fruits.remove('banana')
# print(fruits)  # ['apple', 'blueberry', 'cherry', 'dates', 'fig', 'grape']

# # Using pop() method
# fruits.pop()
# print(fruits)  # ['apple', 'blueberry', 'cherry', 'dates', 'fig']

# # Using del keyword
# del fruits[1]
# print(fruits)  # ['apple', 'cherry', 'dates', 'fig']

# # Using clear() method
# fruits.clear()
# print(fruits)  # Empty list []

#* List Operations
# List concatenation, repetition, and membership operations.

# List concatenation
fruits1 = ['apple', 'banana']
fruits2 = ['cherry', 'dates']
fruits = fruits1 + fruits2
print(fruits)  # ['apple', 'banana', 'cherry', 'dates']

# List repetition
fruits = ['apple', 'banana']
print(fruits * 2)  # ['apple', 'banana', 'apple', 'banana']

# List membership
print('apple' in fruits)  # True
print('cherry' not in fruits)  # True

#* List Methods
# List has several built-in methods to perform various operations.

# append() - Add an element to the end of the list
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']

# clear() - Remove all elements from the list
fruits.clear()

# copy() - Return a shallow copy of the list
fruits = ['apple', 'banana']
fruits_copy = fruits.copy()
print(fruits_copy)  # ['apple', 'banana']

# count() - Return the number of occurrences of an element in the list
fruits = ['apple', 'banana', 'apple']
print(fruits.count('apple'))  # 2

# extend() - Add elements of a list to another list
fruits1 = ['apple', 'banana']
fruits2 = ['cherry', 'dates']
fruits1.extend(fruits2)
print(fruits1)  # ['apple', 'banana', 'cherry', 'dates']
