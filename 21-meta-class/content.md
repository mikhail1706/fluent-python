## Глава 21. Метапрограммирование классов

---
* **record_factory.py**
  * Пример 21.2. record_factory.py: простая фабрика классов


* **bulkfood_v6.py**
  * Пример 21.3. bulkfood_v6.py: класс `LineItem` с дескрипторами `Quantity` и `NonBlank`


* **model_v6.py**
  * Пример 21.4. model_v6.py: декоратор класса
  * Пример 21.5. bulkfood_v6.py: doctest-скрипты для проверки атрибутов дескрипторов
    `storage_name`


* **evalsupport.py**
  * Пример 21.7. evalsupport.py: модуль, импортируемый evaltime.py


* **evaltime_meta.py**
  * Пример 21.10. evaltime_meta.py: ClassFive – экземпляр метакласса `MetaAleph`


* **bulkfood_v7.py**
  * Пример 21.14. bulkfood_v7.py: наследование классу `model.Entity` сработает,
    если за кулисами маячит метакласс


* **model_v7.py**
  * Пример 21.15. model_v7.py: метакласс `EntityMeta` и один его экземпляр, `Entity`


* **model_v8.py**
  * Пример 21.16. model_v8.py: в метаклассе `EntityMeta` используется `__prepare__`,
    а в классе `Entity` теперь есть метод класса `field_names`


* **bulkfood_v8.py**
  * Пример 21.17. bulkfood_v8.py: doctest-скрипт для демонстрации метода
    `field_names` – в класс `LineItem` не пришлось вносить никаких изменений;
    метод `field_names` унаследован от `model.Entity`

---
### Summary
* model_v8.py - `EntityMeta` metaclass and descriptors (`AutoStorage`, `Validated`,
                `Quantity`, `NonBlank`).
* bulkfood_v8.py - `LineItem` class inherits from metaclass and contains descriptors


