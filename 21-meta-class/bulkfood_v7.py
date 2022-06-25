"""Пример 21.14. bulkfood_v7.py: наследование классу model.Entity сработает,
если за кулисами маячит метакласс"""

import model_v7 as model


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
