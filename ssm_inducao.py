
def ssm(v, n):

	if n == 0:

		x = max(v[n], 0) # evitando pegar valores negativos

		return x, x

	x, suf = ssm(v, n-1)
	soma = max(x, v[n] + suf)
	suf = max(0, v[n] + suf)

	return soma, suf

v = [1,2,3,4,5,-6, 10, -4]
print(ssm(v, len(v)-1)[1])