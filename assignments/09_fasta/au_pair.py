#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-01
Purpose: Split FASTA Files with Interleaved Paired Reads
"""
import argparse
from Bio import SeqIO
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split Interleaved/Paired Reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('FILE',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs = '+',
                        type = argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        "--outdir",
                        help='Output directory',
                        metavar='DIR',
                        type= os.path.dirname , 
                        default= '../split')

    args = parser.parse_args()
    # files_list = args.FILE
    # for i in files_list:
    #     if os.path.isfile(i):
    #         parser.error(f'No such file or directory: "{files_list[i]}"')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files_list = args.FILE
    director = args.outdir
    print(director)

    if not os.path.exists(f'{args.outdir}'):
        os.mkdir(f'{args.outdir}')

    # out_files = open(director/'alex')


        # for i in files_list:
        #     reader = SeqIO.parse(i, 'fasta')
        #     for rec in reader:
        #         out_files.write('ID :', rec.id)
        #         out_files.write('Seq:', str(rec.seq))
        ### cat

    # out_files = open(args.o/alex)
    # for line in out_files:
    #     print line

# --------------------------------------------------
if __name__ == '__main__':
    main()
