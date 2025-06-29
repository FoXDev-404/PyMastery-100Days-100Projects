import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Ask for date input (weekly, like 2024-06-01)
date = input("Enter a date (YYYY-MM-DD) for Billboard India chart: ")

# Construct Billboard India URL
url = f"https://www.billboard.com/charts/india-songs-hotw/{date}"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")
songs = []

for item in soup.select("li.o-chart-results-list__item h3.c-title"):
    title = item.get_text(strip=True)
    songs.append(title)

print(f"\n🎵 Found {len(songs)} songs from Billboard India chart on {date}")

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

# Search and collect song URIs
song_uris = []
for song in songs:
    result = sp.search(q=song, type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"⚠️ '{song}' not found on Spotify.")

# Create playlist
playlist_name = f"Billboard India {date}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"\n✅ Playlist '{playlist_name}' created with {len(song_uris)} songs.")
