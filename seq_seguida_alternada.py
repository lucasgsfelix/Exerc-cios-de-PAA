
def seq_seguida_alternada(seq):

	tabela = [(0,0)] # do primeiro elemento

	if seq[0] > seq[1]: # descrecente
		tabela.append([0, 1])
	else:
		tabela.append([1, 0]) # crescente

	for i in range(2, len(seq)):

		if(seq[i] > seq[i-1]): # se for decrescente
			tabela.append([tabela[i-1][1] + 1, 0])
		elif(seq[i] < seq[i-1]):
			tabela.append([0, tabela[i-1][0]+1])

	value = tabela[0][0]
	max_value = tabela[0][0]

	print(tabela)

	for i in range(0, len(tabela)):

		if tabela[i][0] > tabela[i][1]:
			value = tabela[i][0]
		else:
			value = tabela[i][1]

		if value > max_value:
			max_value = value

	print(max_value+1)





seq = [1,5,3,4,2,1]
seq_seguida_alternada(seq)