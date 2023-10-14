#!/usr/bin/env python

import matplotlib.pyplot as plt

# step 3.0

list_depth = []
gene_qual = []
allele_freq = []
effects_list = []

for line in open("final.vcf"):
	if line.startswith('#'):
		continue
	fields = line.rstrip('\n').split('\t')
	# print(fields)
	# break
	# grab what you need from `fields`
	
	'''
	info = fields[7]
	depth = info.split(';')[7]
	if ',' in (depth.split('=')[1]):
		multival = depth.split('=')[1]
		list_depth.append(int(multival.split(',')[0])) 
	else:
		list_depth.append(int(depth.split('=')[1]))
	'''
	sample_size = 0
	info = fields[7].split(';')
	location = list(filter(lambda x: 'NS=' in x, info))
	samplenum = location[0].split('=')[1]
	if ',' in samplenum:
		sample_size = int(samplenum.split(',')[0])
	else:
		sample_size = int(samplenum)

	data = fields[-sample_size:]

	#GT:GQ:DP:AD:RO:QR:AO:QA:GL
	for i in data:
		single = i.split(':')
		DP = single[2]
		if ',' in DP:
			list_depth.append(int(DP.split(',')[0]))
		elif '.' in DP:
			continue
		else:
			list_depth.append(int(DP))

		GQ = single[1]
		if ',' in DP:
			gene_qual.append(float(GQ.split(',')[0]))
		elif '.' in DP:
			continue
		else:
			gene_qual.append(float(GQ))

	AF = list(filter(lambda x: 'AF=' in x, info))
	AFnum = AF[0].split('=')[1]
	if ',' in AFnum:
		allele_freq.append(float(AFnum.split(',')[0]))
	else:
		allele_freq.append(float(AFnum))

	effects = fields[7].split('|')[1]
	if '&' in effects:
		effects_list.append(effects.split('&')[0])
		effects_list.append(effects.split('&')[1])
	else:
		effects_list.append(effects)




# step 3.1


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
ax1.hist(list_depth, bins = 300)
ax1.set_xlim(0,100)
ax1.set_xlabel("Read Depth")
ax1.set_ylabel("Frequency (sample)")
ax1.set_title("Distribution of read depth")


#step 3.2 

ax2.hist(gene_qual, bins = 300)
ax2.set_xlabel("Gene_qual")
ax2.set_ylabel("Frequency (sample)")
ax2.set_title("Distribution of genotype quality")

#step 3.3

ax3.hist(allele_freq, bins = 50)
ax3.set_xlabel("Allele Frequency")
ax3.set_ylabel("Frequency (sample)")
ax3.set_title("Distribution of allele frequency")

#step 3.4
effects_dict = {}
for i in set(effects_list):
	effects_dict[i] = effects_list.count(i)

effect_keys = list(effects_dict.keys())
effect_values = list(effects_dict.values())

# fig, ax4 = plt.subplots()
ax4.bar(range(len(effects_dict)), effect_values)
ax4.set_xlabel("Predicted Effects")
ax4.set_ylabel("Frequency (allele)")
ax4.set_title("Predicted efects of variants")
ax4.set_xticks(range(len(effect_keys)))
ax4.set_xticklabels(effect_keys, rotation = 'vertical',  fontsize = 7)

fig.tight_layout()
fig.savefig("multiplot.png")
plt.show()

