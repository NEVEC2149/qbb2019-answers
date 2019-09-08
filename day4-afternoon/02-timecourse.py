#!/usr/bin/env python3

"""
Usage: ./02-timecourse.py <t)name> <samples.csv> <FPKMs>

Create a timecourse of a given transcript for females
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

# specify transcript of interest
t_name = sys.argv[1]

# load metadata
samples = pd.read_csv( sys.argv[2] )
soi = samples.loc[:,"sex"] == "female"
srr_ids = samples.loc[soi,"sample"]

# print( srr_ids )

# load FPKMs
fpkms = pd.read_csv( sys.argv[3], index_col ="t_name" )

# extract data
my_data = []
for srr_id in srr_ids:
        # print( srr_id )
        my_data.append( fpkms.loc[t_name,srr_id] )

# print( my_data )
        
fig, ax = plt.subplots()
ax.plot( my_data )
fig.savefig( "timecourse.png" )
plt.close( fig ) 
