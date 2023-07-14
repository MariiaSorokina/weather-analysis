import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/find"

    def get_weather(self, city_name, country_code):
        params = {
            'q': f'{city_name},{country_code}',
            'type': 'like',
            'units': 'metric',
            'appid': self.api_key
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def get_forecast(self, city_name, country_code):
        weather_data = self.get_weather(city_name, country_code)

        if weather_data:
            forecast = {}
            result = weather_data['list'][0]

            forecast['current_temperature'] = result['main']['temp']
            forecast['feels_like'] = result['main']['feels_like']
            forecast['humidity'] = result['main']['humidity']
            forecast['wind'] = result['wind']['speed']
            forecast['condition'] = result['weather'][0]['description']

            return forecast
        else:
            return None

# Пример использования
file_path = "/Users/msorokina/PycharmProjects/API-ключ OpenWeatherMap"

with open(file_path, 'r') as file:
    api_key = file.read()

weather_api = WeatherAPI(api_key)

city = input('Please enter the city: ').capitalize()
country = input('Please enter the country: ').capitalize()
forecast = weather_api.get_forecast(city, country)

if forecast:
    print("Weather forecast:")
    print(f"Current temperature: {forecast['current_temperature']}°C")
    print(f"Feels like: {forecast['feels_like']}°C")
    print(f"Humidity: {forecast['humidity']}%")
    print(f"Wind speed: {forecast['wind']} м/с")
    print(f"Weather condition: {forecast['condition']}")
else:
    print("It was not possible to get a weather forecast.")

        # current_temperature, feels_like, humidity, wind, condition