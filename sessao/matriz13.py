import random
from typing import List

matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = random.randint(0, 20)
print('matriz')
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]:^3}', end='')
    print()
print('matriz transposta')
matriz_transposta = [[matriz[c][l] for c in range(4)]for l in range(4)]
for t in matriz_transposta:
        print(t)
print('matriz triângular inferior')
for l in range(0, 4):
    for c in range(0, 4):
        if l < c:
            matriz[l][c] = 0
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]:^3}', end='')
    print()





