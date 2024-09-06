# 🌍 Air Quality Monitor on Map 🗺️

Welcome to **Air Quality Monitor on Map**! This Python-based desktop application allows users to monitor real-time air quality data for any location in the world 🌎. Just input your coordinates (latitude and longitude) and get real-time feedback on the air quality of that area, complete with a map and live data!

## 🚀 Features

- **Real-time Air Quality Data** 🏭: Get up-to-date air quality index (AQI) data for any location on Earth using the **IQAir API** 🌬️.
- **Interactive Map** 🗺️: See the location you’ve searched for on a fully interactive map powered by Folium.
- **Easy to Use** 👨‍💻: Just input the latitude and longitude, and hit "Get Air Quality"!
- **IQAir API Integration** 🔗: The app uses the **IQAir AirVisual API** for fetching air quality data. You can easily set up your API key!

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TeddyBb1/air-quality-monitor.git
   ```

2. **Install the required dependencies**:
   - Use `pip` to install the necessary libraries:
     ```bash
     pip install requests folium PySide6
     ```

3. **Get Your IQAir API Key** 🔑:
   - Sign up at [IQAir](https://www.iqair.com/air-pollution-api) and get your API key.

4. **Configure your API Key** 🔧:
   - Open the code and **replace** `your_iqair_api_key` with your **IQAir API key**.

   Example:
   ```python
   API_KEY = 'your_iqair_api_key'
   ```

5. **Run the application** 🖥️:
   - Run the Python script:
     ```bash
     python air.py
     ```
     or
     ```bash
     py air.py
     ```

6. **Enter coordinates** 🗺️:
   - Input the latitude and longitude to get live air quality data and see it on the map.

## 🧩 Project Structure

```bash
air-quality-monitor/
├── air.py             # Main application code
├── map.html           # HTML file for the map (generated automatically)
└── README.md          # Project documentation
```

## 📦 Requirements

- Python 3.8+
- Required libraries:
  - `requests`
  - `folium`
  - `PySide6`

## 🗺️ How it Works

1. **Input your coordinates** 🌐 (Latitude and Longitude).
2. **Fetch the air quality data** using the **IQAir API** 🌬️.
3. **View your selected location** on an interactive map 🗺️ with a marker and air quality details.

## 🛠️ Customization

- Feel free to customize the code if you wish to use a different air quality API, but this version is built specifically for **IQAir**.
- The app is designed to be modular and easy to expand.

## 🤝 Contributions

We welcome contributions! Please submit a pull request or create an issue for feature suggestions or bug reports.

## ⚠️ Disclaimer

Please note that you need to supply your own API key from **IQAir** to access the data.
