programming_dictonary = {
    "Python": "Python is a programming language that lets you work quickly and integrate systems more effectively.",
    "MERN": "MERN is a JavaScript stack used for easier and faster deployment of full-stack web applications.",
    "Py-Dictonary": "A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.",
    123: "This is a number key",
}

# print(programming_dictonary["Py-Dictonary"])
# print(programming_dictonary[123])

# Add a new item to the dictionary
programming_dictonary["Loop"] = "A loop is a programming structure that repeats a sequence of instructions until a specific condition is met."

empty_dictonary = {}

# Wipe the dictionary
# programming_dictonary = {}
# print(programming_dictonary)

# Edit an item in the dictionary
programming_dictonary["Pthon"] = "Python is a high-level programming language."
# print(programming_dictonary["Pthon"])

# Loop through a dictionary
for key in programming_dictonary:
    print(key)
    print(programming_dictonary[key])
