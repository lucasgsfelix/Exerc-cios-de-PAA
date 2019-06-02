def maior_elemento(v, n):

	if n == 0:
		return v[0]

	else:
		e = maior_elemento(v, n-1)
		return max(v[n], e)

v = [1,2,10,2,3,4,5,5,6]
print(maior_elemento(v, len(v)-1))