b = [k for k in range(24, 91)] # список для В
c = [k for k in range(47, 116)] # список для С
m = 10000 # максимальное число
for a_1 in range(0, 100): # старт
    for a_2 in range(a_1 + 1, 100): # конец
        count = 0 # счётчик
        A = [k for k in range(a_1, a_2 + 1)]
        for x in range(-100, 100):
            f = ((x in c) <= (((not(x in A)) and (x in b)) <= (not(x in c))))
            if f == False: # исключаем A
                count = 1
                break
        if count == 0:
            m = min(m, a_2 - a_1 + 1) # нахождение минимальной длины
print(m - 1) # нужно сделать -1
print(m) # но в других задачах -1 не надо делать
