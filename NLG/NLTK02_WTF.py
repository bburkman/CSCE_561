def WTF(path, Trigrams, debug):
	for item in Trigrams[path[0]][1:4]:
		debug.write("%s " % item)
	for i in range (1,len(path),1):
		debug.write("%s " % Trigrams[path[i]][3])
	debug.write("\n\n")
