"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
vetor com 5 posiçoes 
um codigo

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = []
for i in range(1, 6):
    number = lista.append(float(input(f"Digite o {i} valor ")))
#print(lista)
#lista.sort()
#print(lista)
codigo = int(input("digite o código"))
if codigo == 0:
    print("código 0")
elif codigo == 1:
    print("lista ondem direta", lista)
elif codigo == 2:
    lista.sort(reverse=True)
    print("lista na ondem inverda", lista)
else:
    print("código inválido")
