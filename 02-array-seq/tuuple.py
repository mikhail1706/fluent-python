"""
Кортежи.
    Кортежи как записи.
    Example 2.7. Кортежи как записи
        1.паралельная расспаковка
        2. обмен занчений двух переменных
        3. приминение звездочки
        4. Возврат нескольких значений из функции
        5. Использование * для выборки лишьних элементов
        6. Префикс * можно ставить перед одной переменой которая может заимать любую позицию

    Example 2.8
        1. Распаковка вложеного кортежа

    Example 2.9 + Example 2.10
        1. Именованые кортежи

    Кортежи как неизменяемые списки.


"""


# Example 2.7. Кортежи как записи
# lax_coordinates = (33.94, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
#
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
#
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
#
# for country, _ in traveler_ids:
#     print(country)


# паралельная расспаковка
# latitude, longitude = lax_coordinates = (33.94, -118.408056)


# обмен занчений двух переменных
# a = 5
# b = 4
# a, b = b, a


# приминение звездочки
# divmod(20, 8)
# t = (20, 8)
# quotient, remainder = divmod(*t)

# Возврат нескольких значений из функции
# import os
# _, filename = os.path.split('')


# Использование * для выборки лишьних элементов
# a, b, *rest = range(5)
# a, b, *rest = range(3)
# a, b, *rest = range(2)


# Префикс * можно ставить перед одной переменой которая может заимать любую позицию
# a, *body, c, d = range(5)
# *head, b, c, d = range(5)


# Example 2.8. Распаковка вложеного кортежа
# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]
#
# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
#     if longitude <= 0:  # <3>
#         print(fmt.format(name, latitude, longitude))


# Example 2.9 + Example 2.10. Именованные кортежи
# from collections import namedtuple
#
# City = namedtuple('City', 'name country, population coordinates')
#
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
#
# LatLong = namedtuple('LatLong', 'lat long')
# delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
#
# delhi = City._make(delhi_data)              # Cоздает именнованый кортеж из итерируемого обекта.
#                                             # Похоже City(*delhi_data)
#
# for key, value in delhi._asdict().items():
#     print(key + ':', value)



