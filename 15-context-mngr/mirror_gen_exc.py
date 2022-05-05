from contextlib import contextmanager


@contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''

    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Пожалуйста, НЕ НАДО делить на нуль!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)