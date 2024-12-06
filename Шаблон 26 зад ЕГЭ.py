"""
В магазине для упаковки подарков есть N кубических коробок. 
Самой интересной считается упаковка подарка по принципу 
матрешки – подарок упаковывается в одну из коробок, 
та, в свою очередь, в другую коробку и т.д. Одну коробку 
можно поместить в другую, если длина её стороны хотя бы 
на 3 единицы меньше длины стороны другой коробки. 
Определите наибольшее количество коробок, которое 
можно использовать для упаковки одного подарка, 
и максимально возможную длину стороны самой 
маленькой коробки, где будет находиться подарок. 
Размер подарка позволяет поместить его в самую 
маленькую коробку."""
with open('...') as file:
    n = int(file.readline())
    data = [int(k) for k in file]
data.sort(reverse=True)
max_len = float('-inf')
for i in range(n):
    max_count = [data[i]]
    for i in range(n):
        if max_count[-1] - data[i] >= 3:
            max_count.append(data[i])
    print(min(max_count), len(max_count))

"""
На грузовом судне необходимо перевезти 
контейнеры, имеющие одинаковый габарит и 
разные массы (некоторые контейнеры могут 
иметь одинаковую массу). Общая масса всех 
контейнеров превышает грузоподъёмность судна. 
Количество грузовых мест на судне не меньше 
количества контейнеров, назначенных к перевозке. 
Какое максимальное количество контейнеров можно 
перевезти за один рейс и какова масса самого 
тяжёлого контейнера среди всех контейнеров, 
которые можно перевезти за один рейс
"""

with open('26 (1).txt') as file:
    s, n = map(int, file.readline().split())
    data = sorted([int(k) for k in file])
sum_s = 0
for count in range(n):
    if (sum_s + data[count]) > s:
        # просто перебираем с минимальной суммы
        break
    sum_s += data[count]
print(count)  # выводим всю длину
zapas = s - sum_s  # запас
for i in range(n):  # снова перебор
    if data[i] - data[count - 1] <= zapas:
        # если разница между числом и номером с минус один \
        # меньше, либо равно запасу то он
        the_end = data[i]  # и является концом
print(the_end)

"""
В сервисе «Капчеломы» N работников разгадывают
капчи. Разгадывание каждой капчи каждым работником
занимает ровно 60 секунд, разгадывать две капчи
одновременно нельзя.Имеется K запросов на прохождение 
капчи, про каждый известно время в секундах от начала 
рабочего дня, когда этот запрос появляется. 
Если не взять запрос в работу сразу же, 
его перехватывает сервис конкурентов, 
и выполнить его уже нельзя.
"""

with open('...') as file:
    n, r = map(int, file.readline().split())
    s = [int(k) for k in file]
s.sort()
sum_s = 0
min_time = 10 ** 11
for i in range(n):
    b = [s[0]]  # берем первый элемент капчи
    s[0] = -1  # обозначаем индекс в списке
    for j in range(1, len(s)):
        if s[j] >= b[-1] + 60:
            # если время капчи больше капчи прошлой + 60 \
            # секунд на выполнение
            b.append(s[j])  # добавляем файл
            s[j] = -1
    sum_s += len(b)  # длина выполнения капч
    min_time = min(min_time, len(b))  # min \
    # разгадка капч
    s = [k for k in s if k != -1]  # обновление файлов
print(s, n)

with open('...') as file:
    k = 0
    s = []
    for i in file:
        if k == 0:
            start = [int(k) for k in i.split()]
            k += 1
        else:
            s.append(int(i))
    s = sorted(s)
    count = 0
    l = 0
    final = []
    while count + s[l + 1] < start[0] and l + 1 < start[-1]:
        count += s[l]
        l += 1
        final.append(s[l])
    print(final)
    print(l, max(final))

with open('...') as file:
    point, time = map(int, file.readline().split())  # находим данные для решения
    s = [(int(k.split()[0]), int(k.split()[0]) + int(k.split()[1])) for k in file]
s.sort(key=lambda t: (t[1], t[0]))  # метод сортировки кортежей
start = -1
choice = []
for a, b, in s:  # дальше по условию задачи
    if a >= start:
        start = b
        choice.append((a, b))
