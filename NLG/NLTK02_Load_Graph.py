import sys

from NLTK02_Score_Trigrams import Score_Trigrams
from NLTK02_Score_Pentagrams import Score_Pentagrams
sys.path.append('/usr/local/opt/graph-tool/lib/python3.7/site-packages/')
from graph_tool.all import *

def Load_Graph(Adj,Trigrams,Pentagrams,debug):
#	print (sys.path)
	print ("Load Graph")
	g = Graph()
	e = []
	v = g.add_vertex(len(Adj))
	for i in range (len(Adj)):
		for j in range (len(Adj)):
			if Adj[i][j]==1:
				e.append(g.add_edge(g.vertex(i),g.vertex(j)))
#	graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")			
	print ("Circuits")
	Max = 0
	for c in all_circuits(g):
		if len(c)>Max:
			Max = len(c)
			longest_circuit = c
	print (len(longest_circuit), longest_circuit)
	
	
	print ("Paths")
	maxLength = 0
	maxScore = 0
	for i in range (len(Adj)):
		for j in range (len(Adj)):
			for path in all_paths(g,i,j):
				if len(path) > maxLength - 5:
					score = Score_Trigrams(path,Trigrams,debug)
					score += Score_Pentagrams(path,Trigrams,Pentagrams,debug,0)
					if score > maxScore:
						maxScore = score
						high_path = path
				if len(path) > maxLength:
					maxLength = len(path)
	print (len(high_path), maxScore,  high_path)
	Score_Pentagrams(high_path,Trigrams,Pentagrams,debug,1)	
	
	return (longest_circuit, high_path)
