#!/usr/bin/env python3

"""
Usage: ./002-pandas.py <ctab>

Compare num.exons vs length ... using numpy/Pandas!
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd

# exons = []
# lengths = []

ctab = pd.read_csv( sys.argv[1], sep="\t" )
print( ctab )
print( type(ctab) )

exons = ctab.loc[:,"num_exons"]
lengths = ctab.loc[:,"length"]

print( ctab.describe() )

fig, ax = plt.subplots()
ax.scatter( x=exons, y=lengths )
ax.plot( [0,40], [0,20000], color="red" )
fig.savefig( "exon-v-length.png" )
plt.close( fig )