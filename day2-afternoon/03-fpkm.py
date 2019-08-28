#!/usr/bin/env python

"""
Compute the average FPKM
"""

import sys


# count = 0
# total = 0
#
# for i, line in enumerate( open( sys.argv[1] ) ):
#     if i == 0:
#         continue
#     fields = line.rstrip("\n").split("\t")
#     fpkm = float( fields[11] )
#     count += 1
#     total += fpkm
#
# print( total/count )


import numpy

# def read_fpkms_from_t_data( fname ):
#     all_fpkms = []
#     for i, line in enumerate( open( fname ) ):
#         if i == 0:
#             continue
#         fields = line.rstrip("\n").split("\t")
#         fpkm = float( fields[11] )
#         all_fpkms.append( fpkm )
#     return all_fpkms
#
# all_fpkms_1 = read_fpkms_from_t_data( sys.argv[1])
# all_fpkms_2 = read_fpkms_from_t_data( sys.argv[2])
#
# corr = numpy.corrcoef( all_fpkms_1, all_fpkms_2 )
# print( "Pearson's R:", corr[0,1] )


import scipy.stats

def read_fpkms_from_t_data( fname ):
    all_fpkms = []
    for i, line in enumerate( open( fname ) ):
        if i == 0:
            continue
        fields = line.rstrip("\n").split("\t")
        fpkm = float( fields[11] )
        all_fpkms.append( fpkm )
    return all_fpkms

all_fpkms_1 = read_fpkms_from_t_data( sys.argv[1])
all_fpkms_2 = read_fpkms_from_t_data( sys.argv[2])

rho, pval = scipy.corrcoef( all_fpkms_1, all_fpkms_2 )
print( "Speara=man's rho", rho )

print( scipy.stats.ttest_ind(all_fpkms_1, all_fpkms_2) )

print( scipy.stats.ks_2samp( all_fpkms_1, all_fpkms_2) )


