with open('9.txt') as file: # лучше решать 9 задание прогой
    final = 0
    for i in file:
        a, b, c, d = sorted([int(k) for k in i.split()])
    """классический перевод чисел """
        if d ** 3 > 2 * a * b * c and a > 10 and c > 10 \
                and b > 10 and d > 10:
            final += 1
    print(final)
