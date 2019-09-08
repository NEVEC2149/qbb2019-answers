#!/usr/bin/env python3

import sys

if len( sys.argv ) > 1:
    f =open( sys.argv[1] )
else:
    f = sys.stdin
# this requires a "<" before the filename.

for i, line in enumerate( f ):
    # remove newline character
    line = line.rstrip("\n")
    # skip comment lines
    if line.startswith( "#" ):
        continue
    # split into fields
    fields = line.split("\t")
    # consider onlu genes
    if fields[2] == "gene":
        print( int( fields[4] ) - int( fields[3] ) )


print( f.readline() )

print( "\n\n\n\n" )

print( f.readline().rstrip("\n") )


#counter = 0
#while True:
#    if counter > 10:
#        break
#    line = f.readline(.rstrip"\n")
#    print(line)
#    counter += 1

#for i, line in enumerate( f ):
#    line = line.rstrip("\n")
#    print ( line )
#    if i >= 10:
#        break

#for line in f:
#   line = line.rstrip("\n")
#    print( line )