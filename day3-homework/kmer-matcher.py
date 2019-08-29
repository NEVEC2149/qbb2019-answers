#!/usr/bin/env python3


from fasta import FASTAReader
import sys


target = FASTAReader( open (sys.argv[1]) )
query = FASTAReader( open (sys.argv[2]) )
k = int( sys.argv[3] )
kmers = {}


for ident1, sequence1 in target:
    sequence1 = sequence1.upper()
    for i in range( 0, len(sequence1) -k + 1 ):
        kmer1 = sequence1[i:i+k]
        if kmer1 in kmers:
            kmers[kmer1].append((ident1, i))
        else:
            kmers[kmer1] = [(ident1, i)]

for ident2, sequence2 in query:
    sequence2 = sequence2.upper()
    for a in range( 0, len(sequence2) -k + 1 ):
        kmer2 = sequence2[a:a+k]
        if kmer2 in kmers:
            print( kmers[kmer2], str(a), kmer2 )

