"""
    Глава 9. Объект в духе Python
    Пример 9.5. Метод Vector2d.format, попытка №1
    Пример 9.6. Метод Vector2d.format , попытка № 2 – теперь и в полярных
                координатах
    Пример 9.7. vector2d_v3.py: показаны только изменения, необходимые, чтобы
                сделать класс Vector2d неизменяемым, полный листинг см.
                в примере 9.9
    Пример 9.8. vector2d_v3.py: реализация хэширования
    !!!Пример 9.9. vector2d_v3.py: полный код
    Пример 9.11. vector2d_v3_slots.py: по сравнению с версией Vector2d добавился только
                атрибут __slots__
    !!!Пример 9.12. mem_test.py создает 10 миллионов экземпляров класса Vector2d
                из указанного при запуске модуля (например, vector2d_v3.py)
    !!!Пример 9.13. Настройка экземпляра путем установки атрибута typecode, первоначально
                унаследованного от класса
    Пример 9.14. ShortVector2d – подкласс Vector2d, единственное отличие которого –
                 переопределение атрибута typecode по умолчанию
"""

from vector2d_v0 import Vector2d

# Exp 9.1
v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))

# Пример 9.6. Метод Vector2d.format , попытка
# № 2 – теперь и в полярных координатах
format(Vector2d(1, 1), '.3ep')
format(Vector2d(1, 1), 'p')
format(Vector2d(1, 1), '0.5fp')

# Пример 9.8. vector2d_v3.py: реализация хэширования
v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
hash(v1), hash(v2)
print({v1, v2})


# Пример 9.14. ShortVector2d – подкласс Vector2d, единственное отличие
# которого – переопределение атрибута typecode по умолчанию
class ShortVector2d(Vector2d):
    typecode = 'f'