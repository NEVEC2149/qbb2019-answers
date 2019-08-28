#!/usr/bin/env python3

import sys


### Question 1

f =open( sys.argv[1] )

for i, line in enumerate( f ):
    column = line.split()
    if len( column ) < 3:
        continue
    if "FBgn" not in column[-1]:
        continue
    if column[-3].endswith ( "DROME" ):
        print (column[-1], column[-2])




### Question 2
# Input 2 files after the python script, first the Index and second the .ctab

IndexComp = {}

for i, line in enumerate( open( sys.argv[1] ) ):
    columns = line.rstrip("\n").split()
    gene_name = columns[0]
    uniprot = columns[1]
    IndexComp[gene_name] = uniprot

for i, line in enumerate( open( sys.argv[2] ) ):
    columns = line.rstrip("\n").split()
    gene_ID = columns[8]
    if gene_ID in IndexComp:
        print(line, IndexComp[gene_ID])
    elif gene_ID not in IndexComp:
        print ("default")

