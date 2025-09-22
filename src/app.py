import streamlit as st
from streamlit_folium import st_folium
from process_data import load_and_clean_data
import folium
from folium.plugins import MarkerCluster

def get_color(magnitude):
    if magnitude < 4.0:
        return "green"
    elif 4.0 <= magnitude < 6.0:
        return "orange"
    else:
        return "red"

# Sidebar filters
st.sidebar.header("Filters")
min_magnitude = st.sidebar.slider("Minimum Magnitude", 0.0, 10.0, 0.0, 0.1)
search_location = st.sidebar.text_input("Search Location")

# Load and filter data
df = load_and_clean_data()
filtered_df = df[df["magnitude"] >= min_magnitude]

if search_location:
    filtered_df = filtered_df[filtered_df["place"].str.contains(search_location, case=False, na=False)]

st.title("Interactive Earthquake Map")
st.write(f"Showing {len(filtered_df)} earthquakes")

# Create Folium map dynamically
earthquake_map = folium.Map(location=[20,0], zoom_start=2, tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(earthquake_map)

for _, row in filtered_df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=row["magnitude"]*2,
        color=get_color(row["magnitude"]),
        fill=True,
        fill_color=get_color(row["magnitude"]),
        fill_opacity=0.7,
        popup=folium.Popup(
            f"<b>Location:</b> {row['place']}<br>"
            f"<b>Magnitude:</b> {row['magnitude']}<br>"
            f"<b>Depth:</b> {row['depth']} km<br>"
            f"<b>Time:</b> {row['time']}",
            max_width=300
        )
    ).add_to(marker_cluster)

st_folium(earthquake_map, width=1000, height=600)

# CSV download
st.sidebar.download_button(
    label="Download filtered CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name="filtered_earthquakes.csv",
    mime="text/csv"
)
