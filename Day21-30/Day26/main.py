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


# =============== Coding Exercise ================== #
# 1. Create a dictionary where the keys are the words in the sentence and the values are the lengths of those words.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# 2. Convert the Celsius temperatures to Fahrenheit using dictionary comprehension.
# Formula: F = C * 9/5 + 32
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: temp * 9/5 + 32 for day, temp in weather_c.items()}
print(weather_f)


# How to iterate over a Panda DataFrame
import pandas as pd

student_dict = {
    "student": ["Alex", "Beth", "Carolina", "Dave", "Elanor", "Freddie"],
    "score": [56, 78, 45, 89, 90, 100]
}

student_df = pd.DataFrame(student_dict)

# Loop through rows of the DataFrame
for (index, row) in student_df.iterrows():
    print(index, row)
    # print(row.student)  # Accessing the student name
    # print(row.score)    # Accessing the score
    if row.student == "Alex":
        print("Alex's score is:", row.score)
