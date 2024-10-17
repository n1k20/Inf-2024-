from functools import lru_cache
import sys
sys.setrecursionlimit(4000) # увеличиваем рекурсию
@lru_cache(None) # сокращает код
def F(n):  # по условию задачи
    if n == 1: return 1
    if n > 1: return n * F(n - 1) - 1
for i in range(1, 1001):
    F(i) # если ничто не работаем, то перебираем в цикле
print(F(1000) / F(997))