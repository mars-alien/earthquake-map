import folium
from folium.plugins import MarkerCluster
import os
from process_data import load_and_clean_data

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")   # New folder outside repo for HTML
os.makedirs(OUTPUT_DIR, exist_ok=True)          # Ensure folder exists
OUTPUT_HTML = os.path.join(OUTPUT_DIR, "earthquakes_map.html")

# Function to get color by magnitude
def get_color(magnitude):
    if magnitude < 4.0:
        return "green"
    elif 4.0 <= magnitude < 6.0:
        return "orange"
    else:
        return "red"

# Create the map
def create_map():
    df = load_and_clean_data()

    earthquake_map = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(earthquake_map)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=row["magnitude"] * 2,
            color=get_color(row["magnitude"]),
            fill=True,
            fill_color=get_color(row["magnitude"]),
            fill_opacity=0.7,
            popup=folium.Popup(
                f"<b>Location:</b> {row['place']}<br>"
                f"<b>Magnitude:</b> {row['magnitude']}<br>"
                f"<b>Depth:</b> {row['depth']} km<br>"
                f"<b>Time:</b> {row['time']}",
                max_width=300,
            )
        ).add_to(marker_cluster)

    earthquake_map.save(OUTPUT_HTML)
    print(f"Clustered map created: {OUTPUT_HTML}")

if __name__ == "__main__":
    create_map()
