#!/usr/bin/env python3

import sys
import pandas as pd

transcript = open(sys.argv[1])

promoter = {}
t_name = []
pro_start = []
pro_end = []

for i, line in enumerate( transcript ):
    if i == 0:
        continue
    column = line.split()
    t_name = column[5]
    if column[2] == "+":
        if (int(column[3]) - 500) < 0:
            pro_start = str(0)
        else:
            pro_start = str( int(column[3]) - 500 )
            pro_end = str( int(column[3]) + 500 )
    elif column[2] == "-":
        if (int(column[4]) - 500) < 0:
            pro_start = str(0)
        else:
            pro_start = str( int(column[4]) - 500 )
            pro_end = str( int(column[4]) + 500 )
            ####the strings are in the loop every round so no need to += the new value to the string since it is going to be printed everytime
    # print(type(column[1]))
    # print(type(pro_start))
    # print(type(pro_end))
    promoter[ column[5] ] = column[1] + "\t"+ pro_start + "\t"+ pro_end
    print( promoter[t_name], t_name, sep="\t" )

