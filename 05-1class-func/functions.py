"""
    Functions:
    Example 5.1: Создаем и тестируем функцию, затем читаем ее атрибут __doc__
                 и опрашиваем тип
    Example 5.2. Использование функции под другим именем и передача функции
                 в качестве аргумента
    Example 5.3. Сортировка списка слов по длине
    Example 5.4. Сортировка списка слов в обратном порядке букв
    Example 5.5. Списки факториалов, порожденные функциями map и filter, а также
                 альтернатива в виде спискового включения
    Example 5.6. Суммирование целых чисел до 99 с помощью reduce и sum
    Example 5.7. Сортировка списка слов в обратном порядке букв с помощью lambda
    Example 5.8. bingocall.py: экземпляр BingoCage делает всего одну вещь: выбирает
                элементы из перетасованного списка
    Example 5.9. Перечисление атрибутов функций, отсутствующих у обычных объектов
    Example 5.10.Функция tag генерирует HTML; чисто именованный аргумент cls служит
                 для передачи атрибута «class». Это обходное решение необходимо,
                 потому что в Python class – зарезервированное слово
    Example 5.11 Некоторые из многочисленных способов вызвать функцию tag
                 из примера 5.10
    Example 5.18 Связывание сигнатуры функции tag из примера 5.10
                  со словарем аргументов
    Example 5.19 Аннотированная функция clip
    Example 5.22 Вычисление факториала с помощью reduce и operator.mul
    Example 5.23 Результат применения itemgetter для сортировки списка кортежей
    Example 5.24 Применение attrgetter для обработки ранее определенного списка
                 именованных кортежей metro_data (тот же список, что в примере 5.23)
    Example 5.25 Демонстрация methodcaller: во втором тесте показано связывание
                 дополнительных аргументов

    Example 5.26 Использование partial позволяет вызывать функцию с двумя
                 аргументами там, где требуется вызываемый объект с одним аргументом

    Фиксация аргументов с помощью functools.partial ст. 191
"""


# Example 5.1
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial.__doc__)
print(type(factorial))
print(help(factorial))

# Example 5.2
fact = factorial
print(fact)
print(fact(5))
print(list(map(fact, range(11))))

# Example 5.3
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


# Example 5.4
def reverse(word):
    return word[::-1]


print(reverse('testing'))
print(sorted(fruits, key=reverse))

# Example 5.5
list(map(fact, range(6)))
[fact(n) for n in range(6)]

list(map(factorial, filter(lambda n: n % 2, range(6))))
[factorial(n) for n in range(6) if n % 2]

# Example 5.6
from functools import reduce
from operator import add

reduce(add, range(100))
sum(range(100))

# Example 5.7
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word: word[::-1])

# Example 5.8
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))
bingo.pick()
bingo()
callable(bingo)


# Example 5.9
class C:
    pass


obj = C()


def func():
    pass


sorted(set(dir(func)) - set(dir(obj)))


# Example 5.10
def tag(name, *content, cls=None, **attrs):
    """Генерирует один или несколько HTML-тегов"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

# Example 5.11
tag('br')
tag('p', 'hello')
print(tag('p', 'hello', 'world'))
tag('p', 'hello', id=33)
print(tag('p', 'hello', 'world', cls='sidebar'))
tag(content='testing', name="img")

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
tag(**my_tag)