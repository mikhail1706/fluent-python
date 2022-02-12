"""
    Пример 12.1. Наш метод __setitem__ игнорируется методами __init__
                и __update__ встроенного типа dict
    Пример 12.2. Метод __getitem__ из класса AnswerDict игнорируется
                методом dict.update
    Пример 12.3. Классы DoppelDict2 и AnswerDict2 работают, как и ожидалось,
                потому что расширяют UserDict, а не dict
    Пример 12.4. diamond.py: классы A, B, C и D образуют граф,
                показанный на рис. 12.1
    Пример 12.5. Два способа вызвать метод pong от имени экземпляра класса D
    Пример 12.6. Использование super() для вызова ping (для примера 12.4)
    Пример 12.7. Пять вызовов, выполненных методом pingpong (для примера 12.4)
    Пример 12.8. Инспектирование класса __mro__ в нескольких классах
"""

# Пример 12.4
class A:
    def ping(self):
        print('ping A: ', self)

class B(A):
    def pong(self):
        print('pong: ', self)

class C(A):
    def pong(self):
        print('PONG: ', self)

class D(B,C):
    def ping(self):
        super().ping()
        print('post-ping: ', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

# Пример 12.5
d = D()
d.pong()
C.pong(d)

# Пример 12.6. Использование super() для вызова ping (для примера 12.4)
d = D()
d.ping()
# ping: <diamond.D object at 0x10cc40630>
 #post-ping: <diamond.D object at 0x10cc40630>

 # Пример 12.7
d = D()
d.pingpong()