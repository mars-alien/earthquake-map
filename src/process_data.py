import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "earthquakes.csv")

def load_and_clean_data():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)

    
    # Flexible rename map (only apply if column exists)
    rename_map = {
        "mag": "magnitude",
        "magnitude": "magnitude",   # in case it's already named this
        "place": "place",
        "latitude": "latitude",
        "longitude": "longitude",
        "depth": "depth",
        "time": "time"
    }

    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    # Ensure required columns exist
    required_cols = ["latitude", "longitude", "magnitude", "depth", "place", "time"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = None  # create empty if missing

    # Select only required columns
    df = df[required_cols]

    # Drop rows missing critical fields
    df = df.dropna(subset=["latitude", "longitude", "magnitude"])

    return df
