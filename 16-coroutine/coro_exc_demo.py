"""
    Пример 16.8.  coro_exc_demo.py: тестовый код для изучения обработки исключений
                  в сопрограммах
    Пример 16.9.  Активация и завершение demo_exc_handling без исключения
    Пример 16.10. Возбуждение исключения DemoException в demo_exc_handling
                  не приводит к выходу из нее
    Пример 16.11. Сопрограмма завершается, если не может обработать возбужденное
                  в ней исключение
"""


class DemoException(Exception):
    """AN exception type for the demonstration."""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** Demo exception handled. Continuing...')
        else:
            print(f'-> coroutine received: {x}')

    raise RuntimeError('This line should never run.')


# Пример 16.9. Активация и завершение demo_exc_handling без исключения
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
exc_coro.close()
from inspect import getgeneratorstate
getgeneratorstate(exc_coro)



# Пример 16.10. Возбуждение исключения DemoException в demo_exc_handling
# не приводит к выходу из нее
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)
getgeneratorstate(exc_coro)


# Пример 16.11. Сопрограмма завершается, если не может обработать возбужденное
# в ней исключение
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(ZeroDivisionError)
getgeneratorstate(exc_coro)         # GEN_CLOSED