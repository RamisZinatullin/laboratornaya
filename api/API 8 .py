Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... 
... # Вводим координаты дома
... home_lat = float(input("Введите широту вашего дома: "))
... home_long = float(input("Введите долготу вашего дома: "))
... 
... # Вводим координаты университета
... uni_lat = float(input("Введите широту университета: "))
... uni_long = float(input("Введите долготу университета: "))
... 
... # Переводим градусы в радианы
... home_lat_rad = math.radians(home_lat)
... uni_lat_rad = math.radians(uni_lat)
... 
... # Считаем декартову метрику
... distance = 111 * math.sqrt((home_lat - uni_lat)**2 + (home_long - uni_long)**2 * math.cos((home_lat_rad + uni_lat_rad) / 2))
... 
... print("Приблизительное расстояние от дома до университета: ", round(distance, 2), "км")
