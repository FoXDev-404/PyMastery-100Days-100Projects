from bs4 import BeautifulSoup
import requests

date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract only the top 100 songs
song_elements = soup.select("li.o-chart-results-list__item h3.c-title")
songs = [song.get_text(strip=True) for song in song_elements]
top_100 = songs[:100]

# Print top 100
for i, song in enumerate(top_100, start=1):
    print(f"{i}. {song}")

# Save to a file
with open(f"top_100_songs_{date}.txt", "w", encoding="utf-8") as file:
    for i, song in enumerate(top_100, start=1):
        file.write(f"{i}. {song}\n")

print(f"\nTop 100 songs saved to top_100_songs_{date}.txt")
