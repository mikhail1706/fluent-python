"""
    Пример 16.13. coroaverager2.py: сопрограмма averager, возвращающая результат
    Пример 16.14. coroaverager2.py: doctest-скрипт, иллюстрирующий поведение averager
    Пример 16.15. Перехват StopIteration позволяет получить значение,
                  возвращенное averager
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count

    return Result(count, average)

# Пример 16.14. coroaverager2.py: doctest-скрипт,
# иллюстрирующий поведение averager

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
coro_avg.send(None)


# Пример 16.15. Перехват StopIteration позволяет получить значение,
# возвращенное averager

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value