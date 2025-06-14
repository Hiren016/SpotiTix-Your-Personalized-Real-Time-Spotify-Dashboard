from spotify_auth import get_spotify_client
import pandas as pd
import os

def fetch_top_artists(time_range="medium_term", limit=20):
    print(f"🎧 Fetching user's top {limit} artists over time range: {time_range}")

    sp = get_spotify_client()
    results = sp.current_user_top_artists(time_range=time_range, limit=limit)
    artists = []

    for idx, item in enumerate(results['items']):
        artists.append({
            'rank': idx + 1,
            'artist_id': item['id'],  # ✅ required for MongoDB upsert
            'name': item['name'],
            'genres': ", ".join(item['genres']),
            'popularity': item['popularity'],
            'followers': item['followers']['total'],
            'spotify_url': item['external_urls']['spotify'],
            'image_url': item['images'][0]['url'] if item['images'] else None
        })

    df = pd.DataFrame(artists)
    os.makedirs("data", exist_ok=True)
    df.to_excel("data/user_top_artists.xlsx", index=False)

    print("✅ Top artists saved to: data/user_top_artists.xlsx")
    return df

if __name__ == "__main__":
    fetch_top_artists(time_range="medium_term", limit=20)
