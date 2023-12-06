#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import csv
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt

# read in data
# counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
# metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)
'''
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_norme	d = np.log2(counts_df_normed + 1)

full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
results = model.fit()

slope = results.params[1]
pval = results.pvalues[1]

# print(full_design_df)

output_file = "./DE_results.csv"
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Gene', 'Coefficient(Slope)', 'P-Value'])
    de_results = {}
    for gene in counts_df_normed.columns:
        formula = f'Q("{gene}") ~ SEX'  # Replace SEX with your relevant grouping variable
        model = smf.ols(formula=formula, data=full_design_df)
        results = model.fit()
        writer.writerow([gene, results.params['SEX'], results.pvalues['SEX']])
'''

# final_table = pd.read_csv("DE_results.csv", index_col = 0)
# final_table['P-Value']= final_table['P-Value'].fillna(1.0)
# final_table['Q-Value'] = multitest.fdrcorrection(final_table['P-Value'], method = 'indep', alpha=0.1)[1]

# #loop through and write to file

# f = open("genelist.txt", "w")
# for i in final_table.loc[final_table['Q-Value']<0.1,:].index:
# 	f.write(i+ "\n")
# f.close()

'''
dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df
'''
# f = open("des2genelist.txt", "w")
# for i in results.loc[results['padj']<0.1,:].index:
# 	f.write(i+ "\n")
# f.close()

genelist = []
for line in open("genelist.txt"):
	gene = line.rstrip('\n')
	genelist.append(gene)

des2genelist = []
for line1 in open("des2genelist.txt"):
	gene1 = line1.rstrip('\n')
	des2genelist.append(gene1)

geneset = set(genelist)
des2genelist = set(des2genelist)
intersect = geneset.intersection(des2genelist)
together = geneset.union(des2genelist)

index = (len(intersect)/len(together)) * 100
print(index)


'''
results1 = results.dropna(subset=['padj'])

fig, ax = plt.subplots()

log2fold = results1['log2FoldChange']
pvalue = results1['pvalue']
padj = results1['padj']

log10pvalue = -1*(np.log10(pvalue))

DEGs = (padj < 0.1) & (abs(log2fold) > 1)

ax.scatter(log2fold, log10pvalue, color='grey', alpha=0.5, label='Not DE')
ax.scatter(log2fold[DEGs], log10pvalue[DEGs], color='red', alpha=0.7, label='DEGs')
ax.set_xlabel("Log2FoldChange")
ax.set_ylabel("-log10 of P-Value")
ax.set_title("Didfferential expression Volcano Plot")
fig.tight_layout()
plt.show()

fig.savefig("volc.png")
'''

