#!/usr/bin/env python3
"""
Author : abanka <abanka@localhost>
Date   : 2021-09-12
Purpose: I add integers up
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I add integers up',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('int',
                        help='Numbers to add',
                        metavar='INT',
                        type= int,
                        nargs='+')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Why am I hearing jazz music?"""

    args = get_args()
    values = args.int
    strings = [str(n) for n in values]
    print(' + '.join(strings) + ' = ' + str(sum(values)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
