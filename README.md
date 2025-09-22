# 🌍 Interactive Earthquake Map

An interactive web application built with **Streamlit**, **Folium**, and the **USGS Earthquake API**.  
This project visualizes recent earthquakes worldwide, allowing users to **filter by magnitude** and **search locations**, with dynamic clustering on a map.  

---

## 📸 Screenshots

### Filters + Map
![Earthquake Map](./assets/screenshot.png)

---

## ✨ Features

- ✅ **Real-time Data** – Fetches earthquake data directly from [USGS Earthquake API](https://earthquake.usgs.gov/).
- ✅ **Interactive Map** – Explore earthquakes on a Folium map with zoom & pan.
- ✅ **Magnitude Filters** – Adjust minimum magnitude dynamically.
- ✅ **Search by Location** – Quickly locate earthquakes near a place.
- ✅ **Marker Clustering** – Group nearby earthquakes for better visualization.
- ✅ **CSV Export** – Download filtered earthquake data for offline use.
- ✅ **Deployment Ready** – Works locally and deploys smoothly on Streamlit Cloud.

---

## 📂 Project Structure

earthquake-map/
│
├── src/
│   ├── app.py              # Main Streamlit app
│   ├── process_data.py     # Data loading & cleaning
│   ├── generate_map.py        # Folium map generation
|   ├── fetch_data.py    # Fetch the data
│
├── .github/
│   └── workflows/
│       └── update-data.yml # GitHub Actions automation
│
├── requirements.txt
├── README.md




---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/earthquake-map.git
cd earthquake-map
2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Fetch latest earthquake data
python src/fetch_data.py

4️⃣ Run the Streamlit app
streamlit run src/app.py

🔧 Configuration

Data Source: USGS "All Earthquakes, Past 7 Days" feed
→ CSV Feed Link

Output Files:

data/earthquakes.csv → raw data

outputs/earthquakes_map.html → static map export

📦 Deployment

This project is ready to deploy on:

Streamlit Cloud (1-click deploy)

Heroku / Render (with requirements.txt)

Docker (optional: build a container for deployment)

Example for Streamlit Cloud:

Push repo to GitHub

Go to Streamlit Cloud

Create new app → point to src/app.py

🤝 Contributing

Pull requests are welcome!
If you’d like to contribute, please fork the repo and create a new branch:

git checkout -b feature/new-feature
git commit -m "Added new feature"
git push origin feature/new-feature

📜 License

This project is licensed under the MIT License – feel free to use, modify, and distribute.


