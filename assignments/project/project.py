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

# adata = sc.read_10x_mtx('inputs/filtered_gene_bc_matrices/hg19', var_names='gene_symbols', cache = True)
#     # reads in Satan's matrix

# adata.var_names_make_unique()

# adata.X = adata.X.astype('float64')
#     # sets it to be more accurate so it's a closer mirror to Seurat's R module work
# adata.var['mt'] = adata.var_names.str.startswith('MT-')
# sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="I'm helping trace the lineage of ssRNA seq results",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('-indir',
    #                     '--input_directory', 
    #                     help = 'input directory',
    #                     metavar = 'DIR', 
    #                     type= str, 
    #                     default='./inputs/filtered_gene_bc_matrices/hg19')    

    parser.add_argument('-o', 
                        '--outfile',
                        help='What would you like to name your output file?',
                        metavar='str',
                        type=str, 
                        default='pbmc3k')

    args = parser.parse_args()

    # if not os.path.isdir(args.input_directory):
    #     parser.error(f"No such directory: '{args.input_directory}'")

    return args
              
# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    # in_data = args.input_directory
    adata = sc.read_10x_mtx('inputs/filtered_gene_bc_matrices/hg19', var_names='gene_symbols', cache = True)
        # reads in Satan's matrix

    adata.var_names_make_unique()

    adata.X = adata.X.astype('float64')
        # sets it to be more accurate so it's a closer mirror to Seurat's R module work
    
    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
       
    initial_maps(adata)
    adata = filtering(adata)
    adata = filter(adata)
    filtered_maps(adata)
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

# -------------------------------------------
def violins(adata, file_names, file_namesB):
    sc.pl.violin(adata, 'n_genes_by_counts', jitter = 0.4, xlabel='Number of Genes/Cell', size = 2, ylabel='', save = file_namesB)
    sc.pl.violin(adata, 'total_counts', jitter=0.4, xlabel='Total Counts/Cell', size=2, ylabel='', save= file_names)
 
# -------------------------------------------
def scatter_counts_v_genes(adata, file_names):
    sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts', save = file_names)

# ---------------------------------------

def initial_maps(adata):
    file_names = '_initial'
    file_namesB = '_initial_genes_per_cell'
    top_genes(adata, file_names)
    violins(adata, file_names, file_namesB)
    scatter_counts_v_genes(adata, file_names)

# -------------------------------------
def filtering(adata):
    print("Please start small then go higher!")
    low_genes = int(input("Filter out cells that have fewer than ______ genes: "))
    rare_genes = int(input("Filter out genes that are seen in fewer than ____ cells: "))
    if low_genes: 
        sc.pp.filter_cells(adata, min_genes= low_genes)
    else:
        sc.pp.filter_cells(adata, min_genes= 200)
    # filters out cells that have <200 genes detected - non-viable cells
    if rare_genes:
        sc.pp.filter_genes(adata, min_cells=rare_genes)
    else:
        sc.pp.filter_genes(adata, min_cells=10)
    # filters out genes which are expressed by <10 cells
    return(adata)

#----------------------------------------------
def filter(adata):
    adata = adata[adata.obs.n_genes_by_counts < 2500, :]
    adata = adata[adata.obs.pct_counts_mt < 5, :]
    return(adata)

def filtered_maps(adata):
    file_names = '_filtered'
    file_namesB = '_filtered_genes_per_cell'
    top_genes(adata, file_names)
    violins(adata, file_names, file_namesB)
    scatter_counts_v_genes(adata, file_names)

# def tops() ->         
#     sc.pl.highest_expr_genes(adata, n_top=20, show=True)
#     # displays top 20 genes with highest % of counts/cell [averaged across cells]

#     # spy.pp.filter_cells(adata, min_genes=200)
#     # # filters out cells that have <200 genes detected - non-viable cells

#     # spy.pp.filter_genes(adata, min_cells=10)
#     # # filters out genes which are expressed by <10 cells

        
# def get_move(state: State) -> State:
#     """Get the player's move"""

#     player = state['player']
#     cell = input(f'Player {player}, what is your move? [q to quit]: ')

#     if cell == 'q':
#         state['quit'] = True
#         return state

#     if not (cell.isdigit() and int(cell) in range(1, 10)):
#         state['error'] = f'Invalid cell "{cell}", please use 1-9'
#         return state

#     cell_num = int(cell)
#     if state['board'][cell_num - 1] in 'XO':
#         state['error'] = f'Cell "{cell}" already taken'
#         return state

#     board = list(state['board'])
#     board[cell_num - 1] = player

#     return State(
#         board=''.join(board),
#         player='O' if player == 'X' else 'X',
#         winner=find_winner(board),
#         draw='.' not in board,
#         error=None,
#         quit=False,
#     )



# -----------------------------------------------
"""Clustering @ diff resolutions"""
#adata = spy.read_10x_mtx()
# adata = spy.read('./inputs/WagnerScience2018.h5ad')


# --------------------------------------------------
if __name__ == '__main__':
    main()
