lista = []
for i in range(1, 11):
    numeroLista = lista.append(int(input(f"digite o {i} número")))
print(lista)
listaPar = [list(filter(lambda x: x % 2 == 0, lista))]
print("os números pares", listaPar)
listaImpar = [list(filter(lambda x: (x % 2 == 1), lista))]
print("os números ímpares", listaImpar)
