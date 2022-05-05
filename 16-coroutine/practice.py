"""
    Глава 16. Сопрограммы

    Пример 16.1. Простейшая демонстрация сопрограммы в действии
    Пример 16.2. Сопрограмма с двумя yield
    Пример 16.3. coroaverager0.py: сопрограмма для вычисления накопительного
                 среднего
    Пример 16.4. coroaverager0.py: doctest-скрипт, демонстрирующий использование
                 сопрограммы вычисления накопительного среднего из примера 16.3
    Пример 16.5. coroutil.py: декоратор для инициализации сопрограмм
    Пример 16.6. coroaverager1.py: doctest-скрипт и код сопрограммы вычисления
                 накопительного среднего с использованием декоратора @coroutine
                 из примера 16.5
    Пример 16.7. Как необработанное исключение аварийно завершает сопрограмму

    coro_exc_demo.py
    Пример 16.8.  coro_exc_demo.py: тестовый код для изучения обработки исключений
                  в сопрограммах
    Пример 16.9.  Активация и завершение demo_exc_handling без исключения
    Пример 16.10. Возбуждение исключения DemoException в demo_exc_handling
                  не приводит к выходу из нее
    Пример 16.11. Сопрограмма завершается, если не может обработать возбужденное
                  в ней исключение

    coro_finally_demo.py
    Пример 16.12. coro_finally_demo.py: использование try/finally для выполнения
                  некоторых действий по завершении сопрограммы

    сoroaverager2.py
    Пример 16.13. coroaverager2.py: сопрограмма averager, возвращающая результат
    Пример 16.14. coroaverager2.py: doctest-скрипт, иллюстрирующий поведение averager
    Пример 16.15. Перехват StopIteration позволяет получить значение,
                  возвращенное averager

    # Использование yield from
    Пример 16.16. Сцепление итерируемых объектов с помощью yield from

    coroaverager3.py
    Пример 16.17. coroaverager3.py: использование yield from для управления
                  сопрограммой averager и печати статистического отчета


    Пример 16.17. coroaverager3.py: использование yield from для управления
                  сопрограммой averager и печати статистического отчета
    Пример 16.21. Управление сопрограммой taxi_process

"""


# Пример 16.1. Простейшая демонстрация сопрограммы в действии
def simple_coroutine():
    print('_> coroutine started')
    x = yield
    print('-> coroutine received:', x)

my_coro = simple_coroutine()
print(my_coro)
next(my_coro)
my_coro.send(42)

# Пример 16.2. Сопрограмма с двумя yield
def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)

my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate
getgeneratorstate(my_coro2)
next(my_coro2)
getgeneratorstate(my_coro2)
my_coro2.send(28)
my_coro2.send(99)
getgeneratorstate(my_coro2)


# Пример 16.3. coroaverager0.py: сопрограмма для вычисления
# накопительного среднего
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(5)

# Пример 16.5. coroutil.py: декоратор для инициализации сопрограмм
from functools import wraps

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


#Пример 16.6. coroaverager1.py: doctest-скрипт и код сопрограммы вычисления
# накопительного среднего с использованием декоратора @coroutine из примера 16.5
@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

coro_avg = averager()
from inspect import getgeneratorstate
getgeneratorstate(coro_avg)


# Пример 16.16. Сцепление итерируемых объектов с помощью yield from
def chain(*iterables):
    for it in iterables:
        yield from it

s = 'ABC'
t = tuple(range(3))
list(chain(s, t))