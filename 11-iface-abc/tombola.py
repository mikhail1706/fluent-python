from abc import ABC, abstractmethod
import random


class Tombola(ABC):

    @abstractmethod
    def load(self, iterable):
        """Добавить элементы из итерируемого обекта."""

    @abstractmethod
    def pick(self):
        """Извлечь случайный элемент и вернуть его.
        Этот метод должен возбуждать исключение `LookupError`,
        если объект пуст.
        """

    def loaded(self):
        """Вернуть `True`, если есть хотя бы 1 элемент, иначе `False`."""
        return bool(self.inspect())

    def inspect(self):
        """Вернуть отсортированный кортеж, содержащий находящиеся в
        контейнере элементы.
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingCage')

    def __call__(self, *args, **kwargs):
        self.pick()


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingRange')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
