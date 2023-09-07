#!/usr/bin/env python

import sys

f = open("/Users/cmdb/Desktop/swp-python/data/inflammation-01.csv", "r")
lines = f.readlines()

filelist = []

for line in lines:
	line = line.rstrip()
	splitline = line.split(',')
	filelist.append(splitline)

def average(patient1, patient2):
	difflist = []
	for i in range(len(filelist[int(patient1)])):
		diff = int(filelist[int(patient1)][i]) - int(filelist[int(patient2)][i])
		difflist.append(diff)
	return difflist

#print(average(0))
print(average(sys.argv[1],sys.argv[2]))