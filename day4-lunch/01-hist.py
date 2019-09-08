#!/usr/bin/env python3

"""
Usage: ./01-hist.py

Plot FPKM
"""

import sys
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

fpkms = []
for i, line in enumerate( open(sys.argv[1]) ):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append( float(fields[11]) )

my_data = np.log2( fpkms )

mu = int( sys.argv[2] )
sigma = int( sys.argv[3] )
a = int( sys.argv[4] )

x = np.linspace( -15, 15, 100 )
y = stats.norm.pdf( x, mu, sigma )
var = stats.skewnorm.pdf( x, a, loc=mu, scale=sigma )

fig, ax = plt.subplots()
ax.hist( my_data, bins=100, density=True )
ax.plot( x, y )
ax.plot( x, var, color="purple" )
plt.title("FPKM value")
plt.xlabel('log2_FPKM')
plt.ylabel('Frequency')
fig.savefig( "fpkms.png" )
plt.close( fig )