import requests


file_path = "/Users/msorokina/PycharmProjects/API-ключ OpenWeatherMap"

with open(file_path, 'r') as file:
    api_key = file.read()

city_name = input('Please enter the city: ').capitalize()
country_code = input('Please enter the country: ').capitalize()


# Отправляем запрос к API OpenWeatherMap
response = requests.get("http://api.openweathermap.org/data/2.5/find", params={
    'q': f'{city_name},{country_code}',
    'type': 'like',
    'units': 'metric',
    'appid': api_key})

# Проверяем статус код ответа
if response.status_code == 200:
    # Получаем JSON-данные из ответа
    json_data = response.json()
    # Извлекаем список погоды
    weather_list = json_data.get('list', [])

    # Проверяем наличие данных о погоде
    if weather_list:
        # Извлекаем информацию о погоде для первого элемента списка
        main_weather = weather_list[0]['main']
        temperature = main_weather['temp']
        feels_like = main_weather['feels_like']
        humidity = main_weather['humidity']
        wind = weather_list[0]['wind']['speed']
        weather_desc = weather_list[0]['weather'][0]['description']

        # Выводим информацию о погоде
        print(f'The temperature in {city_name} at the moment is {temperature}, \n'
              f'but it feels like: {feels_like}; \nHumidity: {humidity}%;\n'
              f'Wind is around {wind} meters/second;\nThe weather is {weather_desc}')
    else:
        # Если данные о погоде отсутствуют
        print('No weather data available for the specified location.')
else:
    # Если запрос к API не удался
    print('Please check the correctness of the entered data!')
