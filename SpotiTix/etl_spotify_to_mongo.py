# etl_spotify_to_mongo.py

import pandas as pd
import os
from datetime import datetime
import schedule
import time
from mongo import get_mongo_collection
from get_user_profile import fetch_user_profile
from get_top_tracks import fetch_top_tracks
from get_top_artists import fetch_top_artists
from get_recently_played_tracks import fetch_recently_played_tracks
from get_playlist_tracks import fetch_all_playlists_and_tracks_combined
from get_album_new_releases import get_new_album_releases

def save_to_mongodb(df, collection_name, unique_keys=None):
    """
    Save data to MongoDB while avoiding duplicates using upsert.
    :param df: DataFrame to save
    :param collection_name: Name of MongoDB collection
    :param unique_keys: List of keys that uniquely identify each record
    """
    if df is None or df.empty:
        print(f"⚠️ Skipped empty DataFrame for {collection_name}")
        return

    collection = get_mongo_collection(collection_name)
    records = df.to_dict(orient="records")
    inserted, updated = 0, 0

    for record in records:
        # Skip records missing unique keys
        filter_query = {key: record.get(key) for key in unique_keys} if unique_keys else record
        if None in filter_query.values():
            print(f"⚠️ Skipped record due to missing key(s): {filter_query}")
            continue

        # 🟡 Optional Debug for user profile
        if collection_name == "user_profile":
            print("🔎 Inserting user profile with ID:", record.get("id"))

        # Perform upsert
        result = collection.update_one(filter_query, {"$set": record}, upsert=True)
        if result.upserted_id:
            inserted += 1
        else:
            updated += 1

    print(f"✅ {inserted} inserted, {updated} updated in collection: {collection_name}")


def run_etl():
    print("🚀 Starting real-time Spotify ETL")

    # USER PROFILE
    df_user = fetch_user_profile()
    save_to_mongodb(df_user, "user_profile", unique_keys=["id"])

    # TOP TRACKS
    df_tracks = fetch_top_tracks()
    save_to_mongodb(df_tracks, "top_tracks", unique_keys=["track_id"])

    # TOP ARTISTS
    df_artists = fetch_top_artists()
    save_to_mongodb(df_artists, "top_artists", unique_keys=["artist_id"])

    # RECENTLY PLAYED
    df_recent = fetch_recently_played_tracks()
    save_to_mongodb(df_recent, "recently_played", unique_keys=["track_id", "played_at"])

    # NEW RELEASES
    df_new = get_new_album_releases()
    save_to_mongodb(df_new, "new_releases", unique_keys=["album_id"])

    # PLAYLIST TRACKS (Excel + Mongo)
    df_playlists = fetch_all_playlists_and_tracks_combined()
    save_to_mongodb(df_playlists, "playlist_tracks", unique_keys=["track_id", "playlist_id"])

    print("🎉 ETL complete.")

# ⏰ Schedule the ETL job to run every 30 minutes
schedule.every(30).minutes.do(run_etl)

print("⏰ Real-time ETL Scheduler running every 30 minutes...\n")
run_etl()  # Run immediately once

while True:
    schedule.run_pending()
    time.sleep(1)
