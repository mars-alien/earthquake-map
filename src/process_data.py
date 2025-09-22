import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "earthquakes.csv")

def load_and_clean_data(csv_path=CSV_PATH):
    """Load earthquake CSV and clean data"""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f" CSV file not found at {csv_path}. Run fetch_data.py first.")

    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["magnitude", "latitude", "longitude", "place"])

    df["magnitude"] = df["magnitude"].astype(float)
    df["latitude"] = df["latitude"].astype(float)
    df["longitude"] = df["longitude"].astype(float)
    df["latitude"] = df["latitude"].round(4)
    df["longitude"] = df["longitude"].round(4)

    df = df.sort_values(by="magnitude", ascending=False).reset_index(drop=True)
    print(f"Cleaned data: {len(df)} records ready for mapping")
    return df

if __name__ == "__main__":
    df = load_and_clean_data()
    print(df.head())
