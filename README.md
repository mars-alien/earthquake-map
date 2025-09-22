Earthquake Map Auto-Updater

An interactive earthquake visualization dashboard that automatically updates with the latest real-time earthquake data from USGS.
Built with Python, Pandas, Folium, Streamlit, and GitHub Actions, this project combines data engineering, visualization, and automation to create a powerful geo-analytics tool.

🔗 Live Demo
 |
💻 Source Code

✨ Features

📡 Real-Time Data Updates – Earthquake data auto-fetched and refreshed daily via GitHub Actions.

🗺️ Interactive World Map – Explore earthquakes on an interactive Leaflet map powered by Folium.

🎚️ Smart Filters – Filter by minimum magnitude or location for custom insights.

📊 Clustered Visualization – Earthquakes grouped by region and intensity, with intuitive color-coding.

📥 CSV Export – Download filtered earthquake datasets for further analysis.

🌙 Modern UI/UX – Clean, dark-themed dashboard built with Streamlit for smooth user interaction.

🛠️ Tech Stack

Languages: Python

Libraries: Pandas, Folium, Streamlit

Automation: GitHub Actions (auto-updates data pipeline)

Visualization: Leaflet (via Folium), Streamlit components

Deployment: Streamlit Cloud

💡 These tools are highly relevant for Data Science & Software Engineering internships, showcasing skills in:

Data Processing (Pandas, APIs)

Automation/CI-CD (GitHub Actions)

Interactive Dashboards (Streamlit, Folium)

Geospatial Visualization (Leaflet, Clustering)

📸 Screenshots
🔎 Filters + Map

📊 Interactive Clusters

(Include another screenshot focusing on zoomed-in clusters)

⚙️ Installation & Usage

Clone repository

git clone https://github.com/mars-alien/react-portfolio.git
cd earthquake-map


Create virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run src/app.py


Open http://localhost:8501 in your browser 🚀

🔄 Automated Data Updates

This project uses GitHub Actions to:

Fetch latest earthquake data from USGS API daily

Clean and preprocess data with Pandas

Push updates to GitHub repository

Automatically refresh the Streamlit app

This ensures the map always shows the most recent earthquake activity worldwide 🌍

📂 Project Structure
earthquake-map/
│
├── src/
│   ├── app.py              # Main Streamlit app
│   ├── process_data.py     # Data loading & cleaning
│   ├── visualize.py        # Folium map generation
│
├── .github/
│   └── workflows/
│       └── update-data.yml # GitHub Actions automation
│
├── requirements.txt
├── README.md
└── assets/ (screenshots)
