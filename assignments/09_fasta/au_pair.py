#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-01
Purpose: Split FASTA Files with Interleaved Paired Reads
"""
import argparse
from io import StringIO
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
                        nargs='+',
                        type=str,
                        default=None)

    parser.add_argument('-o',
                        "--outdir",
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    args = parser.parse_args()
    for i in args.FILE:
        if not os.path.isfile(i):
            parser.error(f'No such file or directory: "{i}"')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files = args.FILE
    

    for file in args.FILE:
        file_name = os.path.basename(file)
        end = file_name.rfind('.')
        fwd_file = file_name[:end] + '_1' + file_name[end:]
        rvs_file = file_name[:end] + '_2' + file_name[end:]
        Ffile = open(fwd_file,"wt")
        Rile = open(rvs_file,"wt")

        reader = SeqIO.parse(file, 'fasta')
        for rec in reader:
            print('ID :', rec.id)
            print('Seq:', str(rec.seq))


        Ffile.close()
        Rfile.close()


        # fwd_file = i.split(".", 2)
        # print(fwd_file)
        # new_fwd_file = append("jo","bob")
        # # (f'{fwd_file[1]},{fwd_file[2]}').cat
        # print(new_fwd_file)
        # new_fwd_file = open.(f'{fwd_file[1]}')

    for i in args.FILE:
        reader = SeqIO.parse(i, 'fasta')
        for rec in reader:
            # file1 = open(f'{str(files_list[i])}_1.fa', 'x')
            print('ID :', rec.id)
            print('Seq:', str(rec.seq))
            # out_files.write('ID :', rec.id)
            # out_files.write('Seq:', str(rec.seq))
    ### cat

    # out_files = open(args.o/alex)
    # for line in out_files:
    #     print line


# --------------------------------------------------
if __name__ == '__main__':
    main()
