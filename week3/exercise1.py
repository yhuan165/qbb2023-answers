#!/usr/bin/env python

import numpy as np
import sys
import pandas as pd
from fasta import readFASTA

#./exercise1.py './needleman-wunsch/CTCF_38_M27_DNA.fna' './needleman-wunsch/HOXD70.txt' -10 'align.txt'

fastafile = sys.argv[1]
scoringfile = sys.argv[2]
penalty = float(sys.argv[3])
alignpath = sys.argv[4]

 # should be negative

input_sequences = readFASTA(open(fastafile))

# testing
# sequence1 = 'TACGATTA'
# sequence2 = 'ATTAACTTA'


seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]


#print(sequence1)
#print(sequence2)

#import scoring matrix
scoring_matrix = pd.read_csv(scoringfile, sep='\s+')
#print(scoring_matrix)

#1.2
f_matrix = np.zeros((len(sequence1)+1,len(sequence2)+1))
traceback = np.zeros((len(sequence1)+1,len(sequence2)+1), dtype = str)

#1.3
for i in range(len(sequence1)+1):
	f_matrix[i,0] = i * penalty
	traceback[i,0] = 'v'

for j in range(len(sequence2)+1):
	f_matrix[0,j] = j * penalty
	traceback[0,j] = 'h'

for i in range(1, f_matrix.shape[0]):
	for j in range(1, f_matrix.shape[1]):
		d = f_matrix[i-1,j-1] + float(scoring_matrix.loc[sequence1[i-1],sequence2[j-1]])
		h = f_matrix[i, j-1] + penalty
		v = f_matrix[i-1, j] + penalty

		f_matrix[i,j] = max(d,h,v)

		if f_matrix[i,j] == d:
			traceback[i,j] = 'd'
		elif f_matrix[i,j] == h:
			traceback[i,j] = 'h'
		else: 
			traceback[i,j] = 'v'

#print(f_matrix)
#print(traceback)
print("score of alignment:",f_matrix[i,j])
#1.4
#i = f_matrix.shape[0] 
#j = f_matrix.shape[1] 
align1 = ''
align2 = ''

while i != 0 or j != 0:
	if traceback[i,j] == 'd':
		align1 = sequence1[i-1] + align1 
		align2 = sequence2[j-1] + align2
		i -= 1
		j -= 1
	elif traceback[i,j] == 'h':
		align1 = '-' + align1
		align2 = sequence2[j-1] + align2
		j -= 1
	else: 
		align1 = sequence1[i-1] + align1
		align2 = '-' + align2
		i -= 1

print("number of gaps in sequence 1:", align1.count('-'))
print("number of gaps in sequence 2:", align2.count('-'))

#1.5
f = open(alignpath, "w")
L = ["Sequence 1 alignment: ", align1,"\nSequence 2 alignment: ", align2]

f.writelines(L)

f.close()

