#!/usr/bin/env python 

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

'''
graph = set()

for each read:
  for i in range(len(read) - k - 1):
     kmer1 = read[i: i+k]
     kmer2 = read[i+1: i+1+k]
     add "kmer1 -> kmer2" to graph

for each edge in graph:
   print edge
'''

'''
conda avtivate graphviz
dot -Tpng graph.txt > graph.png
./exercise2.py > graph.txt
'''

k = 3
graph = set()

for read in reads:
	for i in range(len(read) - k):
		kmer1 = read[i: i+k]
		kmer2 = read[i+1: i+1+k]
		graph.add(f"{kmer1} -> {kmer2}")

print("digraph {")
for edge in graph:
	print(edge)

print("}")

#piped output into a textfile through bash


