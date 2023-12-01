#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

# print(full_design_df)

#exercise 1.1
# row = full_design_df.loc['GTEX-113JC'] 
# nonzerorow = row[row != 0]
# dropped = nonzerorow.iloc[:-3]

# fig, ax = plt.subplots()

# ax.hist(dropped, bins = 20)
# ax.set_xlabel("Gene Expression of GTEX-113JC (log2(normalized counts))")
# ax.set_ylabel("Number of Genes")
# fig.tight_layout()
# plt.show()

# fig.savefig("GTEX-113JC.png")

#exercise 1.2
# male = full_design_df.loc[full_design_df['SEX'] == 1, 'MXD4']
# female = full_design_df.loc[full_design_df['SEX'] == 2, 'MXD4']
# print(male)
# print(female)

# fig, bx = plt.subplots()

# bx.hist(male, bins = 20, alpha = 0.5, label = 'male')
# bx.hist(female, bins = 20, alpha = 0.5, label = 'female')
# bx.set_xlabel("Gene Expression for MXD4 (log2(normalized counts))")
# bx.set_ylabel("Number of Samples")
# bx.legend()
# fig.tight_layout()
# plt.show()

# fig.savefig("MXD4.png")

#exercise 1.3
age = full_design_df['AGE'].value_counts()
indexes = age.index

fig, cx = plt.subplots()

cx.bar(indexes, age)
cx.set_xlabel("Age")
cx.set_ylabel("Number of Samples")
cx.legend()
fig.tight_layout()
plt.show()

fig.savefig("Age.png")

