from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # check if user already exists
        existing_user = db.session.query(User).filter_by(email=email).first()
        if existing_user:
            flash('An account with that email already exists. Please log in.', 'warning')
            return redirect(url_for('login'))

        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=email, name=name, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        # store name in session so secrets page can greet the user
        session['name'] = name
        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    name = session.get('name')
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    # Send the cheat_sheet.pdf file to open in browser
    return send_from_directory(directory='static/files', path='cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
