import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from .env
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Ask user for date
date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

# Billboard URL
URL = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {"User-Agent": "Mozilla/5.0"}

# Scrape Billboard songs
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
song_elements = soup.select("li.o-chart-results-list__item h3.c-title")
songs = [song.get_text(strip=True) for song in song_elements][:100]

print(f"\n🎵 Found {len(songs)} songs from {date} Billboard Hot 100.")

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]

# Search for each song on Spotify
song_uris = []
year = date.split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"⚠️ '{song}' not found on Spotify.")

# Create a new private playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"\n✅ Playlist '{date} Billboard 100' created successfully with {len(song_uris)} songs.")
