s = '4' + 100 * '6' + '4' # простая замена строки
while ('36' in s) or ('466' in s) or ('5666' in s):
    if '35' in s: s = s.replace('36', '5', 1)
    if '466' in s: s = s.replace('466', '3', 1)
    if '5666' in s: s = s.replace('5666', '4', 1)
    # просто переписываем
    # по условию задачи