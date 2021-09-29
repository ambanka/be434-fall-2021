#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-09-22
Purpose: I concatenate files - that means join
"""

import argparse
import os


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
            if os.path.isfile(i.name):
                blah = open(i.name, "r")
                line_list = blah.readlines()
                blah.close()
                numbering = 1
                for q in line_list:
                    numbered_lines = '     ' + "{}".format(
                        numbering) + '\t' + q.rstrip()
                    # changed " " to "\t" to move it to a tab but it's still unhappy
                    numbering += 1
                    print(numbered_lines)
    else:
        for i in files[0:]:
            if os.path.isfile(i.name):
                blah = open(i.name).read().rstrip()
                print(blah)


# --------------------------------------------------
if __name__ == '__main__':
    main()
