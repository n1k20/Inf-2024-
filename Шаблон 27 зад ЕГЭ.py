print("Я поступлю в ИТМО")

"""
для линеной дороги с вычислением расстояния
"""

with open('27B_5644.txt') as file:
    n = int(file.readline())
    data = [int(k) for k in file]
sum_data = sum(data)
s = 0
sum_s = []
for i in range(n):
    s += data[i]
    sum_s.append(s)
s = 0
for i in range(n):
    s += data[i] * i
max_sum = s
for i in range(1, n):
    s += sum_s[i - 1] - (sum_data - sum_s[i - 1])
    max_sum = max(max_sum, s)
print(max_sum)

"""
метод частичных сумм
"""
with open('27-B_23.txt') as file:
    n = int(file.readline())
    s = [0]  # пустой список
    for i in range(n):
        pair = [int(i) for i in file.readline().split()]
        s = [a + b for a in s for b in pair]  # все возможные комбинации
        s = {x % 3: x for x in sorted(s)}.values()
        # составляет словарь который постоянно обновляется
    print(max(x for x in s if x % 3 != 0))

"""
По каналу связи передаётся последовательность 
целых чисел – показания прибора. В течение N мин. 
(N – натуральное число) прибор ежеминутно регистрирует 
значение напряжения (в условных единицах) в 
электрической сети и передаёт его на сервер.
Определите три таких переданных числа, чтобы между
 моментами передачи любых двух из них прошло не менее 
 K мин., а сумма этих трёх чисел была максимально 
 возможной. Запишите в ответе найденную сумму.
 """
