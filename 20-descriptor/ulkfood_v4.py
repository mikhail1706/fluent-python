"""
    Пример 20.2. bulkfood_v4.py: каждый дескриптор Quantity получает уникальное
        имя storage_name

    Пример 20.3. bulkfood_v4b.py (неполный листинг): при вызове через управляемый
           класс метод __get__ возвращает ссылку на сам дескриптор

"""


class Quantity:
    __counter = 0   # 1

    def __init__(self):
        cls = self.__class__    # 2
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = "-{}#{}".format(prefix, index)  # 3
        cls.__counter += 1  # 4

    def __get__(self, instance, owner):   # 5
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)     # 6

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)  # 7
        else:
            raise ValueError("value must be > 0")


class LineItem:
    weight = Quantity()   # 8
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

