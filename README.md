# 🌍 Earthquake Map Project

An interactive web application that visualizes real-time earthquake data on a map, built with **Python**, **Streamlit**, and **Folium**.

---

### ✨ Features
* **Interactive Map**: Explore recent earthquake data with zoom and pan functionality.
* **Automated Data Updates**: The application automatically fetches and processes the latest data using GitHub Actions.
* **User-Friendly Interface**: A simple and clean web interface for easy data exploration.


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


