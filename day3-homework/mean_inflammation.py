#!/usr/bin/env python

import sys

f = open("/Users/cmdb/Desktop/swp-python/data/inflammation-01.csv", "r")
lines = f.readlines()

filelist = []

for line in lines:
	line = line.rstrip()
	splitline = line.split(',')
	filelist.append(splitline)

def average(patient):
	summ = 0
	for i in filelist[int(patient)]:
		summ += float(i)
	return (summ/len(filelist[int(patient)]))

#print(average(0))
print(average(int(sys.argv[1])))