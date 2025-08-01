from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the Home Page"

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age = age_response.json()['age']
    gender = gender_response.json()['gender']
    return render_template('index.html', name=name, age=age, gender=gender)



if __name__ == "__main__":
    app.run(debug=True)