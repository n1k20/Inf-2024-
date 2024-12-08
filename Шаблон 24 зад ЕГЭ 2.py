with open('...') as file:
    s = file.readline().lower()
min_len = float('+inf')
count = 0
left = 0
right = -1
while right < len(s) and left < len(s):
    if count >= 500:
        min_len = min(min_len, right - left + 1)
        if s[left] == 'x':
            count -= 1
        left += 1
    else:
        right += 1
        if right == len(s):
            break
        if s[right] == 'y':
            count = 0
            left = right
        if s[right] == 'x':
            count += 1
print(min_len)


with open('24.txt') as file:
    s = file.readline().strip().lower()
c = 0
ans = -1
for i in range(1, len(s)):
    if s[i] == 'r':
        if s[i - 1] == 'q':
            c += 1
        else:
            c = 1
    elif s[i] == 's':
        if s[i - 1] == 'r':
            c += 1
        else:
            c = 1
    elif s[i] == 'q':
        if s[i - 1] == 's':
            c += 1
        else:
            c = 1
    else:
        c = 0
    ans = max(ans, c)
print(ans)


# условие внизу
with open('24_5444.txt') as file:
    s = file.readline().lower()
max_s = 0
for start in (0, 1, 2):  # разное начало
    count = 0
    for i in range(start, len(s), 3):  # с шагом в \
        # 3 и перебираем
        if len(set(s[i:i + 3])) == 1:  # если они равны
            count += 3  # плюс 3 потому что шаг 3
        else:
            count = 0  # обнуляем
        max_s = max(max_s, count)  # находим максимум
print(max_s)


"""
Текстовый файл содержит строку из символов A, B, C, D, E, F.
Найдите максимальную длину подстроки, которая состоит из подряд идущих троек одинаковых символов.
Например, в строке BBCDDDEEEFGGGEEEDDDDK такая подстрока GGGEEEDDD. Следовательно, ответ будет 9.
"""

with open('24_3900.txt') as file:
    s = file.readline().lower().split('a')[1:-1]
    # сплитуем по А чтобы найти отрезки
max_len = 0  #
for w, x, y in zip(s, s[1:], s[2:]):  # гениально делаем zip
    # чтобы линейно брать тройки
    if w == x == y:  # сравниваем
        max_len = max(max_len, len(w) * 3 + 4)  # находим максимум
print(max_len)  # answer


"""
Текстовый файл состоит не более, чем из 106 символов 
из набора A, B, C, D, E, F. Найдите максимальную длину строки 
вида А*А*А*А, где между буквами А расположены одинаковые группы 
символов, не содержащие букв А. Например, в строке 
BDADBADBADBABDAFABDA такая подстрока ADBADBADBA (длина 10).
"""


"""
метод двух указателей
"""
s = open('24_10105.txt').readline().lower()
left = max_s = count = 0
for right in range(len(s) - 1):
    if s[right] == 't':
        count += 1
    while count > 100:
        if s[left] == 't':
            count -= 1
        left += 1
    if count == 100:
        max_s = max(max_s, right - left + 1)
print(max_s)

# другой вариант 24 зад
# вариант Дамира
s = open('24_9882.txt').readline().lower()  # открытый файл
answer_len = 10 ** 6  # максимальное число
finish = []  # список для индексов
prev_index = 0
for index in range(len(s)):
    letter = s[index]  # перебор чисел
    if letter in 'bc':  # если соответствует условию
        finish.append(index)  # добавление индекса
        prev_index = index  # значение последнего индекса
        if len(finish) == 127:  # если есть 127 В и С
            answer_len = min(answer_len, finish[-1] - finish[0])
            """минимальная длина """
            finish.pop(0)  # удаление начального индекса
print(answer_len + 1)  # ответ + 1 для букв В и С

"""
метод с заменой переменной
"""
with open('24_4643.txt') as file:
    final = ''
    for i in file: final += str(i)
    final = final.replace('12A', 'X')  # делаем обыкновенную замену
    final = final.replace('12B', 'X')
    final = final.replace('21A', 'X')
    final = final.replace('21B', 'X')
    the_end = []
    count = 0
    for i in final:  # ищем иксы
        if i == 'X':
            count += 1
        else:
            the_end.append(count);
            count = 0
    print(max(the_end) * 3)

# другой сложный вариант 24

s = open('24_10131.txt').readline()

# словарь для префиксов
p = {}
c = max_s = 0

for i in range(len(s)):
    # если в строке равное количество букв
    # A и B, то c будет равно 0
    c += {'A': 1, 'B': -1}.get(s[i], 0)

    # проверим особый случай, когда
    # не надо убирать префикс
    if c == 0:
        max_s = i + 1

    # ищем наибольшую длину с равным
    # количеством букв A и B
    max_s = max(max_s, i - p.get(c, 10 ** 50))

    # так как мы ищем максимальную длину,
    # префикс должен быть минимальным,
    # поэтому сохраняем первую строку
    # с суммой c
    p[c] = p.get(c, i)
print(max_s)
print(p)
