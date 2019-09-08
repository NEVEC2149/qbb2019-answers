#!/usr/bin/env python3


from fasta import FASTAReader
import sys


target = FASTAReader( open (sys.argv[1]) )
query = FASTAReader( open (sys.argv[2]) )
k = int( sys.argv[3] )
kmers = {}
target_sequences = {}


for ident1, sequence1 in target:
    sequence1 = sequence1.upper()
    target_sequences[ident1] = sequence1
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
            variable = kmers[kmer2]
        else:
            continue
        match = []
        for ident1, i in variable:
            sequence1 = target_sequences[ident1]
            x = 0
            # print(i + k + x)
            # print(a + k + x)
            # print(len(sequence1))
            # print(len(sequence2))
            if a + k + x < len(sequence2) and i + k + x < len(sequence1):
                if sequence1[i + k + x] == sequence2[a + k + x]:
                    x += 1
                else:
                    match.append(sequence2[a + k + x] + "\n" )
                if sequence1[i + x] == sequence2[a + x]:
                    continue
            else:
                break           
        match.sort( key=len, reverse=True )
print( match )

#./kmer-matcher-extended.py subset.fa droYak2_seq.fa 11