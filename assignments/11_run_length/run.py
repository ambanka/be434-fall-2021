#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-15
Purpose: I compress strings of DNA
"""
import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I compress strings of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        help='DNA text or file',
                        metavar='str',
                        type=str)

    args = parser.parse_args()

    if os.path.isfile(args.seq):
        args.seq = open(args.seq).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for seq in args.seq.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq: str) -> str:
    """Run-length encoding"""

    previous = ''
    li = []
    count = 1
    for char in seq:
        if previous == '':
            previous = char
            count = 1
        elif char == previous:
            count += 1
        else:
            li.append((previous, count))
            count = 1
        previous = char
    li.append((previous, count))
    final = []
    for tup in li:
        if tup[1] == 1:
            final.append(tup[0])
        else:
            final.append(tup[0])
            final.append(tup[1])
    print(*final, sep='', end='')

    return ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
