/*
Autora: Larissa Ribeiro

Problemática:

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
*/
numero = int(input())

hora = int(numero / 60 / 60)
minuto = int((numero / 60) - (hora * 60))
segundo = int(numero - ((hora * 60 * 60) + (minuto * 60)))

print(str(hora) + ':' + str(minuto) + ':' + str(segundo))
