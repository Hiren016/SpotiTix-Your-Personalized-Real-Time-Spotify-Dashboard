import pandas as pd
import os
from datetime import datetime
from spotify_auth import get_spotify_client

def get_new_album_releases(limit=20, offset=0, market="IN", output_file="data/new_album_releases.xlsx"):
    sp = get_spotify_client()
    
    print(f"🆕 Fetching new album releases... (limit={limit}, market={market})")

    response = sp.new_releases(limit=limit, offset=offset, country=market)
    albums = response['albums']['items']
    fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    album_data = []

    for album in albums:
        album_info = {
            'fetched_at': fetched_at,
            'album_name': album['name'],
            'album_type': album['album_type'],
            'artist': album['artists'][0]['name'] if album['artists'] else None,
            'release_date': album['release_date'],
            'total_tracks': album['total_tracks'],
            'spotify_url': album['external_urls']['spotify'],
            'image_url': album['images'][0]['url'] if album['images'] else None,
            'album_id': album['id']
        }
        album_data.append(album_info)

    df = pd.DataFrame(album_data)
    os.makedirs("data", exist_ok=True)
    df.to_excel(output_file, index=False)

    print(f"✅ Saved {len(df)} new album releases to: {output_file}")
    return df

if __name__ == "__main__":
    get_new_album_releases(limit=30)  # You can set 1–50 as needed