print(len(choice) * point)
start = choice[-2][1]
last_min = 10 ** 100
for x, y in s:
    if x >= start:
        if x < last_min:
            last_min = x
print(last_min)

with open('...') as file:
    count = map(int, file.readline().split())
    time_day = [0 for k in range(0, 1441)]  # список с нулями
    for i in file:
        start, final = map(int, i.split())
        for k in range(start, final + 1):
            time_day[k] = 1
    time = ''
    for l in time_day:
        time += str(l)
    yess = time.split('1')
    count_yess = 0
    for i in yess:
        if i != '':
            count_yess += 1
    print(count_yess)
    counter = 0
    the_end = [1 for k in time_day if k == 0]
    print(sum(the_end) - 1)

with open('...') as file:
    counter = int(file.readline())  # counter numbers in list
    time = [list(map(int, i.split())) for i in file]  # all time
time.sort(key=lambda i: i[-1])  # sorting by last
taken = [time[0]]  # first the end
for start, finish in time[1:]:
    if start >= taken[-1][-1]:
        taken.append((start, finish))
longest = 0  # len last
for start, finish in taken[1:]:
    if start >= taken[-2][1]:
        longest = max(longest, start - taken[-2][1])  # between holidays
print(len(taken), longest)  # answer

"""
или можно так
"""
with open('...') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file]
data.sort(key=lambda x: x[-1])
time = [(data[0][-1])]
for i in range(1, n):
    start = data[i][0]
    finish = data[i][1]
    if time[-1] <= start: time.append(finish)
max_len = 0
for i in data:
    if time[-2] <= i[0]:
        max_len = max(max_len, i[0])
print(len(time), max_len - time[-2])

with open('...') as file:
    counter = int(file.readline())  # кол во отрезков
    favorite_music, other_music = [], []
    for i in range(counter):
        start, final, number = map(int, file.readline().split())
        if number == 1:
            favorite_music.append((start, start + final))  # начало и длина до конца
        else:
            other_music.append((start, start + final))  # то же самое
favorite_music = sorted(favorite_music)  # сортируем данные
other_music = sorted(other_music, key=lambda x: x[1])  # сортировка по последнему числу

"""------------------------------------------------------------------------------------------"""


def check(start, final):
    global favorute_music  # открывает переменные вне функции
    for start_1, final_1 in favorite_music:
        if start_1 > final:
            return True
        if start < final_1 and final > start_1:
            return False


used_other_music = []
for start, final in other_music:
    if len(used_other_music) > 0:
        if start >= used_other_music[-1][1] and check(start, final):
            used_other_music.append((start, final))
    elif check(start, final):
        used_other_music.append((start, final))
print(len(used_other_music) + len(favorite_music))  #
last_music = [i for i in other_music if check(i[0], i[1]) and i[0] >= used_other_music[-2][1]]
print(last_music[-1][1])  # ответ

"""--------------------------------------------------------------------------------------------------"""

with open('27-B_108.txt') as file:
    n = file.readline()
    min_s = float('+inf')
    sum_s = 0
    for i in file:
        x, y = map(int, i.split())
        if x < y:
            x, y = y, x  # выравниваем числа
        sum_s += x  # суммируем
        if (x - y) % 5 != 0 and (x - y) < min_s:
            min_s = x - y  # минимальная разница чтобы не делилась
if sum_s % 5 == 0:  # если неделится
    sum_s -= min_s  # то отнимаем минимум
print(sum_s)

"""
На вход программы поступает последовательность из N пар 
целых положительных чисел. Необходимо выбрать из каждой пары 
число таким образом, чтобы сумма выбранных чисел не делилась 
на 5, при этом была максимальной возможной. 
"""


def max_del(n):
    for k in range(n // 2, 1, -1):
        if n % k == 0:
            break
    if k % 100 == 19:
        return k
    else:
        return 10 ** 6


for i in range(224466, 664422 + 1):
    if i % 5 == 0 and i % 7 == 0 and i % 13 == 0 and i % (5 ** 2) != 0 and i % (7 ** 2) != 0 and i % (
            13 ** 2) != 0 and max_del(i) <= 10 ** 5:
        print(i, max_del(i))
