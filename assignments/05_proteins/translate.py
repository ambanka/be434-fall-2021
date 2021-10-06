#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-10-05
Purpose: I translate nucleic acid sequences to amino acid sequences
"""
import argparse
import os
from textwrap import wrap

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I translate nucleic acid sequences to amino acid sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('NAseq',
                        metavar='str',
                        help='Nucleic acid sequence')


    parser.add_argument('-c',
                        '--codons',
                        help='You must specify the codon table so that I can translate appropriately',
                        metavar='FILE',
                        nargs=1, 
                        type=argparse.FileType('rt'))


    # parser.add_argument('-o',
    #                     '--outfile',
    #                     help='Output filename',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default='out.txt')


    args = parser.parse_args()
    # if not 0 <= args.codons.nargs:
    #     parser.error('No')
    return args


# --------------------------------------------------
def main():
    """Bioinformatics finally commences"""

    args = get_args()
    NAseq = args.NAseq
    cotab = args.codons

    print(NAseq)
    chunked = wrap(NAseq, 3)
    print(chunked)
    val_list = []
    ki_list = []

    for line in cotab:
        tablereadin = line.readlines()
        line.close()

    for x in tablereadin:
        ki_list.append(x[0:3])
    for y in tablereadin: 
        val_list.append(y[4:5])

    ttable = {ki_list[i]:val_list[i] for i in range(len(ki_list))}
    print(ttable)

        # for item in chunked:
        #     if item in yoyo[0:3]:
        #         print('yes')
        #     else:
        #         print('garbage')
        # line.close()
    # print(yoyo)





    # kiwi = []
    # for x in yoyo:
    #     ki = x[0:3]
    #     kiwi = ki[0:]
    #     # print(ki)
    # print(kiwi)
    # for y in yoyo: 
    #     val = y[4:5]
    #     print(val)

    # for tri in chunked:

    # for x in yoyo:
    #     ttable[line]

 # ttable[line[0].upper()] = line.splitlines()

    # fh = open(cotab)
    # print(fh.splitlines())


      



    # print(ttable)
    # for x in chunked:


# --------------------------------------------------
if __name__ == '__main__':
    main()
