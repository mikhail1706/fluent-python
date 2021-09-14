"""
    Example 4.1. Encode(кодирование) and decoded(декодирование)
    Example 4.2. Пятибайтовая последовательность в виде bytes и bytearray
    Example 4.3. Инициализация байтов данными, хранящимися в массиве
    Example 4.4. Использование memoryview и struct для извлечения полей из заголовка
                 GIF-изображения
    Example 4.5  Строка «v», закодированная тремя кодеками, дает совершенно разные
                 последовательности байтов
    Example 4.14 Функция удля удаления всех модифицирующих символов (модуль sanitize.py)
    Example 4.20 Использование метода pyuca.Collator.sort_key
    Example 4.21 Демонстрация работы с метаданными символов в базе данных Unicode
                 (числовые маркеры описывают отдельные столбцы распечатки)
    Example 4.22. ramanujan.py: сравнение поведения простых регулярных выражений
                 с аргументами типа str и bytes
"""

# Example 4.1
s = 'café'
print(len(s))                   # Строка 'café' состоит из четырех символов Unicode.

b = s.encode('utf8')            # Преобразуем str в bytes, пользуясь кодировкой UTF-8.
print(b)                        # Литералы типа bytes начинаются префиксом b.
print(len(b))                   # Объект b типа bytes состоит из пяти байтов (кодовая позиция, соответствую-
                                # щая «é», в UTF-8 кодируется двумя байтами).

print(b.decode('utf-8'))        # Преобразуем bytes обратно в str, пользуясь кодировкой UTF-8.


# Example 4.2
cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

# Example 4.3
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)

# Example 4.5
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

# Example 4.14
import unicodedata
import string


def shave_marks(txt):
    """Удалить все диакритические знаки"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


# Example 4.16
def shave_marks_latin(txt):
    """Удалить все диакритические знаки для базовых символов из наборов Latin"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue

        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters

    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)


# Example 4.21
import unicodedata
import re

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),
          char.center(6),
          're_dig' if re_digit.match(char) else '-',
          'isdig' if char.isdigit() else '-',
          'isnum' if char.isnumeric() else '-',
          format(unicodedata.numeric(char), '5.2f'),
          unicodedata.name(char),
          sep='\t')


# Example 4.22
import re

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')
text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n ')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str))
print(' bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print(' str :', re_words_str.findall(text_str))
print(' bytes:', re_words_bytes.findall(text_bytes))
