
lista = [0, 1, 2, 3, 4]


def potenciaDois(pd):
    return pd**2


def potenciaTres(pt):
    return pt**3


funcao = [potenciaDois, potenciaTres]
for i in lista:
    valor = map(lambda x: x(i), funcao)
    print(list(valor))
