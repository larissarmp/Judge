import numpy
matrix = []
for l in range(0, 3):
    line = []
    for c in range(0, 3):
        value = int(input('valor na posição ({},{})'.format(l, c)))
        line.append(int(value))
    matrix.append(line)
#def soma_diagonal_principal(matrix):
soma_matriz_diagonal = sum(matrix[i][i] for i in range(3))
print('soma dos elementos da diagonal principal                 ', soma_matriz_diagonal)
soma_matriz_acima_diagonal = sum(matrix[i][j]
                                 for i in range(3) for j in range(3) if i < j)
print('soma dos elementos que estão acima da diagonal principal ', soma_matriz_acima_diagonal)
soma_matriz_abaixo_diagonal = sum(matrix[i][j]
                                  for i in range(3) for j in range(3) if i > j)
print('soma dos elementos que estão abaixo da diagonal principal', soma_matriz_abaixo_diagonal)
soma_diagona_secundaria = sum(matrix[i][j]
                              for i in range(3) for j in range(3) if i + j == 3 - 1)
print('soma dos elementos da diagonal secundária', soma_diagona_secundaria)
matriz_transposta = [[matrix[c][l] for c in range(3)]for l in range(3)]
for t in matriz_transposta:
   print(t)

