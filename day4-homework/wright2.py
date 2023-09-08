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

for i in range(30):
	results = wrightfisher(0.5, 8000)
	x_positions = range(0,results[1])
	y_positions = results[0]
	ax.plot(x_positions, y_positions)

ax.set_xlabel("Generation")
ax.set_ylabel("Allele Frequency")
ax.set_ylim(0,1)
ax.set_xlim(0)
ax.set_title("Wright Fisher Model")
fig.savefig( "WrightFisher2.png" )

plt.show()
