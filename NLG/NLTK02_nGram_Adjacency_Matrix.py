def nGram_Adjacency_Matrix(nGrams,debug):
	print ("Create nGram Adjacency Matrix")
	Adj = [[0 for x in range (len(nGrams))] for y in range (len(nGrams))]
	for i in range (len(nGrams)):
		for j in range (len(nGrams)):
			fail=0
			for k in range (2,len(nGrams[0]),1):
				if nGrams[i][k]!=nGrams[j][k-1]:
					fail=1
			if fail==0:
				Adj[i][j]=1
			
	return Adj
