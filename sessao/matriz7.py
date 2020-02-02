import random

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
for l in range(0, 10):
    for c in range(0, 10):
        matriz[l][c] = random.randint(0, 50)
for l in range(0, 10):
    for c in range(0, 10):
        if l < c:
            matriz[l][c] = 2 * l + 7 * c - 2
        elif l == c:
            matriz[l][c] = 3 * l**2 - 1
        else:
            matriz[l][c] = 4 * l**3 - 5 * c**2 + 1
for l in range(0, 10):
    for c in range(0, 10):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
