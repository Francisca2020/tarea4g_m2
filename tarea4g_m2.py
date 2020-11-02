lista = []
lista2 = []

for x in range(3, 26):
    lista2.append(x)


for n in range(2, 501):
    lista.append(n)
    if n % 2 == 0 and n != 2:
        lista.remove(n)
print(lista)
print()
for numero2 in lista2:
    for numero in lista:
        if numero % numero2 == 0:
            lista.remove(numero)


print()
print(lista)