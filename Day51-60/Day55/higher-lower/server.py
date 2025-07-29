from flask import Flask
import random

app = Flask(__name__)

# Generate the random number only once when the server starts
random_number = random.randint(0, 9)
# print(f"Random number is: {random_number}")  # For debugging purpose


# Home Page
@app.route("/")
def home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    )


# Guess route
@app.route("/<int:number>")
def guess(number):
    if number < random_number:
        return (
            f"<h1 style='color: blue;'>{number} is too low! Try again.</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        )
    elif number > random_number:
        return (
            f"<h1 style='color: red;'>{number} is too high! Try again.</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        )
    else:
        return (
            f"<h1 style='color: green;'>{number} is correct!</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        )


# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)
