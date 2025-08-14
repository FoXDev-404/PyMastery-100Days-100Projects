# import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# # cursor.execute("""
# #     CREATE TABLE books (
# #         id INTEGER PRIMARY KEY,
# #         title VARCHAR(250) NOT NULL UNIQUE,
# #         author VARCHAR(250) NOT NULL,
# #         rating FLOAT NOT NULL
# #     );
# # """)

# cursor.execute("""INSERT INTO books VALUES
#     (1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 9.3)
#                """)
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# Read all Records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

# Read A Particular Records By Query
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # To get a single element we can use scalar() instead of scalars().

# Update A Record By PRIMARY KEYbook_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
# Flask-SQLAlchemy also has some handy extra query methods like get_or_404 that we can use.
# Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.
# query.get have been deprecated

# Delete A Particular Record By PRIMARY KEYbook_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
# You can also delete by querying for a particular value e.g. by title or one of the other properties.
# Again, the get_or_404() method is quite handy.