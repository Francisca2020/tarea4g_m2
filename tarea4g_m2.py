<<<<<<< HEAD
lista = []
=======

lista = []
numero = int(input('Ingrese numero 1: '))
lista.append(numero)

for n in range(1,15):
	numero2 = int(input('ingresa otro numero: '))
	lista.append(numero2)

	if lista[n] != lista[n-1]:
		continue
    
    # falta solicitar otro numero en caso de error
	if lista[n] == lista[n-1]:
		print('error')
		break

print(lista)
input()

'''lista = []
>>>>>>> c90ee48e11f1d1dc768eb1491cb189bc343ae6d6
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
<<<<<<< HEAD
print(lista)
=======
print(lista)
'''
>>>>>>> c90ee48e11f1d1dc768eb1491cb189bc343ae6d6
