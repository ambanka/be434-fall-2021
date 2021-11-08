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
    lines_list = file.read().split()
    print(*lines_list, sep='\n')
    line1 = lines_list[0]
    line2 = lines_list[1]

    # think about utilizing map, enumerate, #
    # filter, lambda, something to write an algorithm to do this #

    if len(lines_list) == 2:
        for n in range(len(line1)):
            if line1[n] == line2[n]:
                print('|', end='')
            else:
                print('X', end='')

    if len(lines_list) == 3:
        line3 = lines_list[2]
        for n in range(len(line1)):
            if line1[n] == line2[n] == line3[n]:
                print('|', end='')
            else:
                print('X', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
