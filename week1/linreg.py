#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

import scipy.stats as sps
import statsmodels.formula.api as smf
import statsmodels.api as sm

#step 1.1
df = pd.read_csv('/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_dnm.csv')
#print(df)

#step 1.2
count = df.groupby(['Proband_id','Phase_combined']).size().reset_index(name = 'Count')

#print(count)

dicto = {}
for i in range(0,len(count),2):
	dicto[count.loc[i, "Proband_id"]] = [count.loc[i+1, "Count"],count.loc[i, "Count"]]

#print(dicto)

#step 1.3

deNovoCountDF = pd.DataFrame.from_dict(dicto, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])
#print(deNovoCountDF)

#step 1.4
dfage = pd.read_csv('/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_parental_age.csv', index_col = 'Proband_id')
#print(dfage)

#step 1.5
concat = pd.concat([deNovoCountDF,dfage],axis = 1, join = 'inner')
#print(concat)

#step 2.1
'''
fig, ax = plt.subplots()
ax.scatter(concat["Father_age"],concat["paternal_dnm"])
ax.set_xlabel("Father Age")
ax.set_ylabel("Paternal De Novo Mutations")
ax.set_title("Paternal DNMs in relation to Father Age")
fig.savefig("ex2_b.png")
plt.show()

fig, bx = plt.subplots()
bx.scatter(concat["Mother_age"],concat["maternal_dnm"], c = "red")
bx.set_xlabel("Mother Age")
bx.set_ylabel("Maternal De Novo Mutations")
bx.set_title("Maternal DNMs in relation to Mother Age")
fig.savefig("ex2_a.png")
plt.show()
'''

#step 2.2
model = smf.ols(formula = "maternal_dnm ~ 1 + Mother_age", data = concat)
results = model.fit()
#print(results.summary())
#print(results.pvalues)

#step 2.3
modelf = smf.ols(formula = "paternal_dnm ~ 1 + Father_age", data = concat)
resultsf = modelf.fit()
#print(resultsf.summary())
#print(resultsf.pvalues)

#step 2.4
#in readme

#step 2.5
fig, cx = plt.subplots()
cx.hist(count.loc[count["Phase_combined"] == "mother", "Count"], bins = 30, label = "mother", alpha = 0.5)
cx.hist(count.loc[count["Phase_combined"] == "father", "Count"], bins = 30, label = "father", alpha = 0.5)
cx.set_xlabel("Number of De Novo Mutations")
cx.set_ylabel("Frequency (Number of Proband IDs)")
cx.set_title("Distribution of DNMs by Proband ID")
cx.legend()
fig.savefig("ex2_c.png")
plt.show()

#step 2.6
print(sps.ttest_ind(
count.loc[count['Phase_combined'] == 'father','Count'],
count.loc[count['Phase_combined'] == 'mother','Count']))



