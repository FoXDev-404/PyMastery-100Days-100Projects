# Day 57: URL Building and Templating with Jinja in Your Flask Application
from flask import Flask, render_template
from datetime import datetime
import random
import requests

app = Flask(__name__)


@app.route('/')
def home():
    num = random.randint(1, 10)
    year = datetime.now().year
    return render_template('index.html', num=num, year=year)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age = age_response.json()['age']
    gender = gender_response.json()['gender']
    return render_template('guess.html', name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)