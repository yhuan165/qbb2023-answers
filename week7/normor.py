#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy
#exercise 3.a

ontsite = []
ont1site = []
ontcoverage = []
ont1coverage = []
ontmeth = []
ont1meth = []

for line in open("normal.ONT.chr2.bedgraph"):
	fields = line.rstrip('\n').split()
	ontsite.append(float(fields[1]))
	ontmeth.append(float(fields[3]))
	ontcoverage.append(int(fields[4]))

for line in open("tumor.ONT.chr2.bedgraph"):
	fields = line.rstrip('\n').split()
	ont1site.append(float(fields[1]))
	ont1meth.append(float(fields[3]))
	ont1coverage.append(int(fields[4]))

ont_set = set()
for i in range(len(ontsite)):
    if ontsite[i] not in ont_set:
        ont_set.add(ontsite[i])


ont1_set = set()
for i in range(len(ont1site)):
    if ont1site[i] not in ont1_set:
        ont1_set.add(ont1site[i])

diffont = ont_set.difference(ont1_set)
diffont1 = ont1_set.difference(ont_set)

bothsiteont = ont_set.intersection(ont1_set)



ontmethboth = []
ont1methboth = []
for i in range(len(ontsite)):
	if ontsite[i] in bothsiteont:
		ontmethboth.append(ontmeth[i])

for j in range(len(ont1site)):
	if ont1site[j] in bothsiteont:
		ont1methboth.append(ont1meth[j])

changeont = []
for i in range(len(ontmethboth)):
	change = ontmethboth[i] - ont1methboth[i]
	if change != 0:
		changeont.append(change)

bissite = []
bis1site = []
biscoverage = []
bis1coverage = []
bismeth = []
bis1meth = []

for line in open("normal.bisulfite.chr2.bedgraph"):
	fields = line.rstrip('\n').split()
	bissite.append(float(fields[1]))
	bismeth.append(float(fields[3]))
	biscoverage.append(int(fields[4]))

for line in open("tumor.bisulfite.chr2.bedgraph"):
	fields = line.rstrip('\n').split()
	bis1site.append(float(fields[1]))
	bis1meth.append(float(fields[3]))
	bis1coverage.append(int(fields[4]))

bis_set = set()
for i in range(len(bissite)):
    if bissite[i] not in bis_set:
        bis_set.add(bissite[i])


bis1_set = set()
for i in range(len(bis1site)):
    if bis1site[i] not in bis1_set:
        bis1_set.add(bis1site[i])

diffbis = bis_set.difference(bis1_set)
diffbis1 = bis1_set.difference(bis_set)

bothsitebis = bis_set.intersection(bis1_set)

bismethboth = []
bis1methboth = []
for i in range(len(bissite)):
	if bissite[i] in bothsitebis:
		bismethboth.append(bismeth[i])

for j in range(len(bis1site)):
	if bis1site[j] in bothsitebis:
		bis1methboth.append(bis1meth[j])

changebis = []
for i in range(len(bismethboth)):
	change = bismethboth[i] - bis1methboth[i]
	if change != 0:
		changebis.append(change)
'''
foursite = bothsitebis.intersection(bothsiteont)

fourbismeth = []
for i in range(len(bothsitebis)):
	if bothsitebis[i] in foursite:
		change = bismethboth[i] - bis1methboth[i]
		if change != 0:
			fourbismeth.append(change)

fourontmeth = []
for i in range(len(bothsiteont)):
	if bothsiteont[i] in foursite:
		change = ontmethboth[i] - ont1methboth[i]
		if change != 0:
			fourontmeth.append(change)

corr = numpy.corrcoef(fourontmeth, fourbismeth)
'''

fig, ax1= plt.subplots()
ax1.violinplot([changeont, changebis])
ax1.set_xticks([1,2])
ax1.set_xticklabels(['ONT', 'Bisulfite'])
ax1.set_xlabel("Type of sequencing")
ax1.set_ylabel("Methylation Change")
ax1.set_title(f'Distribution of methylation changes')
fig.savefig("change.png") 
fig.tight_layout()
plt.show()
plt.close


