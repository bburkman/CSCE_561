def Make_Pentagrams(Inaugural,debug,partial):
	print ("Make_Pentagrams")
	P = []
	for speech in Inaugural[0:partial]:
		print (Inaugural.index(speech))
		for i in range (0,len(speech)-4,1):
			p = [1,speech[i],speech[i+1],speech[i+2],speech[i+3],speech[i+4]]
			found = 0
			for row in P:
				if row[1:6]==p[1:6]:
					found = 1
					row[0] += 1
			if found==0:
				P.append(p)

	P = sorted(P,key=lambda x:x[0], reverse=True)

	debug.write("\n\nPentagrams\n\n")	
	for row in P:
		debug.write("%d %s %s %s %s %s\n" % (row[0], row[1], row[2], row[3],row[4], row[5]))
	debug.write("\n\n")

	return P


			
