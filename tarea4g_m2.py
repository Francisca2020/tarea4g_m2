
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