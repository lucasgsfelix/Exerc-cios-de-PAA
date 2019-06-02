def subvetor_par(lista, n, soma):

	print(lista[n])
	if(n == 0):
		if int(lista[n]) % 2 == 0:
			return soma + 1
		else:
			return soma
	
	elif int(lista[n]) % 2 == 0:
		soma += 1
	
	return subvetor_par(lista, n-1, soma)


lista = '805438452'
soma = 0
print(subvetor_par(lista, len(lista)-1, soma))
