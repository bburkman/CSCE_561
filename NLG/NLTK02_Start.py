from NLTK02_Get_Corpus import Get_Corpus
from NLTK02_Frequency_Analysis import Frequency_Analysis
from NLTK02_Make_Trigrams import Make_Trigrams
from NLTK02_Make_Pentagrams import Make_Pentagrams
from NLTK02_Bag_of_Words import Bag_of_Words
from NLTK02_Reduce_Trigrams_not_in_BOW import Reduce_Trigrams_not_in_BOW
from NLTK02_Reduce_Pentagrams_not_in_BOW import Reduce_Pentagrams_not_in_BOW
from NLTK02_nGram_Adjacency_Matrix import nGram_Adjacency_Matrix
from NLTK02_Reduce_nGrams_with_no_Adjacency import Reduce_nGrams_with_no_Adjacency
from NLTK02_Load_Graph import Load_Graph
from NLTK02_WTF import WTF
from NLTK02_WTF_details import WTF_details

#Inaugural=[] # 56 lists of lists giving the ordered words in each address
#Frequency=[] # List of 3-grams
	#	Document Frequency
	# 	Corpus Frequency
	#	Word, unstemmed, case retained

debug = open("debug.txt", "w")

(Inaugural, Frequency) = Get_Corpus(debug)
partial=8
Trigrams = Make_Trigrams(Inaugural,debug,partial)
Pentagrams = Make_Pentagrams(Inaugural,debug,partial)

BOW = Bag_of_Words(Frequency,debug)

Trigrams = Reduce_Trigrams_not_in_BOW(BOW,Trigrams,debug)
(TAM) = nGram_Adjacency_Matrix(Trigrams,debug)
(Trigrams,TAM) = Reduce_nGrams_with_no_Adjacency(Trigrams,TAM,debug)

Pentagrams = Reduce_Pentagrams_not_in_BOW(BOW,Pentagrams,debug)
#(PAM) = nGram_Adjacency_Matrix(Pentagrams,debug)
#(Pentagrams,PAM) = Reduce_nGrams_with_no_Adjacency(Pentagrams,PAM,debug)

(longest_circuit, high_path) = Load_Graph(TAM,Trigrams,Pentagrams,debug)

WTF (longest_circuit, Trigrams, debug)
WTF (high_path,Trigrams, debug)
WTF_details (high_path, Trigrams, debug)



