import math
def candidatos_merge(votos, candidatos, h, t):
	q = math.ceil((t+h)/2)

	if(h == t-1):
		candidatos[votos[h]] += 1
		candidatos[votos[t]] += 1
		return candidatos

	else:

		candidatos = candidatos_merge(votos, candidatos, h, q-1)
		candidatos = candidatos_merge(votos, candidatos, q, t)
		return candidatos



votos = [1,2,3,4,5,1,1,2,2,2,2,3,1,1,4,4]
candidatos = {}
for i in votos:
	candidatos[i] = 0

print(candidatos_merge(votos, candidatos, 0, len(votos)-1))