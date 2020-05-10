#!/usr/bin/env python3

import sys

graph1 = open(sys.argv[1])
graph2 = open(sys.argv[2])

inp = []
overlap = []
uniq1 = []
uniq2 = []
for i, line in enumerate(graph1):
    if i == 0:
        continue
    inp.append(line)

counter = 0
for i, line in enumerate(graph2):
    if i == 0:
        continue
    if line not in inp:
        uniq2.append(line)
    else:
        overlap.append(line)
    counter += 1

print("Methylation sites only in ES_f_mC:\n")
for item in uniq2:
    print(item)
print("N/A")
print("Methylation sites only in EpiSC_mC:\n")
for item in uniq1:
    print(item)