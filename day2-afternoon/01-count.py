#!/usr/bin/env python

"""
Print all unique gene names from a t_data.ctab file
"""

import sys



# gene_names_seen = []
# gene_names_seen = {}
gene_name_counts = {}

for i, line in enumerate( sys.stdin ):
    ## ignore the first header line
    if i == 0:
        continue
    ## get the gene name
    columns = line.rstrip("\n").split("\t")
    gene_name = columns[9]
    ## add gene if ot seen before
    # if gene_name in gene_names_seen:
    if gene_name in gene_name_counts:
        gene_name_counts[gene_name] += 1
        #continue
    else:
        # gene_names_seen.append( gene_name )
        # gene_names_seen[gene_name] = True
        # gene_names_seen.add( gene_name )
        gene_name_counts[gene_name] = 1
        
        
for name in gene_name_counts:
    print(name, gene_name_counts[name])