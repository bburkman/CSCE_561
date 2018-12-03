def Make_Trigrams(Inaugural,debug,partial):
	print ("Make_Trigrams")
	T = []
	for speech in Inaugural[0:partial]:
		print (Inaugural.index(speech))
		for i in range (0,len(speech)-2,1):
			t = [1,speech[i],speech[i+1],speech[i+2]]
			found = 0
			for row in T:
				if row[1:4]==t[1:4]:
					found = 1
					row[0] += 1
			if found==0:
				T.append(t)

	T = sorted(T,key=lambda x:x[0], reverse=True)

	debug.write("\n\nTrigrams\n\n")	
	for row in T:
		debug.write("%d %s %s %s\n" % (row[0], row[1], row[2], row[3]))
	debug.write("\n\n")

	return T


			
