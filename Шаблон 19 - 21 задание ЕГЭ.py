""" 19 - 21"""
"""
Мега имбейшая функция для решения 19 - 21 прогой через рекурсию 
"""
def function1(s1, s2, move): # если на две кучи с действием
    if s1 + s2 >= 41: # суммируем по условию
        return move % 2 == 0 # если подходит
    if move == 0: #если ходы кончились
        return 0
    # по условию задачи
    games = [function1(s1 + 1, s2, move - 1 ),
             function1(s1,  s2 + 1, move - 1),
             function1(s1 * 2, s2, move - 1),
             function1(s1, s2 * 2, move - 1)]

    return any(games) if (move - 1) % 2 == 0 else all(games) # проверяем на ответы


print([s2 for s2 in range(1, 32) if function1(9, s2, 4) and not(function1(9, s2, 2))]) # answer


"""
если тот кто находится в промежутке проиграл в игре
"""

def function2(s, move):
    if s >= 36 and s <= 60: return move % 2 == 0
    if s > 60: return move % 2 != 0
    if move == 0: return 0
    games = [function2(s + 1, move - 1),
             function2(s * 2, move),
             function2(s * 3, move - 1)]
    return any(games) if (move - 1) % 2 == 0 else all(games)
print([s for s in range(1, 36) if function2(s, 4)])


def function3(s1, s2, move): # если на две кучи с действием
    if s1 + s2 >= 41 and s1 + s2 <= 77: # суммируем по условию
        return move % 2 == 0 # если подходит
    if s1 + s2 >= 77:
        return (move + 1) % 2 == 0
    if move == 0: #если ходы кончились
        return 0
    # по условию задачи
    games = [function3(s1 + 1, s2, move - 1 ),
             function3(s1,  s2 + 1, move - 1),
             function3(s1 * 2, s2, move - 1),
             function3(s1, s2 * 2, move - 1)]

    return any(games) if (move - 1) % 2 == 0 else all(games) # проверяем на ответы


print([s2 for s2 in range(1, 32) if function3(9, s2, 4) and not(function3(9, s2, 2))]) # answer



