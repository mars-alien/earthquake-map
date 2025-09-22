import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "earthquakes.csv")

def load_and_clean_data():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")
    df = pd.read_csv(CSV_PATH)
    df = df.rename(columns={
        "latitude": "latitude",
        "longitude": "longitude",
        "mag": "magnitude",
        "place": "place",
        "depth": "depth",
        "time": "time"
    })
    df = df[["latitude", "longitude", "magnitude", "depth", "place", "time"]]
    df = df.dropna(subset=["latitude", "longitude", "magnitude"])
    return df
