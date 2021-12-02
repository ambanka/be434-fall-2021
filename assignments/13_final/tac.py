#!/usr/bin/env python3
"""
Author : abanka <abanka@localhost>
Date   : 2021-12-02
Purpose: I print the lines of a file in reverse!
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I print the lines of a file in reverse!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        nargs='+',
                        metavar='FILE',
                        type=str)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
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
    for file in args.file[0:]:
        contents = (open(file).read()).strip().split('\n')
        contents = [item for item in contents if str(item).islower()]
        contents.reverse()
        for line in contents:
            args.outfile.write(line)
            args.outfile.write('\n')
    args.outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
