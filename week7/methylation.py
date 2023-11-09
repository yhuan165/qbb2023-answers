#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy
#exercise 3.a

ontsite = []
bisulfitesite = []
ontcoverage = []
biscoverage = []
ontmeth = []
bismeth = []

for line in open("ONT.cpg.chr2.bedgraph"):
	fields = line.rstrip('\n').split()
	ontsite.append(float(fields[1]))
	ontmeth.append(float(fields[3]))
	ontcoverage.append(int(fields[4]))

for line in open("bisulfite.cpg.chr2.bedgraph"):
	fields = line.rstrip('\n').split()
	bisulfitesite.append(float(fields[1]))
	bismeth.append(float(fields[3]))
	biscoverage.append(int(fields[4]))

ont_set = set()
for i in range(len(ontsite)):
    if ontsite[i] not in ont_set:
        ont_set.add(ontsite[i])


bis_set = set()
for i in range(len(bisulfitesite)):
    if bisulfitesite[i] not in bis_set:
        bis_set.add(bisulfitesite[i])

diffont = ont_set.difference(bis_set)
diffbis = bis_set.difference(ont_set)

bothsite = ont_set.intersection(bis_set)

print(f"ONT unique reads: {len(diffont)} ({len(diffont)/len(ontsite) * 100})%")
print(f"Bisulfite unique reads: {len(diffbis)} ({len(diffbis)/len(bisulfitesite) * 100})%")
print(f"Shared sites: {len(bothsite)} ({len(bothsite)/(len(bisulfitesite)+len(ontsite)) * 100})%")

'''
fig, ax1= plt.subplots()
ax1.hist(ontcoverage, bins = 2000, alpha = 0.5, label = 'ONT')
ax1.set_xlabel("Coverage")
ax1.set_ylabel("Frequency (site)")
ax1.hist(biscoverage, bins = 2000, alpha = 0.5, label = 'bisulfite')
ax1.set_xlim(0,100)
ax1.set_title('Coverage Frequency Comparison between ONT and Bisfulite')
ax1.legend(loc = 'upper right')
fig.savefig("coverage.png") 
fig.tight_layout()
plt.show()
plt.close
'''

ontmethboth = []
bismethboth = []
for i in range(len(ontsite)):
	if ontsite[i] in bothsite:
		ontmethboth.append(ontmeth[i])

for j in range(len(bisulfitesite)):
	if bisulfitesite[j] in bothsite:
		bismethboth.append(bismeth[j])

corr = numpy.corrcoef(ontmethboth, bismethboth)

fig = plt.figure()
plt.imshow(numpy.log10(1 + numpy.histogram2d(ontmethboth, bismethboth, bins = 100)[0]))
plt.xlabel("ONT Methylation")
plt.ylabel("Bisulfite Methylation")
plt.title(f'Relationship of Methylation Score R= {corr[0,1]:0.3f}')
fig.savefig("methylation.png") 
plt.show()



