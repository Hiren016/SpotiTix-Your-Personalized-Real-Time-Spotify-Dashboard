# 🎧 SpotiTix — Your Personalized Real-Time Spotify Dashboard

🚀 **Live Dashboard Link:**  
[🔗 SpotiTix Dashboard (Power BI)](https://app.powerbi.com/view?r=eyJrIjoiNTY5Yjg2MDMtNmEzMi00OTVmLTlkYTUtMzg1NTc2ZGI3N2IzIiwidCI6ImQxZjE0MzQ4LWYxYjUtNGEwOS1hYzk5LTdlYmYyMTNjYmM4MSIsImMiOjEwfQ%3D%3D)

---

## 📝 Project Description

**SpotiTix** is a personalized real-time music analytics dashboard powered by Spotify’s API. Unlike Spotify Wrapped, which only shows your listening data at the end of the year, SpotiTix provides live, daily insights into your top tracks, favorite artists, playlist behavior, and more — all with vibrant visual storytelling and deep filtering capabilities.

---

## ❓ Problem Statement

Spotify Wrapped only arrives once a year — leaving users blind to their listening behavior during the rest of the year. Users cannot:

- 🔄 Monitor how their music tastes shift in real-time  
- 🎵 Track artist popularity or content-type trends  
- 🎧 View playlist composition or track duration preferences  

**SpotiTix solves this.** By providing a real-time Power BI dashboard, users can see how their music behavior evolves — with every stream.

---

## 🛠️ Technologies & Frameworks Used

| Tool / Platform             | Purpose                                              |
|-----------------------------|------------------------------------------------------|
| 🐍 Python                  | Backend scripting & ETL                              |
| 🎧 Spotify Developer App   | Auth & API access                                    |
| 📊 Power BI                | Dashboard & data visualization                       |
| ☁️ MongoDB Atlas           | Real-time NoSQL data storage                         |
| 🧪 Spotipy (Python SDK)    | Spotify Web API integration                          |
| 🧩 MongoDB BI Connector    | Connect MongoDB Atlas to Power BI                    |
| 📄 MS Excel                | Optional local data export                           |
| 🌐 HTML / JavaScript       | Frontend auth handling (for browser-based auth)      |

---

## 📈 Dashboard Visuals & Features

| Visual Type                  | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| 🖼️ **Image by CloudScope**    | Dynamic rendering of user/artist profile pictures                      |
| 📊 **Clustered Bar Chart**   | Top Tracks by Popularity + Artist Mapping                              |
| 🍩 **Donut Chart**           | Proportion of Explicit vs Non-Explicit Tracks                         |
| 📈 **Line Chart**            | Track Duration by Release Date (Recently Played)                      |
| 🥧 **Pie Chart**             | Artist Reach → Followers vs Popularity Slice                          |
| 📚 **Matrix Heatmap**        | New Album Releases → Album, Artist, Release Date                      |
| 📦 **Clustered Column Chart**| Playlist Breakdown → Dominant Artists, Albums, Album Types            |
| 🎛️ **Slicers + DAX**         | Toggle between time range, top N, explicit filters, etc.              |

---

## 📁 Project Structure

```bash
SpotiTix/
├── etl_spotify_to_mongo.py         # Main ETL orchestrator
├── spotify_auth.py                 # Spotify OAuth handling
├── get_top_tracks.py               # Extract top tracks
├── get_top_artists.py              # Extract top artists
├── get_recently_played_tracks.py   # Extract recent tracks
├── get_playlist_tracks.py          # Extract all user playlists
├── get_album_new_releases.py       # Extract new albums
├── mongo.py                        # MongoDB Atlas connector
├── .env                            # Environment variables for Spotify + MongoDB
├── data/                           # Folder for local Excel exports
├── PowerBI_SpotiTix.pbix           # Final dashboard file
└── README.md                       # You are here
```

---

## 🔧 Steps Followed

1. 🔐 **Spotify App Setup:** Registered app on Spotify Developer Dashboard, obtained credentials  
2. 🧪 **OAuth 2.0 Authentication:** Handled via Spotipy with local redirect and token caching  
3. 📥 **Data Collection:** Used Python scripts to fetch:  
   - User profile  
   - Top artists  
   - Top tracks  
   - Recently played tracks  
   - Playlist details  
   - New releases  
4. ☁️ **MongoDB Atlas:**  
   - Created cloud cluster  
   - Stored real-time Spotify data into collections  
5. 🔗 **MongoDB BI Connector:**  
   - Connected Power BI to Atlas using ODBC driver  
6. 🧼 **Data Transformation:**  
   - Flattened nested documents  
   - Converted durations to `HH:MM:SS`  
   - Cleaned missing/null values  
7. 📊 **Dashboard Development:**  
   - Built dynamic, slicer-driven dashboard in Power BI  
   - Applied Spotify's brand color palette and layout design  
8. 🔄 **ETL Automation:**  
   - Scripts run every 30 minutes using Python `schedule` module

---

## 🧠 Insights Extracted

- 🧑‍🎤 **Who are you listening to most — and how popular are they globally?**  
- ⏳ **What’s your attention span? Are your favorite tracks long or short?**  
- 🎵 **Which artists dominate your playlists or daily listening?**  
- 🚫 **How much of your content is explicit vs clean?**  
- 🆕 **What new albums have recently dropped in your listening space?**

---

## 🖼️ Theming & Branding

| Element         | Design Choice               |
|----------------|-----------------------------|
| Background      | `#191414` (Spotify Black)    |
| Accent Color    | `#1DB954` (Spotify Green)    |
| Highlights      | `#FFFFFF`, `#d63384`, `#ffce00` |
| Fonts & Layout  | Styled as Spotify's interface|
| Logos           | Spotify icon on top-left     |
| Header          | **SpotiTix** with subtitle: _“Real-Time Music Analytics”_ |

---

## 📸 Sample Screenshot

![SpotiTix](https://github.com/user/repo/assets/spotitix-screenshot.png)

---

## 🚀 Why Use SpotiTix?

- 🎯 See real-time changes in your listening behavior  
- 🎧 Get a personalized view of your favorite artists and tracks  
- 📈 Drill down into music trends using slicers and filters  
- 📊 Visually engaging dashboard with smart interactions  
- 🧠 Powered by analytics — built for music lovers  

---

## 🔗 Live Dashboard Link

👉 [Click to Launch Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNTY5Yjg2MDMtNmEzMi00OTVmLTlkYTUtMzg1NTc2ZGI3N2IzIiwidCI6ImQxZjE0MzQ4LWYxYjUtNGEwOS1hYzk5LTdlYmYyMTNjYmM4MSIsImMiOjEwfQ%3D%3D)

---

## 📧 Contact

| Field        | Details                                                   |
|--------------|-----------------------------------------------------------|
| **Author**   | Hiren Darji                                               |
| **Email**    | darjihiren850@gmail.com                                   |
| **LinkedIn** | [linkedin.com/in/hiren-darji31](https://linkedin.com/in/hiren-darji31) |

---

🚀 _Built with passion and technology!_

