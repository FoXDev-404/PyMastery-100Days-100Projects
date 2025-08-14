from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import re

app = Flask(__name__)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


def parse_rating(raw: str) -> float:
    """Parse rating input into a float (0-10 scale).

    Supported formats:
    - '9' or '9.5' -> 9.0 or 9.5
    - '10/10' -> 10.0
    - '4/5' -> (4/5)*10 = 8.0  (converts common 5-star inputs to 10-scale)
    - '80%' -> 8.0
    """
    if raw is None:
        raise ValueError('No rating provided')
    s = raw.strip()
    # percent format
    if s.endswith('%'):
        try:
            pct = float(s[:-1])
            return pct / 10.0
        except ValueError:
            raise ValueError(f'Invalid percent rating: {raw}')

    # fraction format a/b
    if '/' in s:
        parts = s.split('/')
        if len(parts) == 2:
            num_s, den_s = parts[0].strip(), parts[1].strip()
            try:
                num = float(num_s)
                den = float(den_s)
            except ValueError:
                raise ValueError(f'Invalid fractional rating: {raw}')
            if den == 0:
                raise ValueError('Denominator cannot be zero')
            # If denominator is 10, assume the numerator is already on 0-10 scale
            if den == 10:
                return float(num)
            # Otherwise scale to 0-10 (e.g., 4/5 -> (4/5)*10 = 8)
            return (num / den) * 10.0

    # plain number
    # allow commas as decimal separators
    s2 = s.replace(',', '.')
    # extract leading number using regex
    m = re.match(r"^([-+]?[0-9]*\.?[0-9]+)", s2)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass
    raise ValueError(f'Could not parse rating: {raw}')


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        title = request.form.get("title")
        author = request.form.get("author")
        rating_raw = request.form.get("rating")

        try:
            rating_val = parse_rating(rating_raw)
        except ValueError as e:
            # Bad input — return a helpful error page or redirect back to add
            return f"Invalid rating: {e}", 400

        new_book = Book(
            title=title,
            author=author,
            rating=rating_val
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        rating_raw = request.form.get("rating")
        try:
            book_to_update.rating = parse_rating(rating_raw)
        except ValueError as e:
            return f"Invalid rating: {e}", 400
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
