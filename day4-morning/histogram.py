#!/usr/bin/env python3

"""
Usage: ./histogram.py

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

mu = 0
sigma = 1

x = np.linspace( -15, 15, 100 )
# print( x )
# print( type (x) )
y = stats.norm.pdf( x, mu, sigma )
# print( y )
# print( type (y) )

fig, ax = plt.subplots()
ax.hist( my_data, bins=100, density=True )
ax.plot( x, y )
fig.savefig( "fpkms.png" )
plt.close( fig )