from ipaddress import *
"""в цикле перебираем все маски"""
for mask in range(32):
    s = ip_network(f'111.81.27.224/{mask}', 0)
    print(s, mask)
print(int('11000000', 2))
# Нахождение маски
from ipaddress import *
count = 0
"""перебираем все маски чисел"""
for x in ip_network('192.168.32.128/255.255.255.192', 0):
    s = bin(int(x))[2:].zfill(8) # переводим во 2 систему каждое число
    if s.count('1') % 2 == 0:
        count += 1
print(count)