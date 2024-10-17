from itertools import permutations 

t = '12 15 16 21 24 25 34 42 43 45 51 52 54 56 61 65'

g= 'аб ба ав ва бв вб бг гб гд дг де ед вд дв вг гв'

for i in permutations('абвгде'):
    graph = t
    for k in range(1, 7):
        graph = graph.replace(str(k), i[k - 1])
    if set(graph.split()) == set(g.split()):
        print('1 2 3 4 5 6')
        print(*i)
# не буду этим пользоваться