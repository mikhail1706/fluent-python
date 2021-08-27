"""
    Example 4.1. Encode(кодирование) and decoded(декодирование)
    Example 4.2. Пятибайтовая последовательность в виде bytes и bytearray
    Example 4.3. Инициализация байтов данными, хранящимися в массиве
    Example 4.4. Использование memoryview и struct для извлечения полей из заголовка
                 GIF-изображения
    Example 4.5  Строка «v», закодированная тремя кодеками, дает совершенно разные
                 последовательности байтов
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