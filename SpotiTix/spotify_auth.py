# spotify_auth.py

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from flask import Flask, request, redirect, render_template_string

# Load environment variables
load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI", "http://127.0.0.1:8888/callback")

scope = "user-top-read user-read-private user-read-email user-read-recently-played playlist-read-private playlist-read-collaborative"

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    cache_path=".cache",
    show_dialog=True
)

app = Flask(__name__)
user_info = {}  # Will hold Spotify user data

@app.route("/")
def home():
    return render_template_string("""
    <html>
    <body style="background:#191414; color:white; font-family:sans-serif; text-align:center; padding-top:150px;">
        <h1 style="color:#1DB954;">Welcome to SpotiTix 🎶</h1>
        <p style="font-size:18px;">Your personalized Spotify Audio Story awaits</p>
        <a href="/authorize">
            <button style="
              padding: 14px 28px;
              font-size: 18px;
              color: #ffffff;
              background-color: #1DB954;
              border: none;
              border-radius: 30px;
              cursor: pointer;
              transition: all 0.3s ease;
              font-weight: 600;
              margin-top: 40px;
              box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);">
              🔐 Login with Spotify
            </button>
        </a>
        <style>
            button:hover {
                background-color: #1ed760;
                transform: scale(1.05);
            }
        </style>
    </body>
    </html>
    """)

@app.route("/authorize")
def authorize():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_info = sp_oauth.get_access_token(code, as_dict=True)
    sp = spotipy.Spotify(auth=token_info["access_token"])

    user = sp.current_user()
    user_info['id'] = user["id"]
    user_info['display_name'] = user.get("display_name", "Spotify User")

    return render_template_string("""
    <html>
    <body style="background:#191414; color:#fff; font-family:sans-serif; text-align:center; padding-top:100px;">
        <h1 style="color:#1DB954;">🎉 Connected To SpotiTix Successfully!</h1>
        <p>Welcome <b>{{ name }}</b> 👋</p>
        <a href="/dashboard">
            <button style="
              padding: 12px 24px;
              font-size: 16px;
              color: #ffffff;
              background-color: #1DB954;
              border: none;
              border-radius: 30px;
              cursor: pointer;
              transition: all 0.3s ease;
              font-weight: 600;
              box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            ">🚀 Generate My Dashboard</button>
        </a>
        <style>
          button:hover {
            background-color: #1ed760;
            transform: scale(1.05);
          }
        </style>
    </body>
    </html>
    """, name=user_info['display_name'])

@app.route("/dashboard")
def dashboard():
    if not user_info:
        return redirect("/")

    user_id = user_info["id"]
    display_name = user_info["display_name"]

    return render_template_string(f"""
    <html>
    <body style="background:#191414; color:white; font-family:sans-serif; text-align:center; margin:0; padding:0;">
        <h2 style="padding: 30px 0; font-size: 26px; color:#1DB954;">🎯 {display_name}, your dashboard is ready!</h2>
        <iframe 
            width="900" 
            height="600" 
            src="https://app.powerbi.com/view?r=eyJrIjoiNTY5Yjg2MDMtNmEzMi00OTVmLTlkYTUtMzg1NTc2ZGI3N2IzIiwidCI6ImQxZjE0MzQ4LWYxYjUtNGEwOS1hYzk5LTdlYmYyMTNjYmM4MSIsImMiOjEwfQ%3D%3D&filter=user_profile/id eq '{user_id}'"
            frameborder="0" 
            style="border: none;" 
            allowFullScreen="true">
        </iframe>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(port=8888, debug=True)
