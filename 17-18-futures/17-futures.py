"""
    Глава 17. Параллелизм и будущие объекты
    Пример 17.1. Результаты трех типичных прогонов скриптов flags.py, flags_threadpool.py
                 и flags_asyncio.py
    Пример 17.2. flags.py: последовательный скрипт загрузки; некоторые функции будут
                 использованы и в других скриптах
    Пример 17.3. flags_threadpool.py: многопоточный скрипт загрузки с применением
                 класса futures.ThreadPoolExecutor
    Пример 17.4. flags_threadpool_ac.py: замена executor.map на executor.submit
                 и futures.as_completed в функции download_many
    Пример 17.5. Результат работы скрипта flags_threadpool_ac.py
    Пример 17.6. demo_executor_map.py: простая демонстрация метода map
                 объекта ThreadPoolExecutor
    Пример 17.7. Результаты прогона скрипта demo_executor_map.py из примера 17.6
    Пример 17.8. Справка для скриптов из серии flags2
    Пример 17.9. Прогон flags2_sequential.py с параметрами по умолчанию: сервер LOCAL,
                 флаги 20 самых густонаселенных стран, 1 соединение
    Пример 17.11. Прогон flags2_asyncio.py с загрузкой 100 флагов (-al 100)
                  с сервера ERROR, 100 одновременных соединений (-m 100)

    flags2_sequential.py
    Пример 17.12. flags2_sequential.py: базовые функции, отвечающие за загрузку,
                 обе используются также в скрипте flags2_threadpool.py

    flags2_sequential.py
    Пример 17.13. flags2_sequential.py: последовательная реализация download_many

    flags2_threadpool.py
    Пример 17.14. flags2_threadpool.py: полный исходный код
"""