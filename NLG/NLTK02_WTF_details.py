def WTF_details(path, Trigrams, debug):
	for item in Trigrams[path[0]][1:4]:
		debug.write("%s " % item)
	for i in range (1,len(path),1):
		debug.write("%s " % Trigrams[path[i]][3])
	debug.write("\n\n")
	score = 0
	for item in path:
		score += Trigrams[item][0]
		debug.write("%d   %d %s %s %s\n" % (score, Trigrams[item][0], Trigrams[item][1], Trigrams[item][2], Trigrams[item][3]))
	debug.write("%d\n" % score)

