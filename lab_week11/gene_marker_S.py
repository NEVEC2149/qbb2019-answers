#!/usr/bin/env python3

"""
Usage: ./color_by_marker_genes.py
"""

import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

n_top_genes = 1000


sc.pp.filter_genes(adata, min_counts=1)  
sc.pp.normalize_per_cell(               
     adata, key_n_counts='n_counts_all')
filter_result = sc.pp.filter_genes_dispersion(  
    adata.X, flavor='cell_ranger', n_top_genes=n_top_genes, log=False)
adata = adata[:, filter_result.gene_subset]    


sc.pp.normalize_per_cell(adata)        
sc.pp.log1p(adata)               
sc.pp.scale(adata)