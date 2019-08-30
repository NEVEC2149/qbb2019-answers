#!/usr/bin/env python3

import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]

fpkms = {}
sexstg = []

for i, line in enumerate( open(metadata) ):
    if i == 0:
        continue
    fields = line.rstrip("\n").split(",")
    srr_id = fields[0]
    sex_id = fields[1]
    stg_id = fields[2]
    sexstg = sex_id + "_" + stg_id 
    ctab_path = os.path.join( ctab_dir, srr_id, "t_data.ctab" )
    df = pd.read_csv( ctab_path, sep="\t", index_col="t_name" )
    if i == 1:
        fpkms["gene_name"] = df.loc[:,"gene_name"]
        ## the ":" in loc[] takes the entire row
    fpkms[sexstg] = df.loc[:,"FPKM"]
    
df_fpkms = pd.DataFrame( fpkms )
# df_fpkms.columns = sexstg
pd.DataFrame.to_csv( df_fpkms, "all.csv" )