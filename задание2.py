def is_palindrome(data):
    # Создаем пустую строку для хранения очищенной версии входной строки
    cleaned_data = ""

    # Проходим по каждому символу входной строки
    for char in data:
        # Если символ не является пробелом, добавляем его в cleaned_data
        if char != ' ':
            # Приводим символ к нижнему регистру и добавляем его в cleaned_data
            cleaned_data += char.lower()

    # Инициализируем два указателя: left на начало строки и right на конец строки
    left = 0
    right = len(cleaned_data) - 1

    # Проверяем символы с обоих концов строки, пока указатели не встретятся
    while left < right:
        # Если символы не совпадают, возвращаем False
        if cleaned_data[left] != cleaned_data[right]:
            return False
        # Перемещаем указатели навстречу друг другу
        left += 1
        right -= 1

    # Если все символы совпали, возвращаем True
    return True

# Чтение строки из stdin
import sys
input_string = sys.stdin.read().strip()

# Проверка, является ли строка палиндромом
if is_palindrome(input_string):
    print("YES")
else:
    print("NO")
