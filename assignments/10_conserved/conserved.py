#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-06
Purpose: I show conserved bases
"""
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='I show conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    lines_list = file.read().splitlines()
    print(*lines_list, sep='\n')

    for i in range(len(lines_list[0])):
        bases = []
        for char in lines_list:
            bases += char[i]
        # if all([bases[0] == base for base in bases]):
        if len(set(bases)) == 1:
            print('|', end='')
        else:
            print('X', end='')
    # printing alt conserved += | or X & print(conserved)
    # conserved += '|' if len(set(bases)) == 1 else 'X' & prnt cons


# --------------------------------------------------
if __name__ == '__main__':
    main()