with open('27_A_2024.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    data = [int(k) for k in file]
max_1 = [-10 ** 10] * n  # 3 списка для максимумов
max_2 = [-10 ** 10] * n
max_3 = [-10 ** 10] * n
max_1[0] = data[0]  # обозначаем начало
for i in range(n - 1):
    max_1[i] = max(max_1[i - 1], data[i])
    # прописываем максимумы чисел в первом списке
for i in range(k, n):
    max_2[i] = max(max_2[i - 1], data[i] + max_1[i - k])
    # сравниваем число предыдущее из списка с суммой числа \
    # из data и максимума числа в первом списке
for i in range(2 * k, n):
    max_3[i] = max(max_3[i - 1], max_2[i - k] + data[i])
    # тоже самое для третьего списка
print(max_3[n - 1])  # в конце выйдет максимум

with open('27.txt') as file:
    n = int(file.readline())
    data = [int(k) for k in file]
max_sum = 0  # максимальная сумма
max_left = [-1] * n  # список из n чисел \
# который будет заполнен максимумами на \
# определенных промежутках
max_left[0] = data[0]  # прирвниваем начало к началу
max_right = [-1] * n  # тоже самое для правой границы
max_right[n - 1] = data[n - 1]  # тоже но наоборот
for i in range(1, n):
    max_left[i] = max(max_left[i - 1], data[i])
    # сравниваем максиумаьные числа на промежутках
for i in range(n - 2, 0 - 1):
    max_right[i] = max(max_right[i + 1], data[i])
    # также но наоборот
for l in range(1, n - 1):
    left, mid, right = max_left[l - 1], data[l], max_right[l + 1]
    # перебираем все возможные левые правые и средний числа \
    # чтобы соотыетсвовала условию
    if left >= mid and right >= mid:
        max_sum = max(max_sum, left - 2 * mid + right)
print(max_sum)

with open('27A_6321.txt') as file:
    n, v, m = map(int, file.readline().split())
    data = []
    for i in file:
        s = [int(k) for k in i.split()]
        data.append([s[0], s[1] // v if s[1] % v == 0 else s[1] // v + 1])
data.sort()
distance = [0] * 10000  # пустой
for i in data:
    km, cont = i[0], i[1]
    distance[km] = cont  # добавляем кол во контейнеров
sum_data = sum(distance[:2 * m + 1])
max_sum = sum_data
for l in range(m + 1, 1000 - m):
    sum_data -= distance[l - m - 1]
    sum_data += distance[l + m]
    if distance[l] > 0:  # важная проверка на 0 оно должно быть его больше
        max_sum = max(max_sum, sum_data)
print(max_sum)

with open('27B_4116.txt') as file:
    n, k = map(int, file.readline().split())
    data = [int(k) for k in file]
start = finish = 0
sum_data = data[0]
while sum_data + data[finish + 1] <= k:
    sum_data += data[finish + 1]
    finish += 1
max_sum = finish - start + 1
while finish != n - 1:
    sum_data -= data[start]
    start += 1
    while finish != n - 1 and sum_data + data[finish + 1] <= k:
        sum_data += data[finish + 1]
        finish += 1
    max_sum = max(max_sum, finish - start + 1)
print(max_sum)

"""В лесничестве саженцы сосны высадили параллельными
рядами, которые пронумерованы идущими подряд натуральными
числами. Растения в каждом ряду пронумерованы натуральными
числами начиная с единицы. По данным аэрофотосъёмки известно,
 в каких рядах и на каких местах растения не прижились.
 Найдите ряд с наибольшим номером, в котором есть ровно
 13 идущих подряд свободных мест для посадки новых сосен,
 таких, что непосредственно слева и справа от них в том же
 ряду растут сосны. Гарантируется, что есть хотя бы один ряд,
 удовлетворяющий этому условию. """
with open('107_26.txt') as file:
    n = int(file.readline())
    data = [list(map(int, k.split())) for k in file]
data.sort()
max_r = 0
min_n = 0
start = data[0][0]
for i in range(n):
    if data[i][0] != start:  # чтобы ускорить процесс
        start = data[i][0]  # берем первый элемент
        numbers = []
        for l in range(i, n):  # перебирем все номера ряда
            if data[l][0] == start:
                numbers.append(data[l][-1])
            elif data[l][0] > start:
                break
        numbers.sort()  # сортируем
        answer = []
        for k in range(len(numbers) - 1):  # проходимся по разницам
            if (numbers[k + 1] - numbers[k]) == 14:
                # здесь важно что разница не 13 а 14 \
                # потому что длина индексов будет на 1 больше
                answer.append(numbers[k])
        if len(answer) > 0:
            max_r = start
            min_n = answer[0] + 1  # + 1 обязательно потому что \
            # индекс начинается с 0 а в матрице нет
print(max_r, min_n)

"""задача на акции"""
with open('26_акция.txt') as file:
    n = int(file.readline())
    data = [int(k) for k in file]
data.sort()  # делим на 4 и смотрим по индексам
print(sum(data[:n // 4 * 3]) + ((sum(data[n // 4 * 3:]) / 2)))  # первый случай
# суммма первых трех элементов + сумма последних самых больших
print(sum(data[:n // 4]) / 2 + sum(data[n // 4:]))
# здесь тоже самое


"""На вход программе подается последовательность натуральных чисел. Особым числом называется число,\
 делящееся на 3. Рассматриваются все непрерывные подпоследовательности исходной последовательности, \
 содержащие ровно 10 особых чисел. Программа должна вывести одно число – минимальную сумму элементов \
 такой подпоследовательности."""
with open('27A_2903.txt') as file:
    n = int(file.readline())
    min_sum, sum_s, count = float('+inf'), 0, 0
    list_s = [0] * n  # список со всеми позициями
    for i in range(n):
        x = int(file.readline())
        sum_s += x
        if x % 3 == 0: count += 1
        if count == 10: min_sum = min(min_sum, sum_s)
        if count >= 10: min_sum = min(min_sum, sum_s - list_s[count - 10])  # минимум суммы чисел и разница его \
        # индекса с минус 10 чтобы в разнице кол во чисел делящихся на 3 было ровно 10
        list_s[count] = max(list_s[count], sum_s)  # разметка позиции этих чисел
print(min_sum)

with open('27B_2256.txt') as file:
    n = int(file.readline())
    s = [int(file.readline()) for _ in range(n)]
max_sum = 0
sum_numbers, k = 0, 0
list_3 = [10 ** 9] * 3
for i in range(n):
    i = s[i]
    sum_numbers += i  # суммируем последовательность
    if i % 5 == 0: k += 1  # если делится
    if k % 3 == 0: max_sum = max(sum_numbers, max_sum)  # сравниваем число с суммой если кол во чисел делится на 3
    max_sum = max(max_sum, sum_numbers - list_3[k % 3])  # сравниваем числа с разницой суммы и числа в списке
    list_3[k % 3] = min(list_3[k % 3], sum_numbers)  # оставляем минимальную сумму
print(max_sum)  # answer

"""cамая сложная задача на кольцевую дорогу"""
with open('27A_3378.txt') as file:
    n, K = map(int, file.readline().split())
    s = [int(k) for k in file]
min_len = []
for i in range(n):  # прохожусь по всем правилам
    sum_s = 0
    for k in range(n):  # еще раз прохажусь
        if k == i:
            continue
        # система с линией и отрезками
        # само добавление зависит от условия задачи
        elif k < (i + n // 2) and k > i:
            sum_s += (k - i) ** 2 * s[k]
            print(k, i, (k - i) ** 2 * s[k])
        elif k > i and k > (i + n // 2):
            sum_s += (n - k + i) ** 2 * s[k]
            print(k, i, (n - k + i) ** 2 * s[k])
        elif k < i and k > (i - n // 2):
            sum_s += (n - k + i) ** 2 * s[k]
            print(k, i, (n - k + i) ** 2 * s[k])
        elif k < i and k < (i - n // 2):
            sum_s += (k + n - i) ** 2 * s[k]
            print(k, i, (k + n - i) ** 2 * s[k])
    min_len.append((sum_s, i))
min_len.sort(key=lambda x: x[0])
print(min_len)

with open('27A_2901.txt') as file:
    n = int(file.readline())
    s = [int(file.readline()) for _ in range(n)]
s.sort(reverse=True)  # сортируем не обязательно
sum_s = 0
count = 0
zero_list = [0] * 666  # список с остатками от суммы
for i in range(n):
    sum_s += s[i]  #
    if sum_s % 666 == 0:  # если делится
        count += 1
    count += zero_list[sum_s % 666]  # прибавляем на кол во остатков этого числа
    zero_list[sum_s % 666] += 1  # и сами увеличиваем число в ячейке
print(count)  # answer

with open('27-A_12479 (1).txt') as file:  # решение 27 А
    k, n = (int(file.readline()), int(file.readline()))
    s = [int(k) for k in file]
max_s = 0
for left in range(n - 1):  # левая граница
    for right in range(left + k, n):  # правая граница
        max_s = max(max_s, right - left + s[right] + s[left])
        # находим максимум из условия задачи
print(max_s)

"""Метеорологическая станция Деда Мороза ведёт наблюдение за количеством \
выпавшего снега. Показания записываются каждую минуту в течении N минут. \
Определите пару различных измерений, чтобы сумма их значений, прибавленная \
к расстоянию между этими измерениями, была максимальной. При этом расстояние \
между измерениями должно быть не менее K минут. В ответ запишите полученную сумму.
Входные данные
Даны два входных файла (файл A и файл B), каждый из которых в первой \
строке содержит натуральное число K – минимальное количество минут, \
которое должно пройти между моментами измерений показаний, а во второй – \
количество переданных показаний N (1 ≤ N ≤ 107, N > K). В каждой из \
следующих N строк находится одно неотрицательное целое число, не \
превышающее 107, которое обозначает количество выпавшего снега в \
соответствующую минуту."""

with open('27B_13622.txt') as file:
    k, n = int(file.readline()), int(file.readline())
    s = sorted([int(k) for k in file])  # сортировка по возрастанию
count = 0  # счётчик
left = 0
right = n - 1
while left < right:  # метод двух указателей
    if s[left] + s[right] > k:
        count += 2
        left += 1  # идем дальше
        right -= 1  # берем другое right
    else:
        left += 1  # другое число
print(count)  # ответ

with open('27_B_14960.txt') as f:
    n = int(f.readline())
    a = [int(t) for t in f]
h = -10 ** 6  # максимальная разница
cm, l = a[0], 0  # начальный минимум и его положение (подпосл.)
for i in range(1, n):
    d = a[i] - cm  # разница между текущим элементом и текущим минимумом
    if d >= h:  # если найденная разница больше
        # или равна макс-й, запоминаем как макс. и её начало (h2) окончание (h1)
        h = d
        h1 = l  # номер текущего минимума, начало подпосл.
        h2 = i  # номер текущего числа, конец подпосл.
    if a[i] <= cm:  # обновляем если нужно минимум
        cm = a[i]
        l = i  # и его расположение (последнее) - это возм. начало след. подпослед.
print(h2 - h1 + 1)

"""на кол - во делителей"""
with open("27B_2719.txt") as file:
    n = int(file.readline())
    count_0 = count_1 = 0  # кол во четных и нечетных
    for i in file:
        if int(i) % 2 == 0:
            count += 1  # если делится count_0 += 1 # прибавляем
        else:
            count_1 += 1  # иначе прибавдяем к нечетным
    print(count_0 * (count_0 - 1) // 2 + count_1 * (count_1 - 1) // 2)
""" на кол во делителей """
from itertools import combinations  # кол во комбинаций

with open('27A_2721.txt') as file:
    n = int(file.readline())
    s = [int(k) for k in file]  # список чисел
count = 0
for x, y in combinations(s, 2):  # перебор всех комбинаций
    if x * y % 65 == 0:  # проверка на комбинации
        count += 1
print(count)

with open('27_B_14960.txt') as file:
    n = int(file.readline())
    s = [int(k) for k in file]  # база
finish = [s[i] - s[i - 1] for i in range(1, n)]
# finish - разность последовательности
prefics = [0] * n  # начальный список для чисел
min_s = 0  # минимум числа
len_s = 0  # длина максимальной последовательности
max_s = 0  # максимальная сумма
for i in range(1, n):
    prefics[i] = prefics[i - 1] + finish[i - 1]  # разница \
    # в префиксе и числе
    if prefics[i] <= prefics[min_s]:  # если префикс \
        # меньше минимального префикса
        min_s = i  # минимальный номер
    sum_s = prefics[i] - prefics[min_s]  # разница префиксов
    if sum_s >= max_s:
        max_s = sum_s  # максимальное равно сумме
        len_s = i - min_s + 1  # итоговая длина
print(len_s)

"""другая задача"""

"""Дана последовательность N целых неотрицательных \
чисел. Необходимо определить количество пар положительных \
элементов этой последовательности, сумма которых четна, \
при этом между элементами пары есть хотя бы один ноль."""
with open('27-B_442.txt') as file:
    n = int(file.readline())
    # кол во четных и нечетных после которых были нули
    start = [0, 0]
    # кол во четных и нечетных после которых не было нулей
    finish = [0, 0]
    count = 0
    for i in range(n):
        x = int(file.readline())
        if x == 0:  # здесь происходит магия
            start[0] += finish[0]
            start[1] += finish[1]
            finish = [0, 0]
        else:
            count += start[x % 2]
            finish[x % 2] += 1
print(count)

"""на делители сложноого числа
здесь оно 5"""

with open('27B_2722.txt') as file:
    n = int(file.readline())
    count_5 = count_10 = count_0 = count_1 = 0
    for i in range(n):
        s = int(file.readline())
        if s % 5 == 0 and s % 2 == 0:
            count_10 += 1
        elif s % 5 == 0:
            count_5 += 1
        elif s % 2 == 0 and s % 5 != 0:
            count_0 += 1
        elif s % 2 != 0 and s % 5 != 0:
            count_1 += 1
print(count_10 * count_1 + count_5 * count_0 + count_10 * count_5)

with open('27A_2724 (1).txt') as file:
    n = int(file.readline())
    x = [0] * 131
    for i in range(n):
        x[int(file.readline()) % 131] += 1  # магия
count = 0
count += x[0] * (x[0] - 1) // 2  # магия
for i in range(1, 65 + 1):
    count += x[i] * x[131 - i]  # магия
print(count)

""" Дана последовательность N целых положительных чисел. Необходимо определить \
количество пар элементов этой последовательности, сумма которых делится на m = 80 \
и при этом хотя бы один элемент из пары больше b = 50000 """
with open('27A_2723.txt') as file:
    n = int(file.readline())
    s_1 = [0] * 80  # список чисел с меньшими 50_000
    s_2 = [0] * 80  # список чисел больше 50_000
    for _ in range(n):
        k = int(file.readline())
        if k > 50_000:
            s_2[k % 80] += 1  # обозначаем его \
            # остаток от деления на 80
        else:
            s_1[k % 80] += 1  # тоже
    count = 0
    count += s_2[0] * (s_2[0] - 1) // 2 + s_2[40] * (s_2[40] - 1) // 2
    # магия
    for i in range(1, 40):
        count += s_2[i] * s_2[80 - i]  # рассматриваем случаи \
        # и перемножаем пары с индексом 80 - i потому что \
        # при разности мы отнимаем а при сумме отнимаем еще элемент \
        # который в сумме дает 80
    count += s_2[0] * s_1[0] + s_2[40] * s_1[40]  # магия
    for i in range(1, 40):
        count += s_2[i] * s_1[80 - i]  # также рассматриваем все случаи
        count += s_1[i] * s_2[80 - i]
    print(count)

"""Набор данных представляет собой последовательность \
натуральных чисел. Необходимо выбрать такую \
подпоследовательность подряд идущих чисел, чтобы \
их сумма была максимальной и делилась на 1000. \
В ответе укажите её сумму. Гарантируется, что \
такая подпоследовательность существует.
"""
with open('27A_2900.txt') as file:
    n = int(file.readline())
    max_s = float('-inf')
    sum_s = 0
    list_s = [10 ** 5] * 1000  # большой список с большими числами
    for _ in range(n):
        number = int(file.readline())
        sum_s += number  # суммируем
        if sum_s % 1000 == 0:  # если подходит
            max_s = max(max_s, sum_s)  # сравниваем
        max_s = max(max_s, sum_s - list_s[sum_s % 1000])  # магия
        list_s[sum_s % 1000] = min(list_s[sum_s % 1000], sum_s)  # уменьшаем значение числа в sum_s % 1000 до sum_s
print(max_s)
