/*

Autora: Larissa Ribeiro

Problemática:

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
*/
valores = input().split(" ")

A, B, C = valores
A = int(A)
B = int(B)
C = int(C)

maoirAB =(A+B + abs(A-B))/2
maoirAB = (maoirAB+C + abs(maoirAB-C))/2

print("%d eh o maior" %maoirAB)
