from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

POSTS_PER_PAGE = 5
POSTS_API_URL = "https://api.npoint.io/bd1a4eac9c8740415a56"

# Email configuration
OWN_EMAIL = os.getenv("EMAIL")
OWN_PASSWORD = os.getenv("EMAIL_PASSWORD")

posts = requests.get(POSTS_API_URL).json()


@app.route('/')
def get_all_posts():
    page = request.args.get('page', 1, type=int)
    total_pages = (len(posts) + POSTS_PER_PAGE - 1) // POSTS_PER_PAGE
    start = (page - 1) * POSTS_PER_PAGE
    end = start + POSTS_PER_PAGE
    paginated_posts = posts[start:end]
    return render_template('index.html', posts=paginated_posts, page=page, total_pages=total_pages)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    bg_url = post.get('bg_url', 'https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=1500&q=80')
    return render_template('post.html', post=post, bg_url=bg_url)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


def send_email(name, email, phone, message):
    if not OWN_EMAIL or not OWN_PASSWORD:
        return

    email_message = f"Subject:New Message from Blog Contact Form\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
    except Exception as e:
        print(f"Email error: {e}")


if __name__ == '__main__':
    app.run(debug=True)