import random

matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]
print('\n', "  B    I    N   G   O ", '\n')
print('_'*28, '\n')
for i in range(0, 5):
    for j in range(0, 5):
        matriz[i][j] = random.randint(0, 99)

for i in range(0, 5):
    for j in range(0, 5):
        print(f'{matriz[i][j]:^5}', end=' ')
    print()
print('_'*28, '\n')

