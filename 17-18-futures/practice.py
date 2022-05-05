"""
    Пример 18.1. spinner_thread.py: анимация текстового индикатора с помощью потока
    Пример 18.2. spinner_asyncio.py: анимация текстового индикатора с помощью сопрограммы
    Пример 18.3. spinner_thread.py: функция supervisor с отдельным потоком
    Пример 18.4. spinner_asyncio.py: асинхронная сопрограмма supervisor
    Пример 18.6. Запуск скрипта flags2_asyncio.py
    Пример 18.7. flags2_asyncio.py: первая часть скрипта, вторая – в примере 18.8
    Пример 18.8. flags2_asyncio.py: продолжение скрипта из примера 18.7
    Пример 18.9. flags2_asyncio_executor.py: использование исполнителя по умолчанию
                 на основе пула потоков для выполнения функции save_flag
    Пример 18.10. Ад обратных вызовов в JavaScript: вложенные анонимные функции,
                 называемые еще «пирамидой судьбы» (http://survivejs.com/common_problems/pyramid.html)
    Пример 18.11. Ад обратных вызовов в Python: сцепленные обратные вызовы
    Пример 18.12. Сопрограммы и выражение yield from открывают возможность
                  для асинхронного программирования без обратных вызовов
    Пример 18.13. flags3_asyncio.py: количество вызовов сопрограмм увеличилось,
                  поскольку для каждого флага выполняется два запроса


    Пример 18.14. tcp_charfinder.py: простой TCP-сервер с применением функции
                  asyncio.start_server; код этого модуля продолжается в примере 18.15
    Пример 18.15. tcp_charfinder.py (продолжение примера 18.14): функция main
                  инициализирует и завершает цикл обработки событий и TCP-сервер
    Пример 18.16. tcp_charfinder.py: это серверная часть сеанса, показанного на рис. 18.2
    Пример 18.17. http_charfinder.py: функции main и init
    Пример 1818. http_charfinder.py: функция home

"""

@asyncio.coroutine
def three_stages(request1):
    response1 = yield from api_call1(request1)
    # шаг 1
    request2 = step1(response1)
    response2 = yield from api_call2(request2)
    # шаг 2
    request3 = step2(response2)
    response3 = yield from api_call3(request3)
    # шаг 3
    step3(response3)
    # выполнение необходимо планировать явно
    loop.create_task(three_stages(request1))