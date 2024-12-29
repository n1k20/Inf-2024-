from functools import *


"""
Прошу не пинать меня за это га*** код, но у меня просто тогда 
не было понимания PEP 8 и того как это не эстетично
"""
s = set()  # множество


@lru_cache(None)
def function1(x, y):
    if y == 68:  # если нужное кол-во команд
        s.add(x)
    else:
        function1(x + 3, y + 1)
        function1(x - 2, y + 1)


function1(1, 0)
print(len(s))

"""
----------------------------------------------------------------------------------
"""
@lru_cache(None)
def function2(x, y, c):  # ставим счётчик на c
    if x == y:
        a.add(c)  # добавляем в set
        return x == y
    if x > y: return 0
    return function2(x + 1, y, c + 1) + function2(x + 5, y, c + 1) + function2(x * 3, y, c + 1)  # по условию задачи


a = set()
function2(1, 227, 0)
print(min(a))  # находим минимальную длину

"""
------------------------------------------------------------------------------------
"""
# другие задачи
# 1
def function3(x, y):
    if x >= y: return x == y
    return function3(x + 2, y) + function3(x + 4, y)  + function3(x + 5, y)


for i in range(1, 1000):
    if function3(31, i) == 1001:
        print(i)

"""
--------------------------------------------------------------------------------------
"""
# 2
# на кол во различных чисел которые могут получиться
from functools import *


@lru_cache(None)
def function4(x, k):
    if k == 68:
        a.add(x)
        return
    function4(x + 1, k + 1)
    function4(x + 3, k + 1)


a = set()
function4(1, 0)
print(len(a))
