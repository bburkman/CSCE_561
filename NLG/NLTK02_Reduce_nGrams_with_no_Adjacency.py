# Take out n-grams that don't have any n-gram to follow them, 
#	and n-grams that don't have any n-gram to precede them, 
# 	based on having all zero's in a column or row of the adjacency matrix.  
# Also simultaneously update the adjacency matrix

# Adj should have the same number of rows and columns
#	as nGrams has rows.  
def Reduce_nGrams_with_no_Adjacency(nGrams,Adj,debug):
	print ("Reduce nGrams with no Adjacency")
	debug.write("\n\nReduce nGrams with no Adjacency\n\n")
	debug.write("Number of %d-Grams = %d\n\n" % (len(nGrams[0])-1,len(nGrams)))
	reduced = 1
	while (reduced==1):
		reduced = 0
		for i in range (len(nGrams)-1,-1,-1):
			rowones = 0
			for j in range (len(nGrams)):
				if Adj[i][j]==1:
					rowones = 1
			colones = 0
			for j in range (len(nGrams)):
				if Adj[j][i]==1:
					colones = 1
			if rowones==0 or colones==0:
				del(nGrams[i])
				del(Adj[i])
				for row in Adj:
					del(row[i])
				reduced=1

	debug.write("Reduced number of %d-Grams = %d\n\n" % (len(nGrams[0])-1,len(nGrams)))
	debug.write("Size of Adjacency Matrix = %d x %d\n\n" % (len(Adj),len(Adj[0])))
	for row in nGrams:
		debug.write("%d " % (row[0]))
		for i in range (1, len(row),1):
			debug.write("%s " % row[i])
		debug.write("\n")
	debug.write("\n\n")

	for row in Adj:
		for item in row:
			debug.write("%d " % item)
		debug.write("\n")
	debug.write("\n\n")

	return (nGrams,Adj)
