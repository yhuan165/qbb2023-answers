#!/usr/bin/env python

#Exercise 1
f = open("./data/inflammation-01.csv", "r")
lines = f.readlines()

filelist = []

for line in lines:
	line = line.rstrip()
	line_list = line.split(',')
	filelist.append(line_list)

#print(len(filelist))

#number of flare-ups that the fifth patient had on the first, tenth, and last day.
print("first day",filelist[4][0])
print("tenth day",filelist[4][9])
print("last day",filelist[4][-1])


#Exercise 2
patientavg = []
for x in filelist:
	sum1 = 0 
	for y in x:
		sum1 += float(y)
	patientavg.append(sum1/len(x))

#print(patientavg)
#print the first 10 averages
for i in range(10):
	print(patientavg[i])

#Exercise 3
print("the max average is:",max(patientavg))
print("the min average is:",min(patientavg))

#Exercise 4
difflist = []
for i in range(len(filelist[0])):
	diff = int(filelist[4][i]) - int(filelist[0][i])
	absdiff = abs(diff)
	difflist.append(absdiff)
print(difflist)

#Optional
dailyavg = []
for x in range(len(filelist[0])):
	summ = 0
	for y in range(len(filelist)):
		summ += float(filelist[y][x])
	dailyavg.append(summ/len(filelist))
print(dailyavg)

f.close()