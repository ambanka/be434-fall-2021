#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-09-22
Purpose: I concatenate files - that means join
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I concatenate files - that means join',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fi',
                        help='Input files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Bwam bwam bwam bwaaaaa"""

    args = get_args()
    files = args.fi

    if args.number:
        for i in files[0:]:
            line_list = i.readlines()
            i.close()
            numbering = 1
            for q in line_list:
                numbered_lines = '     ' + "{}".format(
                    numbering) + '\t' + q.rstrip()
                numbering += 1
                print(numbered_lines)
    else:
        for i in files[0:]:
            print(i.read().rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
