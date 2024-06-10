def is_correct_mobile_phone_number_ru(number):
    # Проверяем, что номер начинается с '+7' или '8'
    if not (number.startswith('+7') or number.startswith('8')):
        return False

    # Проверяем правильное использование скобок
    if '(' in number or ')' in number:
        if '(' not in number or ')' not in number:
            return False
        otkr_skobka = number.index('(')
        zakr_skobka = number.index(')')
        if zakr_skobka - otkr_skobka != 4:
            return False

    cleaned_number=""

    for char in number:
        if char.isdigit():
            # Если символ является цифрой, добавляем его в cleaned_number
            cleaned_number += char

    if len(cleaned_number) != 11:
        return False

    # Если все проверки пройдены, возвращаем True
    return True

# Тестирующая программа
def run_tests():
    # Список тестов в формате (номер телефона, ожидаемый результат)
    tests = [
        # Корректные номера
        ("+7 900 123 45 67", True),
        ("+7(900)123-45-67", True),
        ("+7 900 1234567", True),
        ("8 900 123 45 67", True),
        ("8(900)123-45-67", True),
        ("89001234567", True),
        # Некорректные номера
        ("+7 900 123 45 678", False),  # Слишком много цифр
        ("+7 900 123 456", False),     # Недостаточно цифр
        ("+7 90 123 45 67", False),    # Недостаточно цифр в коде оператора
        ("9 900 123 45 67", False),    # Неправильный префикс
        ("+7 (900) 123 45 67 89", False),  # Слишком много цифр
        ("8 9001234567", True),        # Корректный номер с отсутствующими пробелами и дефисами
        ("+7(999 123 45 67", False),   # Некорректное использование скобок
        ("7(999)1234567", False),      # Неправильный префикс
    ]

    # Проходим по каждому тесту
    for number, expected in tests:
        result = is_correct_mobile_phone_number_ru(number)
        if result != expected:
            print(f"Test failed for number: {number}. Expected: {expected}, got: {result}")
            print("NO")
            return

    # Если все тесты пройдены, печатаем "YES"
    print("YES")

# Запускаем тесты
run_tests()

