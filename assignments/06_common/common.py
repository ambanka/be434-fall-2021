#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-10-10
Purpose: I find the words in common between two files
"""
import argparse
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

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    contents1 = args.FILE1.read()
    contents2 = args.FILE2.read()

    words1 = contents1.split()

    wordlist = []
    for x in words1:
        pattern = re.compile((x) + r'[\s,.]')
        overlap = pattern.search(contents2)
        if overlap:

            word = overlap.group(0)

            wordlist.append(word.rstrip())

    wordlist.sort()
    no_duplicates = list(dict.fromkeys(wordlist))
    final = "\n".join(no_duplicates)
    args.outfile.write(final)
    args.outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
