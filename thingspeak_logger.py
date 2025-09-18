import requests
import random
import time

API_KEY = "MZP0W73EOOV41XYC"  # Replace with your ThingSpeak Write API Key
URL = "https://api.thingspeak.com/update"

def send_data():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 60.0), 2)
    
    payload = {
        'api_key': API_KEY,
        'field1': temperature,
        'field2': humidity
    }
    
    response = requests.post(URL, data=payload)
    
    if response.status_code == 200 and response.text != '0':
        print(f"Data sent successfully: Temp={temperature}°C, Humidity={humidity}%")
    else:
        print("Failed to send data")

if __name__ == "__main__":
    while True:
        send_data()
        time.sleep(15)
