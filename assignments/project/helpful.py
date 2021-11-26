#!/usr/bin/env python3
"""
Author : abanka <abanka@localhost>
Date   : 2021-11-25
Purpose: I'm going to help figure out the basics
"""
#%% [markdown]
# <h1>ssRNA sequence analysis<h1>
# <h4>Purpose: Analysis of ssRNA sequence data from single-cell expirements<h4>
# <h2>Author: Amy Banka<h2>
# <h4>Date: November 29, 2021 <br>Course: BE Something something<h4>

#%%
import argparse
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import scanpy as sc
from matplotlib import rcParams
from matplotlib.pyplot import rc_context, show

"""Alter scanpy's settings"""
sc.settings.verbosity = 3
# will make scanpy the most helpful

sc.set_figure_params(dpi=80, dpi_save= 200, color_map = 'Pastel2_r', facecolor= 'white')
# low dots/inch yields small inline figures? - from one source
# (dpi=80, 100, 200, frameon=False, figsize=(3, 3)) [further other settings] - from another source?

results_file = './results/pbmc3k.h5ad'
    # sets the file location for the results, I hope?

adata = sc.read_10x_mtx('inputs/filtered_gene_bc_matrices/hg19', var_names='gene_ids', cache = True)
    # reads in Satan's matrix
    ##### print(adata)
adata.X = adata.X.astype('float64')

# %% [markdown]
# # Let's do some initial mapping
# ### Please note: Data was already somewhat filtered
# #### I've chosen to leave in "unnecessary" steps because I will <br>use them with my actual data

# %% [markdown]
# # Here's the uncached data with basic maps!!
# %%
"""Let's do some initial mapping"""
sc.pl.highest_expr_genes(adata, n_top=20)
# displays top 20 genes with highest % of counts/cell [averaged across cells]

adata.var['mt'] = adata.var_names.str.startswith('MT-')
# for w/e reason, this data came pre-filled for mitochondrial genes
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
### where is ^ going? ###
# sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
#              jitter=0.4, multi_panel=True)
# sc.pl.scatter(adata, x='total_counts', y='pct_counts_mt')
sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts'],
             jitter=0.4, multi_panel=True)
sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts')


# %%
sc.pp.filter_cells(adata, min_genes=200)
    # filters out cells that have <200 genes detected - non-viable cells

sc.pp.filter_genes(adata, min_cells=10)
    # filters out genes which are expressed by <10 cells

adata = adata[adata.obs.n_genes_by_counts < 2500, :]
adata = adata[adata.obs.pct_counts_mt < 5, :]

#-------------------------------------

# %%
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
# high mitochondrial count suggests a damaged/leaking cell
sc.pl.highest_expr_genes(adata, n_top=20, show=True)
# displays top 20 genes with highest % of counts/cell [averaged across cells]
### deleted mt garbage for rn
sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts'],
             jitter=0.4, multi_panel=True)
sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts')
sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts')

# ----------------------------------
# %%
"""normalize & log?"""
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# %%
"""Repeat graphs to view differences"""
sc.pl.highest_expr_genes(adata, n_top=20, show=True)
# displays top 20 genes with highest % of counts/cell [averaged across cells]
sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts'],
             jitter=0.4, multi_panel=True)
sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts')


# %%
"""Id highly variable genes"""
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
sc.pl.highly_variable_genes(adata)
sc.pl.highest_expr_genes(adata, n_top=20)
# %%

# %%
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    # args = get_args()
    plots1()

# --------------------------------------------------
if __name__ == '__main__':
    main()

# %%
def plots1():
    sc.pl.scatter(adata, x='Total Counts', y='n_genes_by_counts')


# %%
