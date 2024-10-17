s = open('24_9882.txt').readline().lower()
count_b = 0
count_c = 0
left = 0
right = 0
max_s = float('+inf')
while right < len(s):
    while count_c < 128 and count_b < 128:
        right += 1
        max_s = min(max_s, right - left + 1)
        if s[right] == 'b': count_b += 1
        if s[right] == 'c': count_c += 1
    while count_c > 127 and count_b > 127:
        if s[left] == 'c': count_c -= 1
        if s[left] == 'b': count_b -= 1
        left += 1
    max_s = min(max_s, right - left + 1)
    print(right, left)
print(max_s)