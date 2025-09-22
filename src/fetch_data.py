import requests
import pandas as pd
import os

# Create data folder if not exists
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
CSV_PATH = os.path.join(DATA_DIR, "earthquakes.csv")

# USGS API for past 7 days
URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv"

def fetch_earthquake_data():
    r = requests.get(URL)
    r.raise_for_status()
    with open(CSV_PATH, "wb") as f:
        f.write(r.content)
    print(f"Earthquake data saved: {CSV_PATH}")

if __name__ == "__main__":
    fetch_earthquake_data()
