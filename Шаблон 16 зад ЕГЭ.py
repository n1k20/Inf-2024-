import sys
from functools import lru_cache

sys.setrecursionlimit(4000)  # увеличиваем рекурсию

"-----------------------------------------------------------------------------"
"""
Тут мы без lru cache переписываем рекурсию
а дальше если мы превышаем лимит, то увеличиваем или оптимизируем 
setrecursionlimit или @lru_cache
"""


@lru_cache(None)  # сокращает код
def F(number):  # по условию задачи
    if number == 1:
        return 1
    if number > 1:
        return number * F(number - 1) - 1


"-----------------------------------------------------------------------------"
for i in range(1, 1001):
    F(i)  # если ничто не работаем, то перебираем в цикле
print(F(1000) / F(997))
