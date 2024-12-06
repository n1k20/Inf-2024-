b = list(range(24, 91)) # список для В
c = list(range(47, 116)) # список для С
m = 10000 # максимальное число
for left in range(0, 100): # старт
    for right in range(left + 1, 100): # конец
        count = 0 # счётчик
        A = list(range(left, right + 1))
        for x in range(-100, 100):
            if ((x in c) <= (((not(x in A)) and (x in b)) <= (not(x in c)))) == False:
                count = 1
                break
        if count == 0:
            m = min(m, right - left + 1) # нахождение минимальной длины

