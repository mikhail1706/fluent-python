class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


def make_averager():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return average


# Пример 7.10 && Пример 7.12
avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

# Пример 7.11
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

# привязка к свободной переменной
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

# Пример 7.13.
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager


# Пример 7.14.
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
