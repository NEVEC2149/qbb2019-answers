#!/usr/bin/env python3

import sys

gene_list = []
position = {}

for i, line in enumerate( open(sys.argv[1]) ):
    column = line.rstrip("\n").split()
    if column[0] == "3R" and column[2] == "gene" and "protein_coding" in line:
        gene_list.append( int( column[3] ) )
        gene_list.append( int( column[4] ) )
        gene_name = column[13]
        position[column[3]] = gene_name
        position[column[4]] = gene_name

# keys: positions
# values: gene_name

mut = 21378950
sorted( gene_list )
iteration = 0
mid = 0
lo = 0
hi = len(gene_list) - 1
while hi > 1:
    hi = len(gene_list) - 1
    iteration += 1
    mid = int( hi/2 )
    if gene_list[mid] == mut:
        gene_pos = gene_list[mid]
        gene_name = position[str(gene_pos)]
        print ( gene_name, abs(gene_list[mid] - mut), iteration )
    elif gene_list[mid] > mut:
        gene_list = gene_list[:mid]
    elif gene_list[mid] < mut:
        gene_list = gene_list[mid:]
    else:
        break
gene_pos = gene_list[mid]
gene_name = position[str(gene_pos)]
print ( gene_name, abs(gene_list[mid] - mut), iteration )


# less -S /Users/cmdb/data/genomes/BDGP6.Ensembl.81.gtf
# ./binary-search.py /Users/cmdb/data/genomes/BDGP6.Ensembl.81.gtf
