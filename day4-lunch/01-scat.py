#!/usr/bin/env python3

"""
Usage: ./01-scat.py <ctab>

Compare FPKM vlaues
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv( sys.argv[1], sep="\t", index_col="t_name" )

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv( sys.argv[2], sep="\t", index_col="t_name" )
    
fpkm = { name1 : ctab1.loc[:,"FPKM"],
         name2 : ctab2.loc[:,"FPKM"] }
         
df = pd.DataFrame( fpkm )

    
fig, ax = plt.subplots()
ax.scatter( x=np.log2( df.loc[:,name1] + 0.001 ), y=np.log2( df.loc[:,name2] + 0.001 ), s=4, alpha=0.1 )
ax.plot( np.polyfit( x=np.log2( df.loc[:,name1] + 0.001), y=np.log2( df.loc[:,name2] + 0.001), deg=1 ), color="red" )
plt.title('FPKM Comparison')
plt.xlabel('FPKM1')
plt.ylabel('FPKM2')
fig.savefig( "FPKM-comparison.png" )
plt.close( fig )