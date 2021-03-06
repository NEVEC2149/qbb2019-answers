#!/usr/bin/env python3

"""
Parse and print all reords from a FASTA flle
"""

import sys

class FASTAReader(object):
    
    def __init__( self, fh ):
        self.fh = fh
        self.last_ident = None
        self.eof = False
    
    def __iter__( self ):
        return self
        
    def __next__( self ):
        
        if self.eof:
            # return None, None
            raise StopIteration
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
        # if we reach here, ident is set correctly
        
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append( line.strip() )
            
        sequence = "".join( sequences )
        return ident, sequence
            
            
        

# what I want to work:

# reader = FASTAReader( sys.stdin)

# while True:
#     ident, sequence = reader.next()
#     if ident is None:
#         break
#     print( ident, sequence )

# for ident, sequence in reader:
#    print ( ident, sequence )