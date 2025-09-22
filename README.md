Interactive Earthquake Map

A Python-based interactive web application to visualize real-time earthquake events worldwide using USGS data. Built with Python, Pandas, Folium, and Streamlit.

📌 Features

Fetches real-time earthquake data from the USGS API (past 7 days)

Cleans and processes earthquake data (CSV)

Generates interactive map using Folium:

Circle size proportional to earthquake magnitude

Color-coded by magnitude: Green (<4), Orange (4–6), Red (>6)

Popups show location, magnitude, depth, and time

Clustering of nearby earthquakes for a cleaner map

Streamlit web app:

Filters by minimum magnitude

Filter by location keyword

Download filtered CSV

Automated weekly data update using GitHub Actions

📂 Project Structure
earthquake-map/
│
├── data/
│   ├── earthquakes.csv          # Fetched earthquake data
│   └── earthquakes_map.html     # Generated Folium map (optional)
│
├── src/
│   ├── fetch_data.py            # Fetch earthquake data from USGS
│   ├── process_data.py          # Clean and prepare data
│   ├── generate_map.py          # Generate interactive map (with clustering)
│   └── app.py                   # Streamlit web app
│
├── .github/workflows/
│   └── update_earthquakes.yml  # Auto-update workflow
├── requirements.txt
└── README.md

⚙️ Setup

Clone the repository

git clone <your-repo-url>
cd earthquake-map


Create and activate virtual environment

python -m venv venv
# Windows CMD
venv\Scripts\activate
# PowerShell
.\venv\Scripts\Activate.ps1


Install dependencies

pip install -r requirements.txt


Fetch initial earthquake data

python src/fetch_data.py


Generate interactive HTML map (optional)

python src/generate_map.py


Run Streamlit web app locally

streamlit run src/app.py

🌐 Deployment
Streamlit Cloud (Free & Easy)

Push the repo to GitHub

Go to Streamlit Cloud
 → New App → Connect GitHub repo

Set Main file path: src/app.py

Deploy → You get a public link to share

📈 Automation: Auto-update Data

GitHub Actions workflow runs weekly:

Updates earthquakes.csv

Optionally updates earthquakes_map.html

Streamlit app always displays latest earthquake data

💻 Tech Stack

Python 3.11

Pandas → Data processing

Requests → Fetch USGS API

Folium → Interactive maps

Streamlit + streamlit-folium → Web interface

GitHub Actions → Automation