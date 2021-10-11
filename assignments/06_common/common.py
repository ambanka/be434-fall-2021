#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-10-10
Purpose: I find the words in common between two files
"""
import argparse
import os
import sys
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="I'm a snitch",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))
 #this outputs a class '_io.TextIOWrapper'
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default = sys.stdout)
        #this outputs a class '_io.TextIOWrapper'
 

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    contents1 = args.FILE1.read()
    contents2 = args.FILE2.read()
    # produces a string

    words1 = contents1.split()
        # produces a list


    wordlist = []
    for x in words1:
        if x in contents2:
            wordlist.append(x)
    wordlist.sort()
    no_duplicates = list(dict.fromkeys(wordlist))
    final = "\n".join(no_duplicates)
    args.outfile.write(final)
    args.outfile.close()
    



    #tried a bunch of stuff with re.
        # overlap = re.search(x, contents2)
        # if overlap:
        #     word = overlap.group(0)
           # word = string
  

# --------------------------------------------------
if __name__ == '__main__':
    main()
