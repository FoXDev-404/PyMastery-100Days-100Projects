from flask import Flask

# Creating the Flask app object
app = Flask(__name__)

# # ------------------- Custom Decorators -------------------
#
# # This will make the text bold
# def make_bold(func):
#     def wrapper_function():
#         return f"<b>{func()}</b>"
#     return wrapper_function
#
# # This will make the text italic
# def make_emphasis(func):
#     def wrapper_function():
#         return f"<em>{func()}</em>"
#     return wrapper_function
#
# # This will underline the text
# def make_underlined(func):
#     def wrapper_function():
#         # return f"<em><u><b>Bye!</b></u></em>"
#         return f"<u>{func()}</u>"
#     return wrapper_function
#
# # ------------------- Routes -------------------
#
# # Home page
# @app.route("/")
# def hello_world():
#     return (
#         "<h1 style='text-align: center'>Hello, World!</h1>"
#         "<p>This is a paragraph.</p>"
#         "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjEyeDhldWp6dGd2N2dzOXhlcnlmMXd2NDNmMXMzaG5mbzQwcmgyaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12bjQ7uASAaCKk/giphy.gif' width=200px>"
#     )
#
# # Route that shows "Bye!" text with bold, underline and italic styling
# @app.route("/bye")
# @make_emphasis       # italics
# @make_underlined     # underline
# @make_bold           # bold
# def bye():
#     return "Bye!"
#
# # Dynamic route where values come from URL
# # Example: /username/Raj/22 -> Hello there Rahul, you are 22 years old.
# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello there {name}, you are {number} years old."
#
# # Run
# if __name__ == "__main__":
#     app.run(debug=True)


## Advanced Python Decoder Functions

# A simple User class with name and login status
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# Decorator to check if user is authenticated (logged in)
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        # First argument is expected to be the 'user' object
        if args[0].is_logged_in == True:
            # If logged in, then run the function
            function(args[0])
        else:
            print("Access denied: Please log in first.")
    return wrapper

# This function creates a blog post – but only if user is logged in
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Raj")
new_user.is_logged_in = True  # Simulate user login
create_blog_post(new_user)
