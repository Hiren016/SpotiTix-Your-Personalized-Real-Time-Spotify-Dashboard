from spotify_auth import get_spotify_client
import pandas as pd
import os
from datetime import datetime

def format_duration(ms):
    seconds = ms // 1000
    minutes = (seconds // 60) % 60
    hours = seconds // 3600
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def fetch_top_tracks(time_range="medium_term", limit=20):
    print(f"🎧 Fetching user's top {limit} tracks over time range: {time_range}")
    sp = get_spotify_client()

    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    tracks = []

    fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for idx, item in enumerate(results['items']):
        try:
            duration_ms = item['duration_ms']
            tracks.append({
                'fetched_at': fetched_at,
                'rank': idx + 1,
                'track_name': item['name'],
                'artist': item['artists'][0]['name'],
                'album': item['album']['name'],
                'release_date': item['album']['release_date'],
                'popularity': item['popularity'],
                'duration_ms': duration_ms,
                'duration': format_duration(duration_ms),  # ✅ Human readable format
                'explicit': item['explicit'],
                'track_url': item['external_urls']['spotify'],
                'image_url': item['album']['images'][0]['url'] if item['album']['images'] else None,
                'album_type': item['album']['album_type'],
                'track_number': item['track_number'],
                'total_tracks_in_album': item['album']['total_tracks'],
                'artist_id': item['artists'][0]['id'],
                'album_id': item['album']['id'],
                'track_id': item['id']
            })
        except Exception as e:
            print(f"❌ Error parsing track '{item['name']}': {e}")
            continue

    df = pd.DataFrame(tracks)

    os.makedirs("data", exist_ok=True)
    df.to_excel("data/user_top_tracks.xlsx", index=False)

    print("✅ Top tracks saved: data/user_top_tracks.xlsx")
    return df

if __name__ == "__main__":
    fetch_top_tracks(time_range="short_term", limit=20)
