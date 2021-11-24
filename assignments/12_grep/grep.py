#!/usr/bin/env python3
"""
Author : abanka <abanka@localhost>
Date   : 2021-11-22
Purpose: I kinda copy the normal functions of grep
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I kinda copy the normal functions of grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('file', 
                        help='Input file(s)',
                        nargs = '+', 
                        metavar='FILE',
                        type=argparse.FileType('rt'))
                    
    parser.add_argument('-i', 
                        '--insensitive', 
                        help = 'Case insensitive search', 
                        type = str, 
                        metavar = '', 
                        default = False)
                

    parser.add_argument('-o', 
                        '--outfile', 
                        type = argparse.FileType('wt'), 
                        metavar = 'FILE', 
                        help = 'Output', 
                        default= sys.stdout)


    args = parser.parse_args()

    if os.path.isfile(args.file):
        args.file = open(args.file).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
