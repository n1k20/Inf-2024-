s = [int(l) for l in open('17-6.txt')]
final = 0
k = 0
for i in range(0, len(s) - 2):
    if bin(s[i])[2:].count('1') == 3 and bin(s[i + 1])[2:].count('1') == 3 \
            and bin(s[i + 2])[2:].count('1') == 3:
        final += max(s[i], s[i + 1], s[i + 2])
        k += 1
print(k, final)
