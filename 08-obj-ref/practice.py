"""
    Ссылки на объекты, изменяемость и повторное использование
    Пример 8.1.  В переменных a и b хранятся ссылки на один и тот же список,
                 а не копии списка
    Пример 8.2.  Переменные присваиваются объектам только после создания
                 объектов
    Пример 8.3.  Переменные charles и lewis ссылаются на один и тот же объект
    Пример 8.4.  alex и charles равны, но alex не совпадает с charles
    Пример 8.5.  Кортежи t1 и t2 первоначально равны, но после модификации
                 изменяемого
                 объекта, хранящегося в t1, они перестают быть равными
    Пример 8.6.  Создание поверхностной копии списка, содержащего
                 другой список;
                 скопируйте этот код на сайт Online Python Tutor,
                 чтобы увидеть его анимацию
    Пример 8.7.  Результат работы примера 8.6
    Пример 8.8.  Автобус подбирает и высаживает пассажиров
    Пример 8.9.  Сравнение copy и deepcopy
    Пример 8.10. Циклические ссылки: b ссылается на a, а затем добавляется
                 в конец a; тем не менее, deepcopy справляется с копированием a
    Пример 8.11. Функция может модифицировать любой переданный ей изменяемый объект
    Пример 8.12. Простой класс, иллюстрирующий опасности изменяемых значений
                 по умолчанию
    Пример 8.13. Автобусы, облюбованные пассажирами-призраками
    Пример 8.15. Простой класс, иллюстрирующий опасности, которыми чревато изменение
                 полученных аргументов


    Защитное программирование при наличии изменяемых параметров ст. 261
"""


# Пример 8.8. Автобус подбирает и высаживает пассажиров
class Bus:
    def __init__(self, passenger=None):
        if passenger is None:
            self.passengers = []
        else:
            self.passengers = list(passenger)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# Пример 8.9. Сравнение copy и deepcopy
import  copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
bus1.drop('Bill')
print(bus2.passengers)
print(bus3.passengers)

# Пример 8.10. Циклические ссылки: b ссылается на a, а затем добавляется в
# конец a; тем не менее, deepcopy справляется с копированием a

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)
from copy import deepcopy
c = deepcopy(a)
print(c)


# Пример 8.11. Функция может модифицировать любой переданный
# ей изменяемый объект
def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))      # output: 3
print(x, y)         # (1, 2)

a = [1, 2]
b = [3, 4]
print(f(a, b))      # [1, 2, 3, 4]
print(a, b)         # ([1, 2, 3, 4], [3, 4])

t = (10, 20)
u = (30, 40)
print(f(t, u))      # ((10, 20), (30, 40))

# Пример 8.12. Простой класс, иллюстрирующий опасности изменяемых значений
# по умолчанию


class HauntedBus:
    """Автобус, облюбованный пассажирами-призраками"""
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# Пример 8.13. Автобусы, облюбованные пассажирами-призраками
bus1 = HauntedBus(['Alice', 'Bill'])
bus1.passengers
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)


# Пример 8.15
class TwilightBus:
    """Автобус, из которого бесследно исчезают пассажиры"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            # не правильно
            # self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

