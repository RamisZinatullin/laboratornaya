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

# Читаем строку из stdin
phone_number = input()

# Проверяем корректность номера
if is_correct_mobile_phone_number_ru(phone_number):
    print("YES")
else:
    print("NO")
