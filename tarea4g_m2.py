lista = []
contador = 0

while contador <= 14:
    numero = int(input("Ingrese un número: "))
    if numero in lista:
        print("Error, vuelva a ingresar un nuevo número")
    else:
        lista.append(numero)
        contador += 1
print(lista)



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
