#!/usr/bin/env python3

"""
Usage: ./01-boxplot.py <gene_name> <FPKMs.csv>

Boxplot all transripts for a given file
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv( fpkm_file, index_col="t_name" )
### index_col add row names
#print( df )

goi = df.loc[:,"gene_name"] == gene_name

fpkms = df.drop( columns="gene_name" )
print( fpkms.loc[goi,:] )

fig, ax = plt.subplots()
ax.boxplot( fpkms.loc[goi,:].T )
fig.savefig( "boxplot.png" )
plt.close( fig )