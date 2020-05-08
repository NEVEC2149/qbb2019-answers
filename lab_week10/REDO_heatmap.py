#!/usr/bin/env python3

import sys
import scipy 
import numpy as np
import scipy.cluster.hierarchy as hac
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans

f = open(sys.argv[1])
df = pd.read_table(f, header=0, index_col=0)

cell_types = df.columns.values
gene_names = df.index.values
info_array = df.values

Z = linkage(info_array, method = 'average')
genes_sorted = leaves_list(Z)
gene_names_sorted = gene_names[genes_sorted]

Z_transposed = linkage(info_array.T,  method = 'average')
cells_sorted = leaves_list(Z_transposed)
cell_types_sorted = cell_types[cells_sorted]

heat_data = info_array[genes_sorted, :]
heat_data = heat_data[:, cells_sorted]


values = (heat_data-np.average(heat_data, axis=0)) / np.std(heat_data, axis=0)
max_value = np.max(np.abs(values))
sns.heatmap(values)
plt.savefig("heatmap.png")