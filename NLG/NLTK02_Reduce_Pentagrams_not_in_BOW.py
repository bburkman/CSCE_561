def Reduce_Pentagrams_not_in_BOW(BOW,Pentagrams,debug):
	print ("Reduce Pentagrams not in BOW")
# Make a 1D list that is the words in BOW, so we can search it more quickly.
	Words = []
	for row in BOW:
		Words.append(row[2])

# Take out pentagrams that contain a word not in BOW
	debug.write("\n\nReduce Pentagrams\n")
	debug.write("len(Pentagrams) = %d\n" % (len(Pentagrams)))
	for row in Pentagrams:
		for word in row[1:4]:
			if word not in Words:
				row[0]=0
	for i in range (len(Pentagrams)-1,-1,-1):
		if Pentagrams[i][0]==0:
			del(Pentagrams[i]) 
	debug.write("len(Pentagrams) = %d\n" % (len(Pentagrams)))

	for row in Pentagrams:
		debug.write("%d %s %s %s %s %s\n" % (row[0], row[1], row[2], row[3], row[4], row[5]))
	debug.write("\n\n")
	return Pentagrams
