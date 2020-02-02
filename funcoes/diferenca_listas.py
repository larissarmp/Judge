#a = [0, 1, 2, 3, 4, 5, 6]
#b = [0, 2, 4, 6, 8]
a = []
b = []
for i in range(8):
    newList = a.append(int(input(f"insira {i} numero na lista")))
for j in range(5):
    newList = b.append(int(input(f"insira {j} numero na lista")))
resultado = list(set(a).difference(set(b)))
print(resultado)