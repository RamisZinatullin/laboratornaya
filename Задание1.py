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

def run_tests():
    # Список тестов: каждая пара (строка, ожидаемый результат)
    tests = [
        ("A man a plan a canal Panama", True),
        ("racecar", True),
        ("hello", False),
        ("Was it a car or a cat I saw", True),
        ("No lemon, no melon", True),
        ("This is not a palindrome", False),
        ("", True),  # Пустая строка считается палиндромом
        ("a", True),  # Однобуквенная строка тоже палиндром
    ]

    # Проверяем все тесты
    for data, expected in tests:
        if is_palindrome(data) != expected:
            print("NO")
            return

    print("YES")

# Запускаем тесты
run_tests()
