#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

transcripts = np.loadtxt( "/Users/cmdb/Desktop/swp-python/all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "/Users/cmdb/Desktop/swp-python/all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "/Users/cmdb/Desktop/swp-python/all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest
cols = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols.append(i)

# Find columns with samples of interest MALE
colsmale = []
for i in range(len(samples)):
    if "male" in samples[i] and "female" not in samples[i]:
        colsmale.append(i)

# Subset data of interest
expression = data[row, cols]
expressionmale = data[row,colsmale]

# Prepare data
x = [10,11,12,13,"14A","14B","14C","14D"]
y = expression
ymale = expressionmale
ymaledouble = ymale * 2

# Plot data
fig, ax = plt.subplots()
ax.set_title( "FBtr0073461" )
ax.plot(x, y, c = "red", label = "female" )
ax.plot(x, ymale, c = "blue", label = "male")
ax.plot(x, ymaledouble, c = "green", label = "male x2")
fig.savefig( "FBtr0073461.png" )
plt.show()
plt.close( fig )