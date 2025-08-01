# Day 57: URL Building and Templating with Jinja in Your Flask Application
from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/')
def home():
    num = random.randint(1, 100)
    year = datetime.now().year
    return render_template('index.html', num=num, year=year)


if __name__ == "__main__":
    app.run(debug=True)