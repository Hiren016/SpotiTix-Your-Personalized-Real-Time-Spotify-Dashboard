import pandas as pd
import os
from datetime import datetime
from spotify_auth import get_spotify_client

def format_duration(ms):
    seconds = ms // 1000
    minutes = (seconds // 60) % 60
    hours = seconds // 3600
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def fetch_recently_played_tracks(limit=50, output_file="data/recently_played_tracks.xlsx"):
    sp = get_spotify_client()
    print(f"🎧 Fetching recently played tracks (limit={limit})...")

    results = sp.current_user_recently_played(limit=limit)

    played_tracks = []
    fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in results['items']:
        track = item['track']
        played_at = item['played_at']
        duration_ms = track['duration_ms']
        duration = format_duration(duration_ms)

        track_data = {
            'fetched_at': fetched_at,
            'played_at': played_at,
            'track_name': track['name'],
            'artist': track['artists'][0]['name'] if track['artists'] else None,
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'duration_ms': duration_ms,
            'duration': duration,  # ✅ Human readable
            'explicit': track['explicit'],
            'track_url': track['external_urls']['spotify'],
            'image_url': track['album']['images'][0]['url'] if track['album']['images'] else None,
            'album_type': track['album']['album_type'],
            'track_number': track['track_number'],
            'total_tracks_in_album': track['album']['total_tracks'],
            'artist_id': track['artists'][0]['id'],
            'album_id': track['album']['id'],
            'track_id': track['id']
        }

        played_tracks.append(track_data)

    df = pd.DataFrame(played_tracks)
    os.makedirs("data", exist_ok=True)
    df.to_excel(output_file, index=False)
    print(f"✅ Recently played tracks saved to: {output_file}")
    return df

if __name__ == "__main__":
    fetch_recently_played_tracks(limit=50)
