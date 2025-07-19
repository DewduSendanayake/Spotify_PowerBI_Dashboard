import requests
import pandas as pd

def get_spotify_token(client_id: str, client_secret: str) -> str:
    """
    Uses Client Credentials flow to get an access token.
    Only works for public endpoints (no user data).
    """
    auth_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(auth_url, data=payload)
    response.raise_for_status()
    return response.json()['access_token']

def search_track(track_name: str, artist_name: str, token: str) -> str | None:
    """
    Searches Spotify for a track by name & artist, returns the track ID if found.
    """
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        'q': f"{track_name} artist:{artist_name}",
        'type': 'track',
        'limit': 1
    }
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    items = resp.json().get('tracks', {}).get('items', [])
    return items[0]['id'] if items else None

def get_track_image(track_id: str, token: str) -> str | None:
    """
    Fetches album art URL for a given track ID.
    """
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    images = resp.json().get('album', {}).get('images', [])
    return images[0]['url'] if images else None

# === Your credentials ===
client_id = '26ee2f8b28c444e28dc0ec8e793422f4'
client_secret = '01c14cb6da22468ca373d9faa8259122'

# === Get a token ===
access_token = get_spotify_token(client_id, client_secret)

# === Load your CSV ===
df = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# === Enrich with album art ===
df['image_url'] = None  # initialize column
for i, row in df.iterrows():
    tid = search_track(row['track_name'], row['artist_name'], access_token)
    if tid:
        df.at[i, 'image_url'] = get_track_image(tid, access_token)

# === Save out ===
df.to_csv('updated_file.csv', index=False)
