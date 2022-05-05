"""
    ГЛАВА 14. Итерируемые объекты, итераторы и генераторы 473
    Пример 14.1. sentence.py: объект Sentence как последовательность слов
    Пример 14.2. Итерирование объекта Sentence
    Пример 14.3. Класс abc.Iterator; код взят из файла Lib/_collections_abc.py
    Пример 14.4. sentence_iter.py: класс Sentence, реализованный с помощью
                 паттерна Итератор
    Пример 14.5. sentence_gen.py: реализация класса Sentence с помощью генераторной
                функции
    Пример 14.6. Генераторная функция, печатающая сообщения во время выполнения
    Пример 14.7. sentence_gen2.py: реализация класса Sentence с помощью генераторной
                функции, которая вызывает генераторную функцию re.finditer

    Пример 14.8. Генераторная функция gen_AB используется сначала в списковом
                включении, а затем в генераторном выражении
    Пример 14.9. sentence_genexp.py: реализация класса Sentence с помощью
                генераторного выражения
    Пример 14.10. Демонстрация класса ArithmeticProgression
    Пример 14.11. Класс ArithmeticProgression
    Пример 14.12. Генераторная функция aritprog_gen
    Пример 14.13. aritprog_v3.py: работает, как предыдущие варианты
                  функции aritprog_gen

    Пример 14.14. Примеры фильтрующих генераторных функций
    Пример 14.15. Примеры применения генераторной функции itertools.accumulate
    Пример 14.16. Примеры применения отображающих генераторных функций
    Пример 14.17. Примеры применения объединяющих генераторных функций
    Пример 14.17. Примеры применения объединяющих генераторных функций
    Пример 14.19. Функции count, cycle и repeat
    Пример 14.20. Комбинаторные генераторные функции отдают несколько значений
                  для каждого входного элемента
    Пример 14.21. itertools.groupby
    Пример 14.23. Результаты применения all и any к некоторым
                  последовательностям

"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence {reprlib.repr(self.text)}'


class Iterator:
    pass


# Пример 14.6. Генераторная функция, печатающая сообщения во время выполнения
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index