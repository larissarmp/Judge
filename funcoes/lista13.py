"""""""""""""""""""""""""""""""""""""""""""""""""""

Ler 5 valores e, em seguida, mostrar a posição 
onde se encontra o maio e o menor valor

"""""""""""""""""'""""""""""""""""""""""""""""""""""'

lista = []
for i in range(1,6):
    number = lista.append(int(input(f"Insira o {i} item da lista")))
print(lista)

valor = max(lista)
posicao = lista.index(valor)
print("o valor maximo", valor, "a posição", posicao)
