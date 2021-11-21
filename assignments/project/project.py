#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-06
Purpose: I'm helping trace the lineage of ssRNA seq results
"""
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from matplotlib import rcParams
import scanpy as spy



spy.settings.verbosity = 3
# will make scanpy the most helpful

spy.set_figure_params(dpi=80)
# low dots/inch yields small inline figures? - from one source
# (dpi=80, frameon=False, figsize=(3, 3), facecolor='white') [further other settings] - from another source?
# ????

spy.logging.print_versions()
# ????

results_file = './results/sc_j19_paga.h5ad'
# sets the file location for the results, I hope?


# ----------------------------------------------
"""Let's assume the preprocessing was done previously?"""

# -----------------------------------------------
"""Clustering @ diff resolutions"""
#adata = spy.read_10x_mtx()




# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="I'm helping trace the lineage of ssRNA seq results",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('input',
    #                     help='Please add input file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'))
                  
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
        
  


# --------------------------------------------------
if __name__ == '__main__':
    main()
