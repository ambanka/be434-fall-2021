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
        # print(rle(seq))
        print(seq)


# --------------------------------------------------
def rle(seq: str) -> str:
    """Run-length encoding"""
    
   
   return ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
