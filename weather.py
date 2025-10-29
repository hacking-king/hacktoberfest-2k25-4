import requests

def get_weather(city):
    api_key = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': 'YOUR_API_KEY',  # Replace with your OpenWeather key
        'units': 'metric'
    }
    res = requests.get(api_key, params=params)
    data = res.json()
    
    if data.get("cod") != 200:
        print("City not found!")
        return
    print(f"🌦 Weather in {city}: {data['weather'][0]['description']}")
    print(f"🌡 Temperature: {data['main']['temp']}°C")
    print(f"💨 Wind Speed: {data['wind']['speed']} m/s")

city = input("Enter city name: ")
get_weather(city)
