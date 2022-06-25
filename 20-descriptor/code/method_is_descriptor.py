"""Пример 20.14. method_is_descriptor.py: класс Text, наследующий UserString
    Пример 20.15. Эксперименты с методом
"""

import collections


class Text(collections.UserString):
    def __repr__(self):
        return "Text({!r})".format(self.data)

    def reverse(self):
        return self[::-1]


word = Text("forward")
print(repr(word))

print(repr(word.reverse()))

print(repr(Text.reverse(Text('backward'))))

print(type(Text.reverse), type(word.reverse))
print(list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')])))
print(Text.reverse.__get__(word))
print(Text.reverse.__get__(None, Text))
print(repr(word.reverse))
print(repr(word.reverse.__self__))
print(word.reverse.__func__ is Text.reverse)