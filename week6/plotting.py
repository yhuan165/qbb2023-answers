#!/usr/bin/env python

import matplotlib.pyplot as plt
import math

pca1 = []
pca2 = []
allfreq = []

for line in open("PCA10.eigenvec"):
	fields = line.rstrip('\n').split()

	pca1.append(float(fields[2]))
	pca2.append(float(fields[3]))

for line in open("afs.frq"):
	fields = line.rstrip('\n').split()
	if fields[4] == 'MAF':
		continue
	allfreq.append(float(fields[4]))

pvalues = []
smallest = 1
SNP = ''
for line in open("phenotype_gwas_resultsCB.assoc.linear"):
	fields = line.rstrip('\n').split()
	if fields[4] == 'ADD':
		pvalues.append(float(fields[8]))
		if float(fields[8]) < smallest:
			smallest = float(fields[8])
			SNP = fields[1]
	else:
		continue
print('CB',SNP)

logpvalues = []
for i in pvalues:
	logpvalues.append(-math.log10(i))

smallest1 = 1
SNP1 = ''
pvalues1 = []
for line in open("phenotype_gwas_resultsGS.assoc.linear"):
	fields = line.rstrip('\n').split()
	if fields[4] == 'ADD':
		pvalues1.append(float(fields[8]))
		if float(fields[8]) < smallest1:
			smallest1 = float(fields[8])
			SNP1 = fields[1]
	else:
		continue

print('GS',SNP1)

logpvalues1 = []
for i in pvalues1:
	logpvalues1.append(-math.log10(i))

for line in open("genotypes.vcf"):
	if line.startswith('#'):
		continue
	fields = line.rstrip('\n').split('\t')
	if fields[2] == SNP:
		info = fields[9:]

#print(len(info))

phenotype = []
for line in open("CB1908_IC50.txt"):
	fields = line.rstrip('\n').split()
	if fields[2] != 'CB1908_IC50':
		if fields[2] == 'NA':
			phenotype.append('NA')
		else: 
			phenotype.append(float(fields[2]))
	else:
		continue

#print(phenotype)

homozero = []
hetero = []
homoone = []

for i in range(0, len(info)):
	if info[i] == '0/0':
		if phenotype[i] == 'NA':
			continue
		else:
			homozero.append(phenotype[i])
	elif info[i] == '0/1':
		if phenotype[i] == 'NA':
			continue
		else:
			hetero.append(phenotype[i])
	elif info[i] == '1/1':
		if phenotype[i] == 'NA':
			continue
		else:
			homoone.append(phenotype[i])
	else:
		continue 

alldata = []
alldata.append(homozero)
alldata.append(hetero)
alldata.append(homoone)

labels = ['0/0', '0/1', '1/1']

fig, ax5 = plt.subplots()
ax5.boxplot(alldata, labels = labels)
ax5.set_xlabel("Genotype")
ax5.set_ylabel("Phenotype")
ax5.set_title("CB rs10876043 Genotype vs. Phenotype")
fig.savefig("boxplot.png")
fig.tight_layout()
plt.show()

'''
fig,ax1 = plt.subplots() 
ax1.scatter(pca1, pca2)
ax1.set_xlabel("PCA1")
ax1.set_ylabel("PCA2")
ax1.set_title("Genotype PCA")
fig.savefig("genotypePC.png")

fig,ax2 = plt.subplots()
ax2.hist(allfreq, bins = 20)
ax2.set_xlabel("Allele Frequency Spectrum")
ax2.set_ylabel("Frequency (sample)")
ax2.set_title("Overall Allele Frequency Spectrum of Samples")
fig.savefig("allelefreq.png")

CBcolor = ['red' if p > 5 else 'gray' for p in logpvalues]
GScolor = ['red' if p > 5 else 'gray' for p in logpvalues1]

fig, (ax3, ax4) = plt.subplots(2,1)
ax3.scatter(range(0,len(pvalues)),logpvalues, color = CBcolor)
ax3.set_xlabel("SNP Index")
ax3.set_ylabel("Pvalues (-log10)")
ax3.set_title("GWAS of CB1908")
ax3.axhline(y = 5, color = 'b', linestyle = '-') 

ax4.scatter(range(0,len(pvalues1)),logpvalues1, color = GScolor)
ax4.set_xlabel("SNP Index")
ax4.set_ylabel("Pvalues (-log10)")
ax4.set_title("GWAS of GS451")
ax4.axhline(y = 5, color = 'b', linestyle = '-')
fig.savefig("gwas.png") 


fig.tight_layout()
'''
