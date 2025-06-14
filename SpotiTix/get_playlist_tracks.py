from spotify_auth import get_spotify_client
import pandas as pd
import os
from datetime import datetime
import re

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def format_duration(ms):
    seconds = ms // 1000
    minutes = (seconds // 60) % 60
    hours = seconds // 3600
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def fetch_all_playlists():
    sp = get_spotify_client()
    print("🎧 Fetching current user's playlists...")

    playlists = []
    results = sp.current_user_playlists(limit=50)
    while results:
        playlists.extend(results['items'])
        results = sp.next(results) if results['next'] else None

    print(f"📋 Found {len(playlists)} playlists.")
    return playlists

def fetch_tracks_from_playlist(sp, playlist):
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    playlist_owner = playlist['owner']['display_name']
    total_tracks = playlist['tracks']['total']
    fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n▶️ Fetching: {playlist_name} by {playlist_owner} | {total_tracks} tracks")

    tracks = []
    results = sp.playlist_tracks(playlist_id, limit=50)
    while results:
        for item in results['items']:
            track = item['track']
            if not track:
                continue
            try:
                duration_ms = track['duration_ms']
                duration = format_duration(duration_ms)

                tracks.append({
                    'fetched_at': fetched_at,
                    'playlist_name': playlist_name,
                    'playlist_id': playlist_id,
                    'track_name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'album': track['album']['name'],
                    'release_date': track['album']['release_date'],
                    'popularity': track['popularity'],
                    'duration_ms': duration_ms,
                    'duration': duration,  # ✅ Human-readable
                    'explicit': track['explicit'],
                    'track_url': track['external_urls']['spotify'],
                    'image_url': track['album']['images'][0]['url'] if track['album']['images'] else None,
                    'album_type': track['album']['album_type'],
                    'track_number': track['track_number'],
                    'total_tracks_in_album': track['album']['total_tracks'],
                    'artist_id': track['artists'][0]['id'],
                    'album_id': track['album']['id'],
                    'track_id': track['id'],
                    'added_at': item['added_at'],
                    'added_by': item['added_by']['id'] if item.get('added_by') else None
                })
            except Exception as e:
                print(f"❌ Error parsing a track: {e}")
                continue
        results = sp.next(results) if results['next'] else None

    return tracks

def save_playlist_to_excel(tracks, playlist_name):
    df = pd.DataFrame(tracks)
    os.makedirs("data", exist_ok=True)
    safe_name = sanitize_filename(playlist_name)
    filename = f"data/playlist_{safe_name}.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Saved: {filename}")

def fetch_all_playlists_and_tracks_combined():
    """Main entry point: returns all playlists' tracks as a single DataFrame."""
    sp = get_spotify_client()
    playlists = fetch_all_playlists()
    all_tracks = []

    for playlist in playlists:
        tracks = fetch_tracks_from_playlist(sp, playlist)
        if tracks:
            save_playlist_to_excel(tracks, playlist['name'])  # Save Excel
            all_tracks.extend(tracks)  # Add to final Mongo collection

    return pd.DataFrame(all_tracks)
