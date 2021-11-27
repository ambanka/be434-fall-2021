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
from matplotlib.pyplot import get, rc_context

"""Alter scanpy's settings"""
sc.settings.verbosity = 3
# will make scanpy the most helpful

sc.set_figure_params(dpi=80, dpi_save= 200, color_map = 'Pastel2_r', facecolor= 'white')
# basic figure formatting

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
              
# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    in_data = args.input_directory

    adata = sc.read_10x_mtx(in_data, var_names='gene_symbols', cache = True)
        # reads in Satan's matrix

    adata.var_names_make_unique()
    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    adata.X = adata.X.astype('float64')
        # sets it to be more accurate so it's a closer mirror to Seurat's R module work
    
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
       
    initial_maps(adata)
    adata = filtering(adata)
    filtered_maps(adata, 0)
    question(adata)

  # results_file = f'./results/{args.outfile}.h5ad'
    # print(f'"You can find your results in "{results_file}')

# ------------------------------------------------------    
def top_genes(adata, file_names):
    top = int(input("Number of genes to display: "))
    if top:
        sc.pl.highest_expr_genes(adata, n_top=top, save = file_names)
            # displays top 20 genes with highest % of counts/cell [averaged across cells]
    else:
        print("I recommend 10-30")

# --------------------------------
def question(adata):
    count = 1
    while True:
        answer = str(input("Would you like to try more stringent filtering? Y or N: "))
        if answer == "Y":
            adata = filtering(adata)
            filtered_maps(adata, count)
            count += 1
        elif answer == "N":
            break
        else:
            print("Wtf, dude?")


# -------------------------------------------
def violins(adata, file_namesA, file_namesB, file_namesMT):
    sc.pl.violin(adata, 'n_genes_by_counts', jitter = 0.4, xlabel='Number of Genes/Cell', size = 2, ylabel='', save = file_namesB)
    sc.pl.violin(adata, 'total_counts', jitter=0.4, xlabel='Total Counts/Cell', size=2, ylabel='', save= file_namesA)
    sc.pl.violin(adata, 'pct_counts_mt', jitter=0.4, xlabel='Percentage Counts in Mitochondrial Genes', size=2, ylabel='', save= file_namesMT)
 
# -------------------------------------------
def scatter_counts_v_genes(adata, file_namesB, file_namesMT):
    sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts', save = file_namesB)
    sc.pl.scatter(adata, x='total_counts', y='pct_counts_mt', save = file_namesMT)

# ---------------------------------------

def initial_maps(adata):
    file_names = '_initial'
    file_namesA = '_initial_T_counts_per_cell'
    file_namesB = '_initial_genes_per_cell'
    file_namesMT = '_initial_MT'
    top_genes(adata, file_names)
    violins(adata, file_namesA, file_namesB, file_namesMT)
    scatter_counts_v_genes(adata, file_namesB, file_namesMT)

# -------------------------------------
def filtering(adata):
    
    print("Please start small then go higher!")

    low_genes = int(input("Filter out cells that have fewer than ____ genes: "))
    high_genes = int(input("Filter out cells that have more than ____ gene counts: "))
    rare_genes = int(input("Filter out genes that are seen in fewer than ____ cells: "))
    mito_perc = int(input("Filter out cells with too high a mitochondrial gene percentage: "))
 
    sc.pp.filter_cells(adata, min_genes= low_genes)
    sc.pp.filter_genes(adata, min_cells=rare_genes)
    adata = adata[adata.obs.n_genes_by_counts < high_genes, :]
    adata = adata[adata.obs.pct_counts_mt < mito_perc, :]
 
    return(adata)

# ----------------------------------------------


# -------------------------------------------
def filtered_maps(adata, count):
    file_names = f'_filtered_{count}'
    file_namesB = f'_filtered_genes_per_cell_{count}'
    top_genes(adata, file_names)
    violins(adata, file_names, file_namesB)
    scatter_counts_v_genes(adata, file_names)


# -------------------------------------
# def ():
#     sc.pl.scatter(adata, x='total_counts', y='pct_counts_mt')
#     sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts')

# # -------------------------------------
# def ():


# # -------------------------------------
# def ():

# # -------------------------------------
# def ():

# # -------------------------------------
# def ():


# # -------------------------------------
# def ():

# --------------------------------------------------
if __name__ == '__main__':
    main()
