#1 при малой сложности
print('x y z w')
from itertools import product
for x, y, z, w in product([0,1], repeat=4):
    if (((x<=w) and ((not(y)) <=z)) <= ((z==x) or (w and (not(y)))))==0:
        print(x,y,z,w)
# 2 самый скучный вариант
print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a or b) and c or d or a and (not(b))) == 0:
                    print(a, b, c, d)
# 3 когда большая таблица
from itertools import *
def f(x, y, z, w, u):
    return (((z <= w) and (y == (not(x)))) <= (u == (y or z)))
for a1, a2,a3, a4, a5, a6, a7, a8 in product([0, 1], repeat = 8): # места с пустыми ячейками
    s = [(0, a1, 0, 0, 0), (0, a2, a3, 0, 0), (a4, 0, 0, 0, a5), (0, 0, a6, a7, a8)]
    if len(s) == len(set(s)):
        for p in permutations('xyzwu'):
            if [f(**dict(zip(p, r))) for r in s] == [0, 0, 0, 0]:  #кол во строк и их нумерации сверху вниз
                print(* p)
# компактный 3 вариант
from itertools import product, permutations
def f(x, y, z, w):
    return ((not(y <= (x == w))) and (z <= x))
for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    s = [(a1, 1, 1, a2), (0, a3, a4, 0), (a5, 0, 1, 0)]
    if len(set(s)) == len(s):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in s] == [1, 1, 1]:
                print(* p)

# Самый сложный варинт 2 задания
from itertools import *
def f(w, x, y, z): return ((x or (not(y))) and (not(x == z)) and w)
def g(w, x, y, z): return ((x <= y) and (y <= z) and (z <= w))
for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    s = [(1, 0, 0, a1), (1, a2, 1, a3), (0, 0, a4, a5)]
    if len(set(s)) == len(s):
        for p in permutations('wxyz', r = 4):
            for f1, f2, g1 in product([0, 1], repeat = 3):
                if [f(**dict(zip(p, r1))) for r1 in s] == [f1, f2, 1] \
                    and [g(**dict(zip(p, r2))) for r2 in s] == [1, 1, g1]:print(''.join(p))