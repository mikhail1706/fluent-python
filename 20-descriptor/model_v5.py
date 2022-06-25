"""Пример 20.6. model_v5.py: дескрипторные классы после рефакторинга"""

import abc


class AutoStorage:  # 1
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = "_{}#{}".format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)     # 2


class Validated(abc.ABC, AutoStorage):  # 3
    def __set__(self, instance, value):
        value = self.validate(instance, value)  # 4
        super(Validated, self).__set__(instance, value)  # 5

    @abc.abstractmethod
    def validate(self, instance, value):    # 6
        """Возвращает проверенное значение или возбуждает ValueError"""


class Quantity(Validated):  # 7
    """Число больше нуля"""
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        return value


class NonBlank(Validated):
    """Строка содержит хотя бы один непробельный символ"""
    def validate(self, instance, value: str):
        value = value.strip()
        if len(value) == 0:
            raise ValueError("Value cannot be empty or blank")
        return value    # 8

