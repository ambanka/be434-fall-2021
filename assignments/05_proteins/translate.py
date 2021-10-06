#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-10-05
Purpose: I translate nucleic acid sequences to amino acid sequences
"""
import argparse
from textwrap import wrap


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description=
        'I translate nucleic acid sequences into amino acid sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('NAseq', metavar='str', help='Nucleic acid sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help=
        'You must specify the codon table so that I can translate appropriately',
        metavar='FILE',
        nargs=1,
        type=argparse.FileType('rt'),
        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """Bioinformatics finally commences"""

    args = get_args()
    NAseq = args.NAseq
    cotab = args.codons

    uppercase = NAseq.upper()
    chunked = wrap(uppercase, 3)
    val_list = []
    ki_list = []
    aa_seq = ''

    for line in cotab:
        tablereadin = line.readlines()
        line.close()

    for x in tablereadin:
        ki_list.append(x[0:3])
    for y in tablereadin:
        val_list.append(y[4:5])

    ttable = {ki_list[i]: val_list[i] for i in range(len(ki_list))}

    for q in range(len(chunked)):
        if chunked[q] in ttable:
            aa_seq += ttable.get(chunked[q])
        else:
            aa_seq += "-"

    args.outfile.write(aa_seq)
    outfi = args.outfile.name
    print('Output written to "' + outfi + '".')
    args.outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
