print('Я поступлю в ИТМО')


"""как переводить системы счисления !!!!!!!!!!!!!"""

def f(n, s):
    p = 0 # счётчик
    l = len(n) - 1 # показатель степени с минус один потому что 0
    for i in range(len(n)): # цикл до длины - 1
        p += n[i] * s ** l # само произведение чисел
        l -= 1 # надо не забыть уменьшать число
    return p # answer

"""или этот метод"""

def f(n, s): #список и система счисления
    len_n = len(n) - 1 #степень числа вначале
    numbers = 0
    for i in n: #из списка
        numbers += i * (s ** len_n) #произведение каждого элемента
        len_n -= 1 #уменьшаем степень
    return numbers #выводим число из любой системы



def system(number, system): # число и система счисления
    point = '' # список или строка куда будет записываться новое число
    while number:
        point += str(number % system) # лобавляем остаток
        number //= system # уменьшаем его
    return point[::-1] # переварачиваем


# количество делителей

def simple(number): # кол в делителей числа
    l = 0
    for k in range(1, number // 2 + 1): # до половины потому что дальше нет смысла
        if number % k == 0: # если подходит
            l += 1
    return l


# условие задачи с def
for i in range(10, 2, -1):
    n = 86
    s = system(n, i)
    s = [int(g) for g in list(s)]
    l = simple(sum(s))
    if l == 2: print(i); break



# другая задача
def three(number, system): # перевод системы счисления
    point = ''
    while number:
        point += str(number % system)
        number //= system
    return point[::-1]
final = []
for i in range(1, 18):
    s = three(i, 3).zfill(3)  # zfill - длина строки
    if int(s[-2]) == int(s[-1]): final.append(i)
print(* final)



def f(n, s): #список и система счисления
    len_n = len(n) - 1 #степень числа вначале
    numbers = 0
    for i in n: #из списка
        numbers += i * (s ** len_n) #произведение каждого элемента
        len_n -= 1 #уменьшаем степень
    return numbers #выводим число из любой системы
for x in range(12, 0, -1): # по условию задачи
    s1 = f([5, 3, 7, x, 6, 2, 3], 13)
    s2 = f([6, x, 3, 5, x, 2], 13)
    if (s1 - s2) % 3 == 0:
        print(x)
        






