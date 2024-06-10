Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import folium
... from geopy.distance import geodesic
... 
... # Задаем последовательность точек в виде списка координат [широта, долгота]
... path_coordinates = [
...     (55.7558, 37.6173), # Москва
...     (59.9343, 30.3351), # Санкт-Петербург
...     (56.8380, 60.5970), # Екатеринбург
...     (45.0355, 38.9753)  # Краснодар
... ]
... 
... # Создаем базовую карту с центром в середине пути
... average_point = [sum(p[0] for p in path_coordinates)/len(path_coordinates), 
...                  sum(p[1] for p in path_coordinates)/len(path_coordinates)]
... 
... path_map = folium.Map(location=average_point, zoom_start=4)
... 
... # Добавляем метку в среднюю точку пути
... folium.Marker(location=average_point, popup="Средняя точка пути", 
...               icon=folium.Icon(color='green')).add_to(path_map)
... 
... # Добавляем линию, представляющую путь, на карту
... folium.PolyLine(path_coordinates, color="blue", weight=2.5, opacity=1).add_to(path_map)
... 
... # Определяем длину пути
... distance = 0
... for i in range(len(path_coordinates)-1):
...     distance += geodesic(path_coordinates[i], path_coordinates[i+1]).kilometers
... 
... print("Длина пути:", distance, "километров")
... 
... # Сохраняем карту в HTML файл
... path_map.save("path_map.html")
