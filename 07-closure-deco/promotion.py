promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """"""
    """5%-ая скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """10%-ая скидка для каждой позиции LineItem, в которой заказано
    не менее 20 единиц"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """7%-ая скидка для заказов, включающих не менее 10 различных позиций"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    """Выбрать максимально возможную скидку
    """
    return max(promo(order) for promo in promos)