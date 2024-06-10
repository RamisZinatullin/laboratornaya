Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import folium
... 
... stadiums_location = {
...     "Лужники": [55.715551, 37.554191],
...     "Спартак": [55.818015, 37.440262],
...     "Динамо": [55.791540, 37.559809]
... }
... 
... # Создаем базовую карту с центром в Москве
... moscow_map = folium.Map(location=[55.755825, 37.617298], zoom_start=11)
... 
... # Добавляем метки стадионов на карту
... for stadium, location in stadiums_location.items():
...     folium.Marker(location=location, tooltip=stadium).add_to(moscow_map)
... 
... # Сохраняем карту в HTML файл
... moscow_map.save("moscow_stadiums_map.html")
