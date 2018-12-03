def Score_Pentagrams(path,Trigrams,Pentagrams,debug,switch):
	score=0
	text = []
	text.append(Trigrams[path[0]][1])
	text.append(Trigrams[path[0]][2])
	text.append(Trigrams[path[0]][3])
	for index in path [1:]:
		text.append(Trigrams[index][3])

	if switch==1:
		for word in text:
			debug.write("%s " % word)
		debug.write("\n")
		for index in path:
			for word in Trigrams[index]:
				debug.write("%s " % word)
			debug.write("\n")
		debug.write("\n")

	P = []
	for i in range (len(text)-4):
		P = []
		for j in range (5):
			P.append(text[i+j])
		for j in range (len(Pentagrams)):
			if P==Pentagrams[j][1:6]:
				score += Pentagrams[j][0]
				if switch==1:
					for word in Pentagrams[j]:
						debug.write("%s " % word)
					debug.write("\n")
	if switch==1:
		debug.write("\n")	

	return score
