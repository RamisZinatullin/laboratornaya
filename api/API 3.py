Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_southernmost_city(cities):
...     city_coordinates = {
...         "Москва":  (55.755825, 37.617298),
...         "Санкт-Петербург": (59.9343, 30.3351),
...         "Екатеринбург": (56.8380, 60.5970),
...         "Краснодар": (45.0355, 38.9753)
...         # Добавьте остальные города и их координаты
...     }
...     
...     southernmost_city = None
...     southernmost_latitude = 90  # Начальное значение для сравнения
...     
...     for city in cities:
...         if city in city_coordinates:
...             latitude = city_coordinates[city][0]
...             if latitude < southernmost_latitude:
...                 southernmost_latitude = latitude
...                 southernmost_city = city
...     
...     return southernmost_city
... 
... # Получаем список городов от пользователя
... cities = input("Введите названия городов через запятую: ").split(",")
... 
... # Находим самый южный город
... southernmost = find_southernmost_city([city.strip() for city in cities])
... 
... # Выводим результат
... if southernmost:
...     print(f"Самый южный город: {southernmost}")
... else:
...     print("Указаны недопустимые города")
