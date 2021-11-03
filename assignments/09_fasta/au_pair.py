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
    for file in args.FILE:
        if not os.path.isfile(file):
            parser.error(f'No such file or directory: "{file}"')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    for file in args.FILE:
        file_name = os.path.basename(file)
        end = file_name.rfind('.')
        fwd_file = file_name[:end] + '_1' + file_name[end:]
        rvs_file = file_name[:end] + '_2' + file_name[end:]
        Ffile = open(args.outdir+'/'+fwd_file,'wt')
        Rfile = open(args.outdir+'/'+rvs_file,'wt')

        dict = {}
        reader = SeqIO.parse(file, 'fasta')
        for rec in reader:
            dict.update({f'>{rec.id}' : f'{str(rec.seq)}'})
        print(dict)


            # Ffile.write(f"{'ID :', rec.id} \n")
            # Ffile.write(f"{'Seq:', str(rec.seq)}")

          

        Ffile.close()
        Rfile.close()
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
