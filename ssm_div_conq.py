import math

#https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
## entender melhor é questão de prova

class X:

	suf = 0
	pref = 0
	soma = 0
	value = 0

def ssm(v, h, t, x):

	if h == t:

		x.suf = max(v[h], 0)
		x.pref = max(v[h], 0)
		x.soma = max(v[h], 0)

		return x

	q = math.ceil((h+t)/2) + h

	l, r = ssm(v, h, q-1, x), ssm(v, q, t, x)
	x.value = max([l.value, r.value, l.suf + r.pref ])
	x.suf = max(r.suf, l.suf + r.soma)
	x.pref = max(l.pref, r.pref + l.soma)
	x.soma = l.soma + r.soma

	return x


x = X()
v = [1,2,3,4,5,-6, 10, -4] # resp é 15
x = ssm(v, 0, len(v)-1, x)