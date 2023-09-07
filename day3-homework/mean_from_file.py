#!/usr/bin/env python

import sys

f = open(sys.argv[1], "r")
lines = f.readlines()

filelist = []

for line in lines:
	line = line.rstrip()
	filelist.append(int(line))

def average(listofint):
	summ = 0
	for i in listofint:
		summ += i
	return (summ/len(listofint))

print(average(filelist))