def Frequency_Analysis(Frequency):
	A = [0 for x in range (57)]
	for row in Frequency:
		a = row[0]
		b = row[1]
		A[a] += b
	for i in range (len(A)):
		print (i, A[i])
	print()

	stopwords = []
	with open("english_stop.txt") as file:
		for line in file:
			line = line.split() 
			stopwords.append(line[0])

	for i in range (len(Frequency)-1,-1,-1):
		a = Frequency[i][2]
		if a.lower() in stopwords:
			del(Frequency[i])
		if not a.isalpha():
			del(Frequency[i])
		
	A = [0 for x in range (57)]
	for row in Frequency:
		a = row[0]
		b = row[1]
		A[a] += b
	for i in range (len(A)):
		print (i, A[i])
	print()

	B = [0 for x in range (57)]
	for i in range (2,54,1):
		B[i] = (A[i-2] + A[i-1] + A[i] + A[i+1] + A[i+2])/5
	for i in range (len(B)):
		print (i, B[i])
	print()

	for row in Frequency:
		if row[0]>40:
			print (row)
	print()

if __name__ == "__main__":
	Frequency = []
	Frequency_Analysis(Frequency)
		
