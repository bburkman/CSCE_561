def Score_Trigrams(path,Trigrams,debug):
	score=0
	for item in path:
		score += Trigrams[item][0]
	return score
