#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-06
Purpose: I'm helping trace the lineage of ssRNA seq results
"""

import argparse
import matplotlib.pyplot as pl
import numpy as np
import os
import pandas as pd
import scanpy as sc
from matplotlib import rcParams
from matplotlib.pyplot import rc_context

"""Alter scanpy's settings"""
sc.settings.verbosity = 3
# will make scanpy the most helpful

sc.set_figure_params(dpi=80, dpi_save= 200, color_map = 'Pastel2_r', facecolor= 'white')
# basic figure formatting
# frameon=False, figsize=(3, 3) [further other settings]

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="I'm helping trace the lineage of ssRNA seq results",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-indir',
                        '--input_directory', 
                        help = 'input directory',
                        metavar = 'DIR', 
                        type= str, 
                        default='./inputs/filtered_gene_bc_matrices/hg19')    

    parser.add_argument('-o', 
                        '--outfile',
                        help='What would you like to name your output file?',
                        metavar='str',
                        type=str, 
                        default='pbmc3k')

    args = parser.parse_args()

    if not os.path.isdir(args.input_directory):
        parser.error(f"No such directory: '{args.input_directory}'")

    return args
              
# ----------------------------------------------
# def preprocessing():
#     """Let's do some preprocessing"""

#     results_file = './results/pbmc3k.h5ad'
#     # sets the file location for the results, I hope?

#     adata = spy.read_10x_mtx('inputs/filtered_gene_bc_matrices/hg19', var_names='gene_ids', cache = True)
#     # reads in Satan's matrix
    
#     spy.pl.highest_expr_genes(adata, n_top=20, )
#     # displays top 20 genes with highest % of counts/cell [averaged across cells]

#     spy.pp.filter_cells(adata, min_genes=200)
#     # filters out cells that have <200 genes detected - non-viable cells

#     spy.pp.filter_genes(adata, min_cells=10)
#     # filters out genes which are expressed by <10 cells





#     return ''




# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    results_file = f'./results/{args.outfile}.h5ad'
    print(f'"You can find your results in "{results_file}')
    input = args.input_directory
    
    adata = sc.read_10x_mtx(input, var_names='gene_ids', cache = True)
    # reads in Satan's matrix
    adata.X = adata.X.astype('float64')
    # sets it to be more accurate so it's a closer mirror to Seurat's R module work
        
    # spy.pl.highest_expr_genes(adata, n_top=20, show=True)
    # # displays top 20 genes with highest % of counts/cell [averaged across cells]

    
    # spy.pp.filter_cells(adata, min_genes=200)
    # # filters out cells that have <200 genes detected - non-viable cells

    # spy.pp.filter_genes(adata, min_cells=10)
    # # filters out genes which are expressed by <10 cells

        
  


# -----------------------------------------------
"""Clustering @ diff resolutions"""
#adata = spy.read_10x_mtx()
# adata = spy.read('./inputs/WagnerScience2018.h5ad')


# --------------------------------------------------
if __name__ == '__main__':
    main()
