import math
def menor_item(v):

	j=0	
	temp = 0
	for i in range(0, len(v)):
		if(v[i] <= 0):
			temp = v[i]
			v[i] = v[j]
			v[j] = temp
			j+=1

	# agora achando o valor positivo

	for i in range(0, len(v)):

		if math.fabs(v[i]) - 1 < len(v) and v[int(math.fabs(v[i]-1))] > 0:
			v[int(math.fabs(v[i]) -1)] = -v[int(math.fabs(v[i]) - 1)]


	print(v)

	for i in range(0, len(v)):
		if(v[i] > 0):
			return i+1

	return len(v)+1

v = [1,5000,3000,1000,4000,6000,7000,8000]
print(v)
print(menor_item(v))