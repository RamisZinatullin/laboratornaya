Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... 
... def find_nearest_pharmacy(address):
...     # Получаем координаты заданного адреса с помощью геокодирования OpenStreetMap
...     response = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&q={address}")
...     location = response.json()[0]  # Берем первый результат
... 
...     # Ищем ближайшие аптеки к полученным координатам
...     pharmacy_response = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&amenity=pharmacy&lat={location['lat']}&lon={location['lon']}&limit=1")
...     pharmacy = pharmacy_response.json()[0]  # Берем ближайшую аптеку
... 
...     return pharmacy
... 
... # Получаем адрес от пользователя
... user_address = input("Введите адрес: ")
... 
... # Находим ближайшую аптеку
... nearest_pharmacy = find_nearest_pharmacy(user_address)
... 
... # Выводим результат
... print(f"Ближайшая аптека находится по адресу: {nearest_pharmacy['display_name']}")
