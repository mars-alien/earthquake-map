import requests
import pandas as pd
from datetime import datetime
import os

# Build path relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "earthquakes.csv")

# USGS API endpoint: Past 7 days of earthquakes
USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

def fetch_earthquake_data():
    """Fetch earthquake data from USGS API and save to CSV"""
    try:
        response = requests.get(USGS_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

    # Extract useful info
    records = []
    for feature in data["features"]:
        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]

        record = {
            "magnitude": props.get("mag"),
            "place": props.get("place"),
            "time": datetime.utcfromtimestamp(props.get("time") / 1000).strftime("%Y-%m-%d %H:%M:%S"),
            "longitude": coords[0],
            "latitude": coords[1],
            "depth": coords[2],
        }
        records.append(record)

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Ensure data folder exists
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(CSV_PATH, index=False)
    print(f" Saved {len(df)} earthquake records to {CSV_PATH}")
    return df

if __name__ == "__main__":
    fetch_earthquake_data()
