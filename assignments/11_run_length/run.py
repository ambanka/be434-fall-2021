#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-15
Purpose: I compress strings of DNA
"""
import argparse


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


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq
    print(seq)
    # n-1
    # map?
    basenumbers = []
    # for seq[0:]:
    #     if seq[n] == seq[n+1]:
    #         print(seq[n])

    for base in args.seq:
        basenumbers.append({base:1})

    for seq[n] in seq:
        print(seq[n])
    print(basenumbers[1])
    # for bases in args.seq:
    #     if bases[1] != bases[2]:
    #         basenumbers.append({bases:1})
        # if base[n] == base[n+1]:
        #     count = 2
        # when base[n] == base[n+1]
        #     count += 1
        # basenumbers.append({base:1})
        

    print(basenumbers)


# --------------------------------------------------
if __name__ == '__main__':
    main()
