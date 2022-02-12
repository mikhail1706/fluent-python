# Пример 7.18
# Пример 7.19
from clockdeco_demo import clock
import functools

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-2) + fibonacci(n-1)



if __name__=='__main__':
    print(fibonacci(6))