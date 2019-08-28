#!/usr/bin/env python3

"""
Parse a single record from a FASTA file and print
"""

import sys

f = sys.stdin

# read header
line = f.readline()
assert line.startswith(">"), "not a FASTA file"
ident = line [1:].rstrip("\n")

sequences = []

while True:
    line = f.readline()
    if line.startswith(">"):
        break
    else:
        sequences.append( line.strip() )
        
sequence = "".join( sequences )

print( ident, sequence )