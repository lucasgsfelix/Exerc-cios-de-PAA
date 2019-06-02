import math
nota = [1, 4, 6]
troco = 8

m = [[0 for i in range(0, troco+1)] for j in range (0, len(nota) + 1)]
nota.insert(0, 0)
inicio = 1

if 1 in nota:
	m[1] = [i for i in range(0, troco+1)]
	inicio = 2

for i in range(inicio, len(nota)):
	for j in range(0, troco+1):
		
		index_a = i-math.ceil(j/nota[i])
		if(index_a < 0): index_a = 0
		index_b = j-i-1
		if(index_b < 0): index_b = 0
		if(i==1):
			m[i][j] = max(m[i-1][j], math.floor(j/nota[i]) + m[index_a][index_b])
		else:
			m[i][j] = min(m[i-1][j], math.floor(j/nota[i]) + m[index_a][index_b])
			print("Valor: ", m[i][j], "I:", i, "J:", j, "Index A:", index_a)

print(m)