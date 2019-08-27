#!/usr/bin/env python3

import sys
import statistics

f =open( sys.argv[1] )

# Question 1    
# counter=0
# for line in f:
#     line = line.rstrip("\n")
#     fields = line.split("\t")
#     if fields[2] != "*":
#         counter += 1
# print (counter)


# Question 2
# counter=0
# for line in f:
#     line = line.rstrip("\n")
#     fields = line.split("\t")
#     if "NM:i:0" in fields:
#         counter += 1
# print (counter)


# Question 3
# counter=0
# for line in f:
#     line = line.rstrip("\n")
#     fields = line.split("\t")
#     if "NH:i:1" in fields:
#         counter += 1
# print (counter)


# Question 4
# for line in f:
#      line = line.rstrip("\n")
#      f.readlines(1-10)
#      fields = line.split("\t")
#      print (fields[2])


# Question 5
# mapqs = []
# for line in f:
#     line = line.rstrip("\n")
#     fields = line.split("\t")
#     mapqs.append( int( fields[4] ) )
# print ( statistics.mean( mapqs ) )


# Question 6
counter = 0
for line in f:
    line = line.rstrip("\n")
    fields = line.split("\t")
    if "2L" == fields[2] and 10000 <= int( fields[3] ) <= 20000:
        counter += 1
print (counter)
        