import requests

API_KEY = "26af2d7dc275b0574a7b791b0c7bd820"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "APPID": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\nWeather Information")
    print(f"City: {data['name']}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}%")

else:
    print("Error:", data.get("message"))