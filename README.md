# Interactive Earthquake Map

This project creates an **interactive map of earthquakes** using **Python, Folium, Pandas, and Streamlit**.  

## Features
- Fetches **real-time earthquake data** from the **USGS API** weekly
- Generates an **interactive map** with:
  - Circle markers sized by magnitude
  - Color-coded by magnitude (green/orange/red)
  - Popup info for location, magnitude, depth, and time
- Allows **user filters**:
  - Minimum magnitude
  - Search by location
- Option to **download filtered CSV**
- **Auto-updated weekly** using GitHub Actions

## Project Structure
See the `src/` folder for all Python code.

## Deployment
- Deployed on **[Streamlit Cloud](https://share.streamlit.io/)**  
- Auto-updates every Sunday via **GitHub Actions workflow**

## How to Run Locally
1. Clone repo: `git clone https://github.com/<your-username>/earthquake-map.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run Streamlit app: `streamlit run src/app.py`
