from itertools import *

count = 0


def f(n):
    p = list(map(int, range(n)))
    return len(p) == len(set(p))


def g(n):
    p = ''
    for i in n:
        p += str(0 if int(i) % 2 == 0 else 1)
    return p.count('11') == 0 and p.count('00') == 0


for i in product('01234567', repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('1') == 0 and \
            f(s) == True and g(s) == True:
        count += 1
        print(s)
print(count)
