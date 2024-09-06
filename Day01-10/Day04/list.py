# List data structure in Python is a mutable, ordered sequence of elements.
# List is defined by square brackets [].
# List elements are separated by commas.

# List creation
# Empty list
empty_list = []
print(empty_list)  # []

# List with elements
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # ['apple', 'banana', 'cherry']

# List with mixed data types
mixed_list = [1, 'apple', 2.5, True]
print(mixed_list)  # [1, 'apple', 2.5, True]

# List with nested lists
nested_list = [1, [2, 3], [4, 5, 6]]
print(nested_list)  # [1, [2, 3], [4, 5, 6]]

# List with list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


#* Accessing List Items Using Indexing
# Index starts from 0.
# Negative index starts from -1.
# List items can be accessed using slicing.

# Accessing list items
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # apple # Positive index
print(fruits[-1])  # cherry # Negative index
