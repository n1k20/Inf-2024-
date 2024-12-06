with open('...')as file:
    s = file.readline().lower()
# счетчик
count_b, count_c = 0, 0
# границы задачи
left, right = 0, 0
# очень большое число
max_s = float('+inf')
while right < len(s):
    while count_c < 128 and count_b < 128:      # какое-то число которые счетчики не должны превышать
        right += 1      # идем вправо
        max_s = min(max_s, right - left + 1)
        # это уже проверка по условию
        if s[right] == 'b':
            count_b += 1
        if s[right] == 'c':
            count_c += 1
    while count_c > 127 and count_b > 127:
        # если же оно стало больше, то мы увеличиваем нижний left на
        # 1 и убираем со счетчика лишние, чтобы проверить все варианты
        if s[left] == 'c':
            count_c -= 1
        if s[left] == 'b':
            count_b -= 1
        left += 1

    max_s = min(max_s, right - left + 1)       # по условию  ищим наименьшую
    print(right, left)
print(max_s)
 # самое главное понять смысл змейки