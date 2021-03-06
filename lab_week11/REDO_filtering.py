#!/usr/bin/env python3

import scanpy.api as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.tl.pca(adata)
sc.pl.pca(adata)
sc.pp.filter_genes(adata, min_counts = 1)
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all')

filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)

adata = adata[:, filter_result.gene_subset]
sc.pp.normalize_per_cell(adata)
sc.pp.log1p(adata)
sc.pp.scale(adata)
sc.tl.pca(adata,n_comps=50)
sc.pl.pca(adata)