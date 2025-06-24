from bs4 import BeautifulSoup
import requests

# Step 2: Ask user for a date
date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

# Step 3: Set up the URL and headers
URL = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

# Step 4: Send a request to Billboard
response = requests.get(URL, headers=headers)
webpage = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")