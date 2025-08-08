from flask import Flask, render_template  # Import Flask and render_template for web app and HTML rendering

app = Flask(__name__)  # Create a Flask application instance


@app.route("/")  # Define the route for the home page
def home():
    # Render the index.html template when accessing the root URL
    return render_template('index.html')

@app.route("/login")  # Define the route for the login page
def login():
    # Render the login.html template when accessing /login
    return render_template('login.html')

if __name__ == '__main__':
    # Run the Flask development server if this file is executed directly
    app.run(debug=True)
