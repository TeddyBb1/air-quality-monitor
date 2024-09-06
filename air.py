import sys
import os
import requests
import folium
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QLineEdit
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import http.server
import socketserver
import threading

# API key for IQAir
API_KEY = 'your_iqair_api_key'
BASE_URL = 'http://api.airvisual.com/v2/nearest_city'
PORT = 8000  # Port on which the local HTTP server will run


class AirQualityMapApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Air Quality Monitoring on Map')
        self.setGeometry(300, 300, 800, 600)

        # Input fields for coordinates
        self.lat_input = QLineEdit(self)
        self.lat_input.setPlaceholderText("Latitude")
        self.lon_input = QLineEdit(self)
        self.lon_input.setPlaceholderText("Longitude")

        # Label to display air quality data
        self.result_label = QLabel('Air quality will appear here.', self)

        # Button to update air quality and map
        self.update_button = QPushButton('Get Air Quality', self)
        self.update_button.clicked.connect(self.get_air_quality_and_update_map)

        # Layout for the coordinate inputs
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.lat_input)
        input_layout.addWidget(self.lon_input)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)

        # Create an initial map centered on a specific location
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        layout.addWidget(self.update_button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Start the local server and load the initial map
        self.start_local_server()
        self.update_map(45.9432, 24.9668)  # Initially, center the map on Romania

    def start_local_server(self):
        """Start a local HTTP server to serve the HTML file."""
        handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", PORT), handler)

        # Run the server in a separate thread so it doesn't block the application
        server_thread = threading.Thread(target=self.httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()

    def update_map(self, lat, lon):
        """Update the map and add a marker at the specified coordinates."""
        # Generate a map centered on the new coordinates
        self.map = folium.Map(location=[lat, lon], zoom_start=6)

        # Add a marker at the new coordinates
        folium.Marker([lat, lon], popup="Selected location").add_to(self.map)

        # Save the map to an HTML file
        self.map.save("map.html")

        # Reload the map in QWebEngineView
        self.web_view.setUrl(QUrl(f"http://localhost:{PORT}/map.html"))

    def get_air_quality_and_update_map(self):
        """Fetch air quality data and update the map."""
        # Get the coordinates entered by the user
        try:
            lat = float(self.lat_input.text().strip())  # Strip spaces and convert to float
            lon = float(self.lon_input.text().strip())
        except ValueError:
            self.result_label.setText("Invalid coordinates entered. Make sure they are valid numbers.")
            return

        # Check if the latitude and longitude are within valid ranges
        if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
            self.result_label.setText("Latitude must be between -90 and 90, and longitude between -180 and 180.")
            return

        # Update the map and add a marker at the new coordinates
        self.update_map(lat, lon)

        # Construct the URL for the IQAir API
        url = f'{BASE_URL}?lat={lat}&lon={lon}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Debugging: Display the data returned by the API
        print(data)

        # Check if data is available and display the result
        if 'data' in data:
            aqi = data['data']['current']['pollution']['aqius']
            self.display_air_quality(aqi)
        else:
            self.result_label.setText("Error retrieving data.")

    def display_air_quality(self, aqi):
        """Display the air quality based on the AQI index."""
        if aqi <= 50:
            self.result_label.setText(f"Air quality: Good (AQI: {aqi})")
        elif aqi <= 100:
            self.result_label.setText(f"Air quality: Moderate (AQI: {aqi})")
        elif aqi <= 150:
            self.result_label.setText(f"Air quality: Unhealthy for sensitive groups (AQI: {aqi})")
        elif aqi <= 200:
            self.result_label.setText(f"Air quality: Unhealthy (AQI: {aqi})")
        elif aqi <= 300:
            self.result_label.setText(f"Air quality: Very unhealthy (AQI: {aqi})")
        else:
            self.result_label.setText(f"Air quality: Hazardous (AQI: {aqi})")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AirQualityMapApp()
    window.show()
    sys.exit(app.exec())
