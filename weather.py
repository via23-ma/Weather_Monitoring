import requests
import time
import sqlite3
from datetime import datetime

API_KEY = "e2195b794aa9656bc2d72d1a9625fc43"
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # Fetch weather data every 5 minutes

# Function to get weather data from OpenWeatherMap API
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(temp_kelvin):
    return round(temp_kelvin - 273.15, 2)

# Function to process weather data
def process_weather_data(city_data):
    temp = kelvin_to_celsius(city_data['main']['temp'])
    feels_like = kelvin_to_celsius(city_data['main']['feels_like'])
    condition = city_data['weather'][0]['main']
    timestamp = city_data['dt']
    return {
        'city': city_data['name'],
        'temp': temp,
        'feels_like': feels_like,
        'condition': condition,
        'timestamp': datetime.fromtimestamp(timestamp)
    }

# Function to save weather data in SQLite
def save_to_database(data):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                      (city TEXT, temp REAL, feels_like REAL, condition TEXT, timestamp TEXT)''')
    cursor.execute("INSERT INTO weather (city, temp, feels_like, condition, timestamp) VALUES (?, ?, ?, ?, ?)",
                   (data['city'], data['temp'], data['feels_like'], data['condition'], data['timestamp']))
    conn.commit()
    conn.close()

# Main function to run the weather monitoring system
def run_weather_monitoring():
    while True:
        for city in CITIES:
            city_data = get_weather_data(city)
            if city_data:
                processed_data = process_weather_data(city_data)
                save_to_database(processed_data)
                print(f"Weather data for {city} saved at {processed_data['timestamp']}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run_weather_monitoring()
