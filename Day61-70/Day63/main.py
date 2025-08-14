from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Use .get to avoid KeyError and validate required fields
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")

        if not title or not author or not rating:
            # Bad request: required form fields missing
            return "Error: Missing required form fields (title, author, rating)", 400

        new_book = {
            "title": title,
            "author": author,
            "rating": rating,
        }
        all_books.append(new_book)
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

