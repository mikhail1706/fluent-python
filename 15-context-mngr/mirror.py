"""
    Пример 15.3. mirror.py: класс контекстного менеджера LookingGlass
    Пример 15.4. Исследование LookingGlass без блока with
    Пример 15.5. mirror_gen.py: реализация контекстного менеджера с
    помощью генератора
"""


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Пожалуйста, НЕ НАДО делить на нуль!')
            return True
