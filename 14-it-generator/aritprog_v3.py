"""
    Пример 14.13. aritprog_v3.py: работает, как предыдущие варианты
    функции aritprog_gen
"""

import itertools


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
