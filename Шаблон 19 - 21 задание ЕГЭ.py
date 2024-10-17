def f(s1, s2, move): # если на две кучи с действием
    if s1 + s2 >= 41: # суммируем по условию
        return move % 2 == 0 # если подходит
    if move == 0: #если ходы кончились
        return 0
    # по условию задачи
    games = [f(s1 + 1, s2, move - 1 ), \
             f(s1,  s2 + 1, move - 1), \
             f(s1 * 2, s2, move - 1), \
             f(s1, s2 * 2, move - 1)]

    return any(games) if (move - 1) % 2 == 0 else all(games) # проверяем на ответы


print([s2 for s2 in range(1, 32) if f(9, s2, 4) and not(f(9, s2, 2))]) # answer

"""если тот кто находится в промежутке проиграл в игре"""

def f(s, move):
    if s >= 36 and s <= 60: return move % 2 == 0
    if s > 60: return move % 2 != 0
    if move == 0: return 0
    games = [f(s + 1, move - 1), f(s * 2, move), f(s * 3, move - 1)]
    return any(games) if (move - 1) % 2 == 0 else all(games)
print([s for s in range(1, 36) if f(s, 4)])


def f(s1, s2, move): # если на две кучи с действием
    if s1 + s2 >= 41 and s1 + s2 <= 77: # суммируем по условию
        return move % 2 == 0 # если подходит
    if s1 + s2 >= 77:
        return (move + 1) % 2 == 0
    if move == 0: #если ходы кончились
        return 0
    # по условию задачи
    games = [f(s1 + 1, s2, move - 1 ), \
             f(s1,  s2 + 1, move - 1), \
             f(s1 * 2, s2, move - 1), \
             f(s1, s2 * 2, move - 1)]

    return any(games) if (move - 1) % 2 == 0 else all(games) # проверяем на ответы


print([s2 for s2 in range(1, 32) if f(9, s2, 4) and not(f(9, s2, 2))]) # answer



