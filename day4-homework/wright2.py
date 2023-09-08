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

tfixation = []
for i in range(1000):
	results = wrightfisher(0.5, 300)
	#x_positions = range(0,results[1])
	#y_positions = results[0]
	#ax.plot(x_positions, y_positions)
	tfixation.append(results[1])

ax.hist(tfixation)

ax.set_xlabel("Time to Fixation (generations)")
ax.set_ylabel("Number of Occurance")
#ax.set_ylim(0,1)
#ax.set_xlim(0)
ax.set_title("Histogram of Time to fixation for Wright Fisher Model")
fig.savefig( "HistWrightFisher2.png" )

plt.show()
