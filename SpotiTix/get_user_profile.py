from spotify_auth import get_spotify_client
import pandas as pd
import os

def fetch_user_profile():
    print("👤 Fetching user profile...")

    sp = get_spotify_client()
    user = sp.current_user()

    profile_data = {
        "display_name": user.get("display_name"),
        "email": user.get("email"),
        "country": user.get("country"),
        "product": user.get("product"),
        "id": user.get("id"),
        "followers": user.get("followers", {}).get("total"),
        "profile_url": user.get("external_urls", {}).get("spotify"),
        "image_url": user["images"][0]["url"] if user.get("images") else None
    }

    df = pd.DataFrame([profile_data])
    os.makedirs("data", exist_ok=True)
    df.to_excel("data/user_profile.xlsx", index=False)

    print("✅ User profile saved to: data/user_profile.xlsx")
    return df  # 🟢 REQUIRED: return this so ETL can use it

if __name__ == "__main__":
    fetch_user_profile()
