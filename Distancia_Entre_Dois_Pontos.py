/*

Autora: Larissa Ribeiro

Problemática:

Timelimit: 1
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
*/

import  math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1, y1 = linha1
x2, y2 = linha2

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("%.4f"%distancia)
