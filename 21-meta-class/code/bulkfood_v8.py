"""Пример 21.17. bulkfood_v8.py: doctest-скрипт для демонстрации метода
field_names – в класс LineItem не пришлось вносить никаких изменений;
метод field_names унаследован от model.Entity"""

import model_v8 as model


class LineItem(model.Entity):  # 1
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


for name in LineItem.field_names():
    print(name)
