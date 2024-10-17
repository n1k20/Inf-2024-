from collections import Counter # импорт функции для моды
with open('17_3738.txt') as file:
    s = [int(k) for k in file]
middle = [sum(map(int, str(x))) for a, x, b in zip(s, s[1:], s[2:])
          if sum(map(int, str(a))) == sum(map(int, str(b)))]
finish = Counter(middle) # для списка
print(finish)
print(len(middle), finish.most_common()[0][0]) # находит моду в списке

# другие задачи
# 1
f = list(map(int, open('2.txt').read().split()))
l = 0
g = []
for k in range(0, len(f)):
    if (abs(f[k]) % 9 == 0 and abs(f[k - 1]) % 9 != 0 and oct(f[k - 1])[-1] == '3') or \
            (abs(f[k - 1]) % 9 == 0 and abs(f[k]) % 9 != 0 and oct(f[k])[-1] == '3'):
        g.append(max(f[k - 1], f[k]))
        l += 1
print(l, max(g))
# 2
s = list(map(int, open('17-4.txt').read().split()))
f = []
for i in range(0, len(s)):
    if s[i] % 31 == 0 or s[i] % 47 == 0 or s[i] % 53 == 0:
        bycva_1 = s[i]
        test_1 = []
        while bycva_1 > 3:
            test_1.append(str(bycva_1 % 3))
            bycva_1 //= 3
        test_1.append(str(bycva_1))
        test_1.reverse()
        test_1 = ''.join(test_1)
        bycva_2 = s[i]
        test_2 = []
        while bycva_2 > 5:
            test_2.append(str(bycva_2 % 5))
            bycva_2 //= 5
        test_2.append(str(bycva_2))
        test_2.reverse()
        test_2 = ''.join(test_2)
        if str(test_1)[-1] == str(test_2)[-1]:
            f.append(s[i])
print(len(f), min(f))


