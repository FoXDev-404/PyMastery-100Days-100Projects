from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, select
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False
    )
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(300), nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

# Create table schema and initial record in the database. Requires application context.
with app.app_context():
    # Ensure tables exist before inserting records
    db.create_all()

    # # Add a sample movie only if it doesn't already exist (prevents UNIQUE constraint failures on restart)
    # if not Movie.query.filter_by(title="Phone Booth").first():
    #     new_movie = Movie(
    #         title="Phone Booth",
    #         year=2002,
    #         description=(
    #             "Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
    #             "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation "
    #             "with the caller leads to a jaw-dropping climax."
    #         ),
    #         rating=7.3,
    #         ranking=10,
    #         review="My favorite character was the caller.",
    #         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    #     )

    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )

    db.session.add(second_movie)
    try:
        db.session.commit()
    except Exception:
        # Rollback on any error to keep the session clean
        db.session.rollback()


@app.route("/")
def home():
    # Query all Movie rows and extract mapped Movie objects using .scalars()
    stmt = select(Movie)
    movies = db.session.execute(stmt).scalars().all()
    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
