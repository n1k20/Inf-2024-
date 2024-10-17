count = int(input())
sum_True = 0
data = []
for _ in range(count):
    answer = str(input())
    sum_True += 1 if answer.split()[-1] == 'Correct' and answer not in data else 0
    data.append(answer)
print(f'Верно решили {sum_True} учащихся')
print(f'Из всех попыток {int(sum_True / len(set(data)) * 100)}% верных')
