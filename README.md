# Real-Time Weather Monitoring System

## Description
This system fetches real-time weather data from the OpenWeatherMap API at regular intervals for metro cities in India (Delhi, Mumbai, Chennai, etc.). It processes the data to calculate daily weather summaries, such as average temperature, maximum/minimum temperature, and the dominant weather condition. The system also features an alerting mechanism for user-defined thresholds.

## Features
- Continuous weather data retrieval every 5 minutes for metro cities.
- Conversion of temperature from Kelvin to Celsius.
- Daily weather summaries including average, max, and min temperatures.
- Alerts for user-defined temperature thresholds (e.g., above 35°C).

## Technologies Used
- **Python 3.x**
- **SQLite3**: Database for storing weather data.
- **Requests**: For API calls to OpenWeatherMap.

## Setup Instructions

### Prerequisites:
1. **Python 3.x** installed on your system.
2. You need to sign up for an API key from [OpenWeatherMap](https://openweathermap.org/).

### Step-by-Step Setup:

1. **Clone the repository**:
   ```bash
   git clone  https://github.com/via23-ma/Weather_Monitoring.git
   cd weather-monitoring
2. **Install dependencies**:
   pip install requests
3. **Run the system**:
   python weather.py
4. **Run the alerting system: You can check for alerts by running**:
   python alerting.py

# Example Usage
- Fetches weather data for six cities every 5 minutes.
- Converts temperature from Kelvin to Celsius.
- Stores weather data in an SQLite database.

# Contribution
 Feel free to submit pull requests to improve the system.

# License
 Licensed under the MIT License.
 