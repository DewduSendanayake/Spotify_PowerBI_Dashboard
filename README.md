# Spotify Data Dashboard with Power BI 🎧

Welcome to a curated journey through Spotify's most streamed tracks — visualized, analyzed, and reimagined. This interactive Power BI dashboard turns a static dataset into a compelling story of global music trends up to 2023.

<p align="center">
  <img src="Spotify Dashboard.png" alt="Spotify Dashboard" width="800"/>
</p>


## 🔐 Secure Access via OAuth 2.0: Built for Privacy

* Registered a Spotify Developer App and implemented **Authorization Code Flow** with **Flask** in Python.
* Created a secure local server using **ngrok** to manage the OAuth 2.0 redirect URI.
* Fetched user-specific listening data using **access tokens**, and ensured seamless re-authentication with **refresh tokens**.


## 🔍 Data Enrichment through Spotify Web API

* Accessed **public endpoints** with **Client Credentials Flow** to fetch audio features and metadata.
* Extracted and engineered features:

  * Acoustic attributes: *danceability, energy, tempo, valence, etc.*
  * Metadata: *track names, artists, genres, album art, playlist source*
  * Custom fields: *decade bins, mood tags, stream ranks*


## 📊 Power BI Visualization Highlights

Transformed the enriched dataset into an interactive experience in **Power BI Desktop**, with visuals that speak louder than words:

* 🎤 **Top Artists Timeline**: Trend analysis across years
* 🔥 **Energy × Danceability**: Interactive scatter with album art tooltips
* ⏱️ **Listening Patterns**: Hourly + weekly heatmaps
* 🎧 **Genre Distribution**: Word clouds & popularity scores
* 📌 Enhanced UX: Filters, drill-throughs, dynamic bookmarks, and hover cards



## 🛠️ Tech Stack & Tools

```text
Languages: Python (Flask, requests, pandas)
APIs: Spotify Web API (OAuth 2.0 & Client Credentials Flow)
Dashboard: Power BI Desktop, Power BI Service
Other Tools: ngrok, HTML for embedding visuals
```



## 🎯 Project Outcomes

* Developed a secure, scalable pipeline from Spotify's API to Power BI
* Designed a personalized, interactive dashboard that reveals insights from 1,000+ globally streamed tracks
* Boosted dashboard development and user engagement skills through storytelling and design



## 📄 License

Released under the [MIT License](LICENSE). Free to remix, reuse, and reimagine. Into analytics, music, or visual storytelling? Let’s collaborate.

> "Music gives a soul to the universe, wings to the mind, flight to the imagination, and life to everything." – Plato



