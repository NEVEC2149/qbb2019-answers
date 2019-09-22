#!/usr/bin/env python3

"""
Usage: ./day5-lunch/Question2.py t_data.ctab
    
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

new_df = []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    chrom = str(fields[1])
    strand = fields[2]
    start = int(fields[3])
    end = int(fields[4])
    t_name = fields[5]
    if strand == "+":
        if start - 500 >= 0:
            prostart = start - 500
            proend = start + 500
        else:
            proend = start + 500
            prostart = 0
        new_df.append([chrom, prostart, proend, t_name])
            
    else:
        if end - 500 >= 0:
            prostart = end - 500
            proend = end + 500
        else:
            prostart = 0
            proend = end + 500
        new_df.append([chrom, prostart, proend, t_name])
    


for i in range(len(new_df)):
    g = new_df[i]

    for j in range(len(g)):
        if j < len(g) - 1:
            print(g[j],end = "\t")
        else:
            print(g[j])