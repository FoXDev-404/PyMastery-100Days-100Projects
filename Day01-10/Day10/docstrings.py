"""
A docstring in Python is a special string literal used to document modules, classes, functions, or methods. 
It is placed as the first statement in the definition and is accessible via the __doc__ attribute.

Docstrings help explain what a function, class, or module does, making code easier to understand and maintain.
They are typically written using triple quotes (\"\"\" or ''') so they can span multiple lines.

Example:
"""

def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

# Accessing the docstring
print(add.__doc__)