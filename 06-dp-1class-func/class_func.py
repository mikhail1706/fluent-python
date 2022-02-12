"""
    Patterns:
    Example 6.1 Реализация класса Order с помощью взаимозаменяемых стратегий
                предоставления скидки
    Example 6.2 Пример использования класса Order с различными стратегиями скидок
    Example 6.3 Класс Order, в котором стратегии предоставления скидок реализованы
                в виде функций
    Пример 6.7. Список promos строится путем просмотра глобального пространства
                имен модуля
    Пример 6.8. Список promos строится путем интроспекции нового модуля promotions
    Пример 6.9. В каждом объекте MacroCommand хранится внутренний список команд

    Функционально-ориентированная стратегия 203
"""

# Example 6.1
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # Контекст
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total()} due: {self.due()}>'


class Promotion(ABC):  # Стартегия: абстрактный базовый класс

    @abstractmethod
    def discount(self, order: Order):
        """Вернуть скидку в виде положительной суммы в долларах"""


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5%-я скидка для заказчиков, имеющиъ не менне 1000 доларов лояльности"""

    def discount(self, order: Order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """10%-ая скидка для каждой позиции LineItem, в которой заказано
    не менее 20 единиц"""

    def discount(self, order: Order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7%-ая скидка для заказов, включающих не менее 10 различных позиций"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


# Example 6.1
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

Order(joe, cart, FidelityPromo())
Order(ann, cart, FidelityPromo())

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
Order(joe, banana_cart, BulkItemPromo())

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
Order(joe, long_order, LargeOrderPromo())
Order(joe, cart, LargeOrderPromo())

# Example 6.3
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """5%-ая скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10%-ая скидка для каждой позиции LineItem, в которой заказано
    не менее 20 единиц"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """7%-ая скидка для заказов, включающих не менее 10 различных позиций"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


# Пример 6.7.
promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']


def best_promo(order):
    """Выбрать максимально возможную скидку
    """
    return max(promo(order) for promo in promos)


# Пример 6.8
import inspect
promotions = 'module'
promos = [func for name, func in
          inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order):
    """Выбрать максимально возможную скидку
    """
    return max(promo(order) for promo in promos)


# Пример 6.9.
class MacroCommand:
    """Команда, выполняющая список команд"""

    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        for command in self.commands:
            command()