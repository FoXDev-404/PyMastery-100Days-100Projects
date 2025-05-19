# List comprehension is a concise way to create lists in Python.
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# List comprehension with string manipulation
names = ["Alex", "Beth", "Carolina", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)  # Output: ['Alex', 'Beth', 'Dave']

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)



# TODO: =============== Dictionary Comprehension ================== #
import random

names = ["Alex", "Beth", "Carolina", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names} # Dictionary comprehension
print(students_scores)
passed_students = {student: "pass" for student, score in students_scores.items() if score >= 50} # Dictionary comprehension with condition
print(passed_students)
failed_students = {student: "fail" for student, score in students_scores.items() if score < 50}
print(failed_students)