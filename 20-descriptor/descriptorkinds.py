"""Пример 20.8. descriptorkinds.py: простые классы для изучения поведения
переопределяющих и непереопределяющих дескрипторов"""


# вспомогательные функции для отображения
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return "<class {}>".format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return "<{} object".format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print("-> {}.__{}__({})".format(cls_name(args[0]), name, pseudo_args))


# существенные для этого примера классы
class Overriding:   # 1
    """Он же дескриптор данных или принудительный дескриптор"""
    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)    # 2

    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class OverridingNoGet:  # 3
    """Переопределяющий дескриптор без ``__get__``"""
    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class NonOverriding:    # 4
    """Он же дескриптор без данных или маскируемый дескриптор"""
    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)


class Managed:  # 5
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):     # 6
        print("-> Managed.spam({})".format(display(self)))
