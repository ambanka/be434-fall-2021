#!/usr/bin/env python3
"""
Author : abanka <abanka@localhost>
Date   : 2021-11-22
Purpose: I kinda copy the normal functions of grep
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I kinda copy the normal functions of grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('file',
                        help='Input file(s)',
                        nargs='+',
                        metavar='FILE',
                        type=str)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        type=argparse.FileType('wt'),
                        metavar='FILE',
                        help='Output',
                        default=sys.stdout)

    args = parser.parse_args()

    for file in args.file:
        if not os.path.isfile(file):
            parser.error(f"No such file or directory: '{file}'")

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.insensitive:
        pattern = re.compile(args.pattern, re.IGNORECASE)
    else:
        pattern = re.compile(args.pattern)

    for file in args.file:
        contents = open(file).read().split('\n')
        for line in contents:
            m = pattern.search(line)
            if m:
                if len(args.file) >= 2:
                    args.outfile.write(f'{file}:{line}')
                    args.outfile.write('\n')
                else:
                    args.outfile.write(line)
                    args.outfile.write('\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()
