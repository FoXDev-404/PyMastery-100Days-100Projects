from bs4 import BeautifulSoup
import requests

date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

# Scrape song titles - as of now Billboard uses h3 tags with specific classes
songs = []
song_elements = soup.select("li ul li h3")  # Billboard titles are in h3 under nested lists
