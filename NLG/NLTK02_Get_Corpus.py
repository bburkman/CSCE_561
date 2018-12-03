import nltk
from nltk.corpus import inaugural
#from nltk.corpus import genesis

def Get_Corpus(debug):
	print ("Get_Corpus")

# Inaugural is a list of lists.  
# 	Each row is one of 56 inaugural addresses.
#	Each row is a sequential list of the words and punctuation marks
#		 in the speech.  
	Inaugural=[]
	i=0
	for fileid in inaugural.fileids():
		Inaugural.append(inaugural.words(fileid))
#	for fileid in genesis.fileids():
#		Inaugural.append(genesis.words(fileid))
		print (i, fileid)
		debug.write("%d %s\n" % (i, fileid))
		i += 1
	
	Words = []
	for speech in Inaugural:
		words = list(set(speech))
		Words = list(set(words+Words))
	
	Frequency = []
	for word in Words:
		Frequency.append([0,0,word])
	for speech in Inaugural:
		for word in speech:
			i = Words.index(word)
			Frequency[i][1] += 1
		S = list(set(speech))
		for word in S:
			i = Words.index(word)
			Frequency[i][0] += 1
	
#	Frequency = sorted(Frequency,key=lambda x:x[2], reverse=True)
	Frequency = sorted(Frequency,key=lambda x:x[1], reverse=True)
	Frequency = sorted(Frequency,key=lambda x:x[0], reverse=True)

	debug.write("\n\nSpeeches\n\n")
	for speech in Inaugural:
		for word in speech:
			debug.write ("%s " % (word))
		debug.write ("\n\n")
	debug.write("\n\n")

	debug.write("\n\nFrequency\n\n")
	for row in Frequency:
		debug.write("%d %d %s\n" % (row[0], row[1], row[2]))
	debug.write("\n\n")

	return (Inaugural, Frequency)
