from spotify_auth import app

if __name__ == "__main__":
    print("🌐 Starting SpotiTix Auth Server at http://127.0.0.1:8888")
    print("📢 Open in browser and approve Spotify access.")
    app.run(host="127.0.0.1", port=8888)
