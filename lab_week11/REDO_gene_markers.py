#!/usr/bin/env python3

import scanpy.api as sc
import sys
import matplotlib.pyplot as plt

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

sc.pp.filter_genes(adata)  
sc.pp.normalize_per_cell(adata, key_n_counts='n_counts_all')
filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor='cell_ranger')
adata = adata[:, filter_result.gene_subset]   

sc.pp.neighbors(adata)
sc.tl.louvain(adata)

sc.tl.rank_genes_groups(adata, groupby ='louvain', method='t-test')
sc.pl.rank_genes_groups(adata, groupby='louvain', method = 't-test', show=False, save='Gene_Type.png')
sc.tl.rank_genes_groups(adata, groupby ='louvain', method='logreg')
sc.pl.rank_genes_groups(adata, groupby='louvain', method = 'logreg', show=False, save='Genes_Log.png')

sc.tl.tsne(adata)
sc.pl.tsne(adata, color = ["louvain", "Dbi", "Arpp21","Nrp2","Hbb-bs", "Arpc1b", "Reln", "Rgs5"], legend_loc="on data" )