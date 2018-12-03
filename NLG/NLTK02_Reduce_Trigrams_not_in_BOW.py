def Reduce_Trigrams_not_in_BOW(BOW,Trigrams,debug):
	print ("Reduce Trigrams not in BOW")
# Make a 1D list that is the words in BOW, so we can search it more quickly.
	Words = []
	for row in BOW:
		Words.append(row[2])

# Take out trigrams that contain a word not in BOW
	debug.write("\n\nReduce Trigrams\n")
	debug.write("len(Trigrams) = %d\n" % (len(Trigrams)))
	for row in Trigrams:
		for word in row[1:4]:
			if word not in Words:
				row[0]=0
	for i in range (len(Trigrams)-1,-1,-1):
		if Trigrams[i][0]==0:
			del(Trigrams[i]) 
	debug.write("len(Trigrams) = %d\n" % (len(Trigrams)))

	for row in Trigrams:
		debug.write("%d %s %s %s\n" % (row[0], row[1], row[2], row[3]))
	debug.write("\n\n")

	return Trigrams
