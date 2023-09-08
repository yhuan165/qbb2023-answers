#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def wrightfisher(af,pop):

	aflist = []

	while af > 0 and af < 1:
		success = np.random.binomial(2*pop, af)
		af = success/(2*pop)
		aflist.append(af)

	numgen = len(aflist)
	return [aflist, numgen]


fig, ax = plt.subplots()

'''
avgtimelist = []
popsize = []
for i in range(5):
	randomnum = np.random.randint(50,200)
	popsize.append(randomnum)
	tfixation = []
	for i in range(50):
		results = wrightfisher(0.5, randomnum)
		tfixation.append(results[1])

	avgtime = sum(tfixation)/len(tfixation)
	avgtimelist.append(avgtime)

ax.scatter(popsize,avgtimelist)
ax.set_xlabel("Population Size")
ax.set_ylabel("Average Time to Fixation")
ax.set_title("Population effect on time to fixation")
fig.savefig( "ChangingPopulation.png" )
'''

avgtimelist = []
freq = []
for i in range(1000):
	randomnum = np.random.uniform(0,1)
	freq.append(randomnum)
	tfixation = []
	for i in range(50):
		results = wrightfisher(randomnum, 1000)
		tfixation.append(results[1])

	avgtime = sum(tfixation)/len(tfixation)
	avgtimelist.append(avgtime)

ax.scatter(freq,avgtimelist)
ax.set_xlabel("Allele Frequency")
ax.set_ylabel("Average Time to Fixation")
ax.set_title("Allele Frequency effect on time to fixation")
fig.savefig( "ChangingFrequency.png" )


plt.show()

