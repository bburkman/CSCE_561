import random

def Bag_of_Words(Frequency,debug):
	random.seed(0)
	print ("Bag_of_Words")
	BOW = []
	for row in Frequency:
		if row[0]>5 and row[1]>5 and row[1]>random.randint(1,1000):
			BOW.append(row)

	BOW = sorted(BOW,key=lambda x:x[1], reverse=True)

	# Zipf
	n = len(BOW)
	for i in range (n):
		BOW[i][1] = int(n/(i+1))

	debug.write("\n\nBag of Tokens has %d Tokens\n\n" % (len(BOW)))
	for row in BOW:
		debug.write("%d %d %s\n" % (row[0], row[1], row[2]))
	debug.write("\n\n")

	return BOW
