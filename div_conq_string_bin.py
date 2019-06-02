import math


def merge_cont(lista, h, t):

	q = math.ceil((t+h)/2)
	if(h == t):
		cont = 0
		if(lista[h] == '0'):
			cont += 1
		return cont
	else:
		return merge_cont(lista, h, q-1) + merge_cont(lista, q, t)




lista = "1001001001000100100100100100100001"
lista = list(lista)
cont = 0
for i in lista:
	if i == '0':
		cont += 1
print(cont)
print(merge_cont(lista, 0, len(lista)-1))