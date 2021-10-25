#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-10-22
Purpose: I find commonalities between two files
"""
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I find commanalities between two files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmers',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()
    if args.kmers <= 0:
        parser.error(f'--kmer "{args.kmers}" must be > 0')
    return args


# --------------------------------------------------
def main():
    """This can't be the fastest way to do this"""

    args = get_args()
    contents1 = args.FILE1.read()
    contents2 = args.FILE2.read()
    k = args.kmers

    def find_kmers(seq, k):
        n = len(seq) - k + 1
        return [] if n < 1 else [seq[i:i + k] for i in range(n)]

    words1 = contents1.split()
    words2 = contents2.split()
    kmer_list = set()

    counted_1 = {}
    counted_2 = {}

    for word in words1:
        for kmer in find_kmers(word, k):
            counted_1.update({kmer: 0})
            counted_2.update({kmer: 0})
            for wo in words2:
                if kmer in find_kmers(wo, k):
                    kmer_list.add(kmer)

    for word in words1:
        for kmer in find_kmers(word, k):
            if kmer in counted_1:
                counted_1[kmer] += 1

    for word in words2:
        for kmer in find_kmers(word, k):
            if kmer in counted_2:
                counted_2[kmer] += 1

    for x in kmer_list:
        print('{0: <10}'.format(x) + '{0: >6}'.format(f'{counted_1.get(x)}') +
              '{0: >6}'.format(f'{counted_2.get(x)}'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
