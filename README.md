# 🚀 Power BI × Spotify Dashboard

A deep dive into public Spotify listening history, engineered into a dynamic and interactive Power BI dashboard. This project wasn't just about playing with data—it was about building a secure, scalable, and seriously cool pipeline that transforms raw audio streams into an elegant visual symphony.


<p align="left">
  <img src="Spotify Dashboard.png" alt="Spotify Dashboard" width="400"/>
</p>



## 🔐 OAuth 2.0 Flow: Secure Auth Like a Pro

* Registered a Spotify Developer App and implemented the **Authorization Code Flow** using **Flask** in Python.
* Created a secure local server using **ngrok** to handle the redirect URI.
* Fetched **user-specific data** via access tokens and managed automatic refresh tokens for continuous access.

## 🚀 API Wizardry: Enriching the Raw Stream

* Used **Client Credentials Flow** to access public endpoints for audio features, genres, and popularity metrics.
* Cleaned and enriched track data with:

  * Audio features: tempo, danceability, energy, etc.
  * Metadata: track name, artist, album art, playlist context
  * Custom engineered fields like decade bins and mood tags

## 🌟 Power BI Magic: Data Meets Storytelling

* Imported the cleaned dataset into **Power BI Desktop**.
* Designed interactive visuals including:

  * Top artists over time
  * Listening heatmaps by hour & day
  * Genre clouds and track popularity charts
  * Energy vs. danceability scatter plots with album art tooltips
* Enabled filters, drilldowns, bookmarks, and dynamic tooltips for next-level UX.


## 🏋️ Tech Stack

```text
Languages: Python (Flask, requests, pandas)
APIs: Spotify Web API (OAuth 2.0 + Client Credentials)
Tools: ngrok, Power BI Desktop, Power BI Service
```


### 🔹 Project Outcome

* Personalized, secure, and visually stunning Spotify dashboard
* Enhanced skillset in API auth flows, REST APIs, data wrangling, and dashboard design
* A portable, reproducible project that could be adapted for any API-powered analytics

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

### 🛍️ Wanna Talk Data x Music?

Connect with me if you're a fellow data nerd, music geek, or someone who appreciates turning "Top 50 Sri Lanka" into something... legendary. 😉


