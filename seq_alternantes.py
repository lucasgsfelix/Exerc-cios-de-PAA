

def verifica_seq(seq):
	tabela = [(0, 0)]
	for i in range(1, len(seq)):
		if seq[i] < seq[i-1]:
			if(tabela[i-1][0] > 1):
				tabela.append(0,0)
			else:
				tabela.append((0, tabela[i-1][1]+1)) # se for descrescente
		else:
			if(tabela[i-1][1] > 1):
				tabela.append((0,0))
			else:
				tabela.append((tabela[i-1][0]+1, 0)) # se for crescente

	flag = 0
	valores = []
	valores.append(seq[0])
	print(tabela)
	for i in range(1, len(tabela)):
		if(tabela[i][0] == 1 or tabela[i][1] == 1): # então é decrescente
			valores.append(seq[i])


	print(valores)

	return len(valores)


#seq = [1,2,3,1,5] # 2, 3 , 2, 5 --> resposta
seq = [3,5,4,3,7,6,9]
valores = []
verifica_seq(seq)