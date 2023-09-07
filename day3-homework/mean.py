#!/usr/bin/env python

def average(listofint):
	summ = 0
	for i in listofint:
		summ += i
	return (summ/len(listofint))

nums = [3,4,5,16,24,64,76]
print(average(nums))