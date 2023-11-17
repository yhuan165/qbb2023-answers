#!/usr/bin/env python

import sys

baitfile, washU, output = sys.argv[1:4]

baitdict = {}
for line in open(baitfile):
	fields = line.rstrip('\n').split()
	baitdict[str(fields[1]+','+fields[2])] = fields[4]

# print(baitdict)

frag1 = []
frag2 = []
interaction = []
for line in open(washU):
	fields = line.rstrip('\n').split()
	frag1.append(fields[0])
	frag2.append(fields[1])
	interaction.append(float(fields[2]))

chrom = []
chromStart = []
chromEnd = []
name = []
score = []
value = []
exp = []
color = []
sourceChrom = []
sourceStart = []
sourceEnd = []
sourceName = []
sourceStrand = []
targetChrom = []
targetStart = []
targetEnd = []
targetName = []
targetStrand = []

for i in range(len(frag1)):
	chrom.append(frag1[i].split(',')[0])
	chromStart.append(min(int(frag1[i].split(',')[1]),int(frag1[i].split(',')[2]),int(frag2[i].split(',')[1]),int(frag2[i].split(',')[2])))
	chromEnd.append(max(int(frag1[i].split(',')[1]),int(frag1[i].split(',')[2]),int(frag2[i].split(',')[1]),int(frag2[i].split(',')[2])))
	name.append('.')
	score.append(int(interaction[i]/max(interaction))*1000)
	value.append(interaction[i])
	exp.append('.')
	color.append('0')
	if (frag1[i][6:] in baitdict.keys()) and (frag2[i][6:] in baitdict.keys()):
		sourceChrom.append(frag1[i].split(',')[0])
		sourceStart.append(int(frag1[i].split(',')[1]))
		sourceEnd.append(int(frag1[i].split(',')[2]))
		sourceName.append(baitdict.get(frag1[i][6:]))
		sourceStrand.append('+')
		targetChrom.append(frag2[i].split(',')[0])
		targetStart.append(int(frag2[i].split(',')[1]))
		targetEnd.append(int(frag2[i].split(',')[2]))
		targetName.append(baitdict.get(frag2[i][6:]))
		targetStrand.append('+')
	elif (frag1[i][6:] in baitdict.keys()) and (frag2[i][6:] not in baitdict.keys()):
		sourceChrom.append(frag1[i].split(',')[0])
		sourceStart.append(int(frag1[i].split(',')[1]))
		sourceEnd.append(int(frag1[i].split(',')[2]))
		sourceName.append(baitdict.get(frag1[i][6:]))
		sourceStrand.append('+')
		targetChrom.append(frag2[i].split(',')[0])
		targetStart.append(int(frag2[i].split(',')[1]))
		targetEnd.append(int(frag2[i].split(',')[2]))
		targetName.append('.')
		targetStrand.append('-')
	elif (frag1[i][6:] not in baitdict.keys()) and (frag2[i][6:] in baitdict.keys()):
		sourceChrom.append(frag2[i].split(',')[0])
		sourceStart.append(int(frag2[i].split(',')[1]))
		sourceEnd.append(int(frag2[i].split(',')[2]))
		sourceName.append(baitdict.get(frag2[i][6:]))
		sourceStrand.append('+')
		targetChrom.append(frag1[i].split(',')[0])
		targetStart.append(int(frag1[i].split(',')[1]))
		targetEnd.append(int(frag1[i].split(',')[2]))
		targetName.append('.')
		targetStrand.append('-')

biglist = [chrom,chromStart,chromEnd,name,score,value,exp,color,sourceChrom,sourceStart,sourceEnd,sourceName,sourceStrand,targetChrom,targetStart,targetEnd,targetName,targetStrand]


f = open("bedbed.bed", "w")
f.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full\n')
for i in range(len(biglist[0])): #range(len(chrom)):
	#f.write('')
	f.write("\t".join([str(y[i]) for y in biglist]) + "\n")
f.close()
# baitfile ./raw/Design/h19_chr20and21.baitmap
# washU ./output/data/output_washU_text.txt
# output ./output
# [chrom[x],chromStart[x],chromEnd[x],name[x],score[x],value[x],exp[x],color[x],sourceChrom[x],sourceStart[x],sourceEnd[x],sourceName[x],sourceStrand[x],targetChrom[x],targetStart[x],targetEnd[x],targetName[x],targetStrand[x]