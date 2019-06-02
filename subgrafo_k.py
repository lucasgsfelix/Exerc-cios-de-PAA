import igraph

def grau_minimo(g):

	lista = [len(g.neighbors(k)) for k in g.vs]
	return min(lista)

def subgrafo_grau_k(g, k, n):
	
	if k==0 or g.vcount() == 0 or grau_minimo(g) >= k or n==0:
		return g
	i=n
	while(i>=0):
		if len(g.neighbors(g.vs[i])) < k:
			g.delete_vertices(g.vs[i])
			n-=1
			i-=1
		else:
			return subgrafo_grau_k(g, k, n-1)

	return g

g = igraph.Graph()
g = g.Read_Ncol("entrada_subgrafo_k.txt", directed = False)
k = 3
subgrafo_grau_k(g, k, g.vcount()-1)