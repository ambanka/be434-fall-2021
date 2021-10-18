#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-10-17
Purpose: I take IUPAC DNA codes & tell you what the sequence options are
"""
import argparse
import sys
import os
import re
from typing import Sequence

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I take IUPAC DNA codes & tell you what the sequence options are',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='SEQ',
                        type=str,                    
                        nargs='+', 
                        help='Input sequence(s)')

    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.sequence

    dict = {'R':'[AG]', 'Y':'[CT]','S':'[GC]','W':'[AT]','K':'[GT]','M':'[AC]','B':'[CGT]','D':'[AGT]','H':'[ACT]','V':'[ACG]','N':'[ACGT]'}

 

    for y in input[0:]:
        def multiple_replace(dict, y):
            regex = re.compile("|".join(map(re.escape, dict.keys(  ))))
            return(regex.sub(lambda match: dict[match.group(0)], y))
        line1 = y + ' '
        line2 = multiple_replace(dict, y) + '\n'
        args.outfile.write(line1)
        args.outfile.write(line2)
    

    file = args.outfile.name
    if os.path.isfile(file):
        print(f'Done, see output in "{args.outfile.name}"')
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
