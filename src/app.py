# src/app.py

import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
from process_data import load_and_clean_data
from generate_map import get_color

st.set_page_config(page_title="🌍 Earthquake Map", layout="wide")
st.title("🌍 Interactive Earthquake Map")
st.markdown("Real-time earthquake data from the **USGS API** (past 7 days).")

df = load_and_clean_data()

# Sidebar filters
st.sidebar.header("🔎 Filters")
min_mag = st.sidebar.slider(
    "Minimum Magnitude",
    min_value=float(df["magnitude"].min()),
    max_value=float(df["magnitude"].max()),
    value=2.5,
    step=0.1
)
region_keyword = st.sidebar.text_input("Filter by Location Keyword", "")

# Filter data
filtered_df = df[df["magnitude"] >= min_mag]
if region_keyword:
    filtered_df = filtered_df[filtered_df["place"].str.contains(region_keyword, case=False, na=False)]
st.sidebar.markdown(f"**Showing {len(filtered_df)} earthquakes**")

# Folium map
earthquake_map = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(earthquake_map)

for _, row in filtered_df.iterrows():
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

st_folium(earthquake_map, width=1200, height=600)

# CSV download
st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_earthquakes.csv",
    mime="text/csv"
)
