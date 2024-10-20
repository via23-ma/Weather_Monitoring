import sqlite3

THRESHOLD_TEMP = 35  # Alert threshold temperature in Celsius

# Function to check for temperature thresholds in the database
def check_for_alerts():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT city, temp, timestamp FROM weather WHERE temp > ?", (THRESHOLD_TEMP,))
    results = cursor.fetchall()
    conn.close()
    if results:
        for result in results:
            print(f"Alert! High temperature in {result[0]}: {result[1]}°C at {result[2]}")
    else:  
      print("No alerts found.")

if __name__ == "__main__":
    check_for_alerts()

