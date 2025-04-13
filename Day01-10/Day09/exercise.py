"""
Program: Student Grading Program
Author: FoXDev-404(PsychoIND)
Date: April 13, 2025

Description:
    This program reads a dictionary of student names and their exam scores,
    then evaluates and assigns a grade based on the following criteria:

        - 91-100: "Outstanding"
        - 81-90 : "Exceeds Expectations"
        - 71-80 : "Acceptable"
        - <=70  : "Fail"

    It generates a new dictionary (student_grades) where each student's
    name maps to their respective grade, and prints the result.

Usage:
    Run the script as is. The output will be the student_grades dictionary.
"""

# Dictionary of students and their respective exam scores
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Dictionary to store final grades
student_grades = {}

for student in student_scores:
    score = student_scores[student]

    # Grade based on score range
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Final grades
print(student_grades)
