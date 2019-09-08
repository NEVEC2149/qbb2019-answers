#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

## not working at the current stage

#FBtr0302347

df = pd.read_csv( sys.argv[1], index_col = "t_name" )
col_names = df.columns.values.tolist()

def sex_dge(transcript_id):
    goi = pd.DataFrame( df.loc[transcript_id].iloc[1:] )
    goi.columns = ["FPKM"]

    goi["FPKM"] = pd.to_numeric(goi["FPKM"])

    goi["sex"], goi["stage"] = goi.index.str.split("_", 1).str
    #print(goi)
    
    goi["stage"].replace("14A", "14", inplace = True)
    goi["stage"].replace("14B", "15", inplace = True)
    goi["stage"].replace("14C", "16", inplace = True)
    goi["stage"].replace("14D", "17", inplace = True)
    
    goi["stage"] = pd.to_numeric(goi["stage"])
    goi["stage"] = np.log( goi["FPKM"] )
    
    model = sm.formula.ols(formula = "FPKM ~ sex + stage", data = goi)
    ols_results = model.fit()
    
    # print( ols_results.summary() )

    return(transcript_id, ols_results.pvalues[1])
    
# print( sex_dge("FBtr0302347") )

hi_exp_genes = ( (df == 0).sum(axis = 1) == 0 )
    ## no zero allowed
hi_df = df.loc[hi_exp_genes, :]
hi_exp_genes_list = hi_df.index.values.tolist()

# print(hi_df.shape)

results = []
for transcript in hi_exp_genes_list:
    results.append( sex_dge(transcript) )

results_df = pd.DataFrame( results, columns = ["t_name", "p_val", "p_val_stage"]).sort_values(by= "p_val_stage")

print(results_df)

fig, ax = plt.subplots()
hist = ax.hist(results_df.loc[:, "p_val"])
fig.savefig("pvalhist.png")
plt.close(fig)