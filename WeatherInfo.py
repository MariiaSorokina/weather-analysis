import requests


class GetWeatherException(Exception):
    pass


class WeatherAPI:
    def __init__(self, api):
        self.api = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/find"

    def get_weather(self, city_name, country_code):
        params = {
            'q': f'{city_name},{country_code}',
            'type': 'like',
            'units': 'metric',
            'appid': self.api
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise GetWeatherException('Failed to retrieve weather data.')

    def get_forecast(self, city_name, country_code):
        try:
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
                raise GetWeatherException("Weather data not found.")
        except GetWeatherException as e:
            print(f"An error occurred: {str(e)}")


# Пример использования
file_path = "/Users/msorokina/PycharmProjects/API-ключ OpenWeatherMap"

with open(file_path, 'r') as file:
    api_key = file.read()

weather_api = WeatherAPI(api_key)

try:
    city = input('Please enter the city: ').capitalize()
    country = input('Please enter the country: ').capitalize()
    forecast = weather_api.get_forecast(city, country)

    print("Weather forecast:")
    print(f"Current temperature: {forecast['current_temperature']}°C")
    print(f"Feels like: {forecast['feels_like']}°C")
    print(f"Humidity: {forecast['humidity']}%")
    print(f"Wind speed: {forecast['wind']} м/с")
except KeyError:
    raise GetWeatherException("Invalid response format.")
except GetWeatherException as e:
    print(f"An error occurred: {str(e)}")
except IndexError:
    print('Incorrect data entered')
