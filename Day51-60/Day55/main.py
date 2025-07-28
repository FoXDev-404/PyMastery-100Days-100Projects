from flask import Flask

app = Flask(__name__)  # Changed 'all' to 'app'

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f"Hello there {name}!"

if __name__ == "__main__":
    app.run(debug=True)
