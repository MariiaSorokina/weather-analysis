# Документация: Получение информации о погоде с помощью OpenWeatherMap API
Этот код предоставляет простой способ получения информации о погоде для указанного города и страны, используя OpenWeatherMap API. Он запрашивает данные о погоде и выводит информацию о температуре, ощущаемой температуре, влажности, скорости ветра и описании погоды.

### Зависимости
Для работы кода необходимо установить модуль requests. Вы можете установить его с помощью pip командой:

````
pip install requests
````
## Использование
1. Зарегистрируйтесь на OpenWeatherMap и получите API-ключ.

2. Вставьте свой API-ключ OpenWeatherMap в переменную api_key в коде.

3. Запустите программу и следуйте указаниям, чтобы ввести город и страну для получения информации о погоде.

4. В результате будет выведена информация о погоде для указанного местоположения.

## Описание работы
1. Программа запрашивает у пользователя название города и страны.

2. Отправляется GET-запрос к API OpenWeatherMap с использованием введенных данных и API-ключа.

3. Если запрос успешен (статус код 200), программа получает JSON-данные с информацией о погоде.

4. Извлекается информация о погоде, включая температуру, ощущаемую температуру, влажность, скорость ветра и описание погоды.

5. Информация о погоде выводится на экран.

6. Если запрос не удался или данные о погоде отсутствуют, выводится соответствующее сообщение.

### Пример вывода

````
Please enter the city: Moscow
Please enter the country: Russia
The temperature in Moscow at the moment is 25.5,
but it feels like: 26.8;
Humidity: 70%;
Wind is around 2.5;
The weather is clear sky
````

### Ошибки и обработка исключений
* Если запрос к API OpenWeatherMap не удался, выводится сообщение Please check the correctness of the entered data!.
* Если данные о погоде для указанного местоположения отсутствуют, выводится сообщение No weather data available for the specified location..

## Важная информация

* Убедитесь, что у вас есть действующий API-ключ OpenWeatherMap и он добавлен в код.
* В случае возникновения ошибок при выполнении запроса или получении данных, проверьте соединение с интернетом, корректность ввода города и страны, а также доступность OpenWeatherMap API.
> Этот код позволяет получать простую информацию о погоде с помощью OpenWeatherMap API. Вы можете расширить его функциональность или внести изменения в соответствии с вашими потребностями и требованиями проекта.