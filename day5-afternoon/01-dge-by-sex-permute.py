#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

#FBtr0302347

df = pd.read_csv( sys.argv[1], index_col = "t_name" )
col_names = df.columns.values.tolist()

def sex_dge(transcript_id):
    goi = pd.DataFrame( df.loc[transcript_id].iloc[1:] )
    goi.columns = ["FPKM"]

    goi["FPKM"] = pd.to_numeric(goi["FPKM"])

    goi["sex"], goi["stage"] = goi.index.str.split("_", 1).str
    goi["sex_permuted"] = np.random.permutation(goi["sex"])
    
    goi["logFPKM"] = np.log( goi["FPKM"] + 1 )

    model = sm.formula.ols(formula = "FPKM ~ sex_permuted", data = goi)
    ols_results = model.fit()

    return(transcript_id, ols_results.pvalues[1])
    
sex_dge("FBtr0302347")

hi_exp_genes = ( (df == 0).sum(axis = 1) == 0 )
    ## less than or equal to three zeros
hi_df = df.loc[hi_exp_genes, :]
hi_exp_genes_list = hi_df.index.values.tolist()

# print(hi_df.shape)

results = []
for transcript in hi_exp_genes_list:
    results.append( sex_dge(transcript) )
    
results_df = pd.DataFrame( results, columns = ["t_name", "p_val"]).sort_values(by= "p_val")
print(results_df)

fig, ax = plt.subplots()
hist = ax.hist(results_df.loc[:, "p_val"])
fig.savefig("pvalhist.png")
plt.close(fig)