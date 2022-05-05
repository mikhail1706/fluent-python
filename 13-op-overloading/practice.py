"""
    Глава 13. Перегрузка операторов: как правильно?

    Пример 13.1. vector_v6.py: унарные операторы - и + в дополнение к примеру 10.16
    Пример 13.4. Метод Vector.add, попытка № 1
    Пример 13.5. Vector.__add__ из примера 13.4 поддерживает сложение с объектами,
                 отличными от Vector
    Пример 13.7. Методы Vector.__add__ и __radd__
    Пример 13.8. Методу Vector.__add__ необходим итерируемый операнд
    Пример 13.9. Методу Vector.__add__ необходим итерируемый операнд с числовыми
                 элементами
    Пример 13.10. vector_v6.py: специальные методы оператора +, добавленные
                в файл vector_v5.py (пример 10.16)
    Пример 13.12. Сравнение Vector с Vector, с Vector2d и с tuple
    Пример 13.13. vector_v8.py: улучшенный метод __eq__ в классе Vector
    Пример 13.14. Те же сравнения, что в примере 13.12, последний результат
                    изменился
    Пример 13.18. bingoaddable.py: класс AddableBingoCage расширяет BingoCage,
                  добавляя поддержку операторов + и +=
    Пример 13.18. bingoaddable.py: класс AddableBingoCage расширяет BingoCage,
                  добавляя поддержку операторов + и +=
"""

import math
import numbers
import reprlib
from array import array
import functools
import operator
import itertools

tombola = __import__('11-iface-abc')

# Пример 13.1.
# Пример 13.4. Метод Vector.add, попытка № 1
# Пример 13.7
class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        """Пример 13.13. vector_v8.py:
        улучшенный метод __eq__ в классе Vector"""

        if isinstance(other, Vector):
            return (len(self) == len(other) and
                    all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        """Пример 13.1"""
        return math.sqrt(sum(x * x for x in self))

    def __pos__(self):
        """Пример 13.1"""
        return Vector(self)

    def __add__(self, other):
        """Пример 13.4 Пример 13.10"""
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        """Пример 13.7"""
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        """оператор @ в версии Python 3.5"""
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
        raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        """Пример 10.8. Часть файла vector_v3.py: в класс Vector из файла vector_v2.py добавлен
                 метод __getattr__"""
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        """Пример 10.10. Часть файла vector_v3.py:
            метод __setattr__ в классе Vector
        """
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z'  in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n), for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):  # hyperspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain[abs(self),
                                     self.angles()]
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


class AddableBingoCage(tombola):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self