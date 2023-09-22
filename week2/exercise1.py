#!/usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#Exercise 1 

def simulatecoverage(coverage, genomelen, readlen, figname):
	coveragearray = np.zeros(genomelen)
	numreads = int((coverage * genomelen)/readlen)

	low = 0
	high = genomelen - readlen

	startpos = np.random.randint(low= low, high= high + 1, size = numreads)

	for i in startpos:
		coveragearray[i: i + readlen] += 1 

	x = np.arange(0, max(coveragearray)+1)

	zerocoverage = genomelen - np.count_nonzero(coveragearray)
	zerocoveragepercent = (zerocoverage/genomelen) * 100

	print(f"in the simulation, there are {zerocoverage} bases with 0 coverage")
	print(f"this is {zerocoveragepercent}% of the genome")

	#get poisson distribution
	fish = stats.poisson.pmf(x, mu = coverage) * genomelen

	#get normal distribution
	y_normal = stats.norm.pdf(x, loc= coverage, scale= np.sqrt(coverage)) * genomelen

	fig, ax = plt.subplots()
	ax.hist(coveragearray, bins = x, label = "Simulation")
	ax.plot(x,fish, label = "Poisson")
	ax.plot(x,y_normal, label = "Normal")
	ax.set_xlabel("Coverage")
	ax.set_ylabel("Frequency (bp)")
	ax.set_title("Simulation of Sequencing Coverage")
	ax.legend()
	fig.tight_layout()
	fig.savefig(figname)

simulatecoverage(30, 1_000_000, 100, "ex1_30x_cov.png")