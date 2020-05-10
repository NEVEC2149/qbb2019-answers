#!/usr/bin/env python2

import hifive as hf
import numpy
import sys 

hic = hf.HiC('class13_project', 'r')
index = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000)
loc = numpy.where(data[:, :, 1] > 0)
index[loc[0], loc[1], 0] /= index[loc[0], loc[1], 1]
index = numpy.log(index[:, :, 0] + 0.1)
index -= numpy.amin(index)

activity = {}
rna = {}

for line in open(sys.argv[1]):
	if line.startswith('track'):
		continue
	fields = line.rstrip('\n').split()
	if int(fields[1]) > 5000000 and int(fields[2]) < 50000000:
		index = (int(fields[2]) - 5000000) / 5000
		if index <= 7000:
			activity[index] = float(fields[4])
          
for line in open(sys.argv[2]):
	if line.startswith('track'):
		continue
	fields = line.rstrip('\n').split()
	if int(fields[1]) > 5000000 and int(fields[2]) < 50000000:
		index = (int(fields[2]) - 5000000) / 5000
		if index <= 7000:
			rna[index] = float(fields[4])
 
overall = {x:activity[x] for x in activity if x in rna}

for i in overall:
	index[:,i] *= activity[i]

index_subset = index[rna.keys(), :][:, activity.keys()]
predictions = numpy.sum(index_subset, axis=1)
for count,i in enumerate(overall):
	print(str(i) + '\t' + str(predictions[count]))

expression = rna.values()
R = numpy.corrcoef(expression, predictions)[0, 1]
print('R coefficient is: ' + str(R))