from functools import *

s = set()  # множество


@lru_cache(None)
def f(x, y):
    if y == 68:  # если нужное кол во команд
        s.add(x)
    else:
        f(x + 3, y + 1)
        f(x - 2, y + 1)


f(1, 0)
print(len(s))


@lru_cache(None)
def f(x, y, c):  # ставим счётчик на c
    if x == y:
        a.add(c)  # добавляем в set
        return x == y
    if x > y: return 0
    return f(x + 1, y, c + 1) + f(x + 5, y, c + 1) + f(x * 3, y, c + 1)  # по условию задачи


a = set()
f(1, 227, 0)
print(min(a))  # находим минимальную длину


# другие задачи
# 1
def f(x, y):
    if x >= y: return x == y
    return f(x + 2, y) + f(x + 4, y) + f(x + 5, y)


for i in range(1, 1000):
    if f(31, i) == 1001:
        print(i)
# 2
# на кол во различных чисел которые могут получиться
from functools import *


@lru_cache(None)
def f(x, k):
    if k == 68:
        a.add(x)
        return
    f(x + 1, k + 1)
    f(x + 3, k + 1)


a = set()
f(1, 0)
print(len(a))
